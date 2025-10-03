from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        # Create users
        self.user1 = User.objects.create_user(username="user1", password="testpass123")
        self.user2 = User.objects.create_user(username="user2", password="testpass123")

        # Create a blog post
        self.post = Post.objects.create(
            title="Test Post",
            content="Post content",
            author=self.user1
        )

        # Create a comment
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user1,
            content="Initial comment"
        )

    def test_create_comment_authenticated(self):
        """Authenticated users can create comments on a post"""
        self.client.login(username="user1", password="testpass123")
        response = self.client.post(
            reverse("comment_create", args=[self.post.id]),
            {"content": "This is a new comment"}
        )
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertEqual(Comment.objects.count(), 2)
        self.assertTrue(Comment.objects.filter(content="This is a new comment").exists())

    def test_create_comment_unauthenticated(self):
        """Unauthenticated users cannot create comments"""
        response = self.client.post(
            reverse("comment_create", args=[self.post.id]),
            {"content": "Should not work"}
        )
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)  # only the initial one exists

    def test_update_comment_by_author(self):
        """Comment author can edit their own comment"""
        self.client.login(username="user1", password="testpass123")
        response = self.client.post(
            reverse("comment_update", args=[self.post.id, self.comment.id]),
            {"content": "Updated comment"}
        )
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, "Updated comment")

    def test_update_comment_by_non_author(self):
        """Non-authors cannot edit someone else’s comment"""
        self.client.login(username="user2", password="testpass123")
        response = self.client.post(
            reverse("comment_update", args=[self.post.id, self.comment.id]),
            {"content": "Hacked edit"}
        )
        self.comment.refresh_from_db()
        self.assertNotEqual(self.comment.content, "Hacked edit")
        self.assertEqual(response.status_code, 403)  # Forbidden

    def test_delete_comment_by_author(self):
        """Comment author can delete their own comment"""
        self.client.login(username="user1", password="testpass123")
        response = self.client.post(
            reverse("comment_delete", args=[self.post.id, self.comment.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_delete_comment_by_non_author(self):
        """Non-authors cannot delete someone else’s comment"""
        self.client.login(username="user2", password="testpass123")
        response = self.client.post(
            reverse("comment_delete", args=[self.post.id, self.comment.id])
        )
        self.assertEqual(response.status_code, 403)  # Forbidden
        self.assertTrue(Comment.objects.filter(id=self.comment.id).exists())
