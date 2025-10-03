from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class BlogPostTests(TestCase):
    """
    Test suite for blog post CRUD operations, access control, and navigation.
    """

    def setUp(self):
        # Create two users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a post by user1
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user1
        )

        self.client = Client()

    # ---------------------------
    # 1. Test List and Detail Views
    # ---------------------------
    def test_post_list_view_accessible_to_all(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_post_detail_view_accessible_to_all(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.content)

    # ---------------------------
    # 2. Test Post Creation
    # ---------------------------
    def test_create_post_authenticated_user(self):
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'content': 'Content for new post'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after creation
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_create_post_unauthenticated_user_redirected(self):
        response = self.client.get(reverse('post_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    # ---------------------------
    # 3. Test Post Update
    # ---------------------------
    def test_update_post_by_author(self):
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('post_update', args=[self.post.pk]), {
            'title': 'Updated Title',
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_update_post_by_non_author_forbidden(self):
        self.client.login(username='user2', password='password123')
        response = self.client.post(reverse('post_update', args=[self.post.pk]), {
            'title': 'Hacked Title',
            'content': 'Hacked content'
        })
        self.assertEqual(response.status_code, 403)
        self.post.refresh_from_db()
        self.assertNotEqual(self.post.title, 'Hacked Title')

    # ---------------------------
    # 4. Test Post Deletion
    # ---------------------------
    def test_delete_post_by_author(self):
        self.client.login(username='user1', password='password123')
        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_delete_post_by_non_author_forbidden(self):
        self.client.login(username='user2', password='password123')
        response = self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

    # Navigation test
            
class BlogPostNavigationTests(TestCase):
    """
    Tests for navigation links/buttons visibility in blog post templates.
    """

    def test_post_list_contains_links_to_detail(self):
        """
        Ensure each post in the list view contains a link to its detail page.
        """
        response = self.client.get(reverse('post_list'))
        detail_url = reverse('post_detail', args=[self.post.pk])
        self.assertContains(response, detail_url)


    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')

        # Create a post by user1
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user1
        )

        self.client = Client()

    def test_edit_delete_links_visible_to_author(self):
        """
        Ensure Edit and Delete buttons are visible only to the author.
        """
        self.client.login(username='user1', password='password123')
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))

        edit_url = reverse('post_update', args=[self.post.pk])
        delete_url = reverse('post_delete', args=[self.post.pk])

        # Author should see the Edit and Delete buttons
        self.assertContains(response, edit_url)
        self.assertContains(response, delete_url)

    def test_edit_delete_links_hidden_from_non_author(self):
        """
        Ensure Edit and Delete buttons are not visible to other users.
        """
        self.client.login(username='user2', password='password123')
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))

        edit_url = reverse('post_update', args=[self.post.pk])
        delete_url = reverse('post_delete', args=[self.post.pk])

        # Non-author should NOT see the buttons
        self.assertNotContains(response, edit_url)
        self.assertNotContains(response, delete_url)

    def test_edit_delete_links_hidden_from_anonymous(self):
        """
        Ensure Edit and Delete buttons are not visible to unauthenticated users.
        """
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))

        edit_url = reverse('post_update', args=[self.post.pk])
        delete_url = reverse('post_delete', args=[self.post.pk])

        self.assertNotContains(response, edit_url)
        self.assertNotContains(response, delete_url)

