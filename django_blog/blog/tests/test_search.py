from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostSearchTests(TestCase):
    def setUp(self):
        """
        Create a test user and some posts with different tags and content.
        """
        self.user = User.objects.create_user(username="testuser", password="password")

        self.post1 = Post.objects.create(
            title="Django Tutorial",
            content="Learn Django step by step.",
            author=self.user,
        )
        self.post1.tags.add("django", "tutorial")

        self.post2 = Post.objects.create(
            title="Python Basics",
            content="Introduction to Python programming.",
            author=self.user,
        )
        self.post2.tags.add("python", "programming")

        self.post3 = Post.objects.create(
            title="Blogging Tips",
            content="How to start blogging.",
            author=self.user,
        )
        self.post3.tags.add("blogging")

    def test_search_by_title(self):
        """
        Search should return posts matching the title.
        """
        results = Post.objects.filter(title__icontains="Django")
        self.assertIn(self.post1, results)
        self.assertNotIn(self.post2, results)
        self.assertNotIn(self.post3, results)

    def test_search_by_content(self):
        """
        Search should return posts matching the content.
        """
        results = Post.objects.filter(content__icontains="Python")
        self.assertIn(self.post2, results)
        self.assertNotIn(self.post1, results)
        self.assertNotIn(self.post3, results)

    def test_search_by_tags(self):
        """
        Search should return posts matching tags.
        """
        results = Post.objects.filter(tags__name__icontains="blogging").distinct()
        self.assertIn(self.post3, results)
        self.assertNotIn(self.post1, results)
        self.assertNotIn(self.post2, results)

    def test_search_no_results(self):
        """
        Search should return an empty queryset if no matches are found.
        """
        results = Post.objects.filter(title__icontains="Nonexistent").distinct()
        self.assertEqual(results.count(), 0)
