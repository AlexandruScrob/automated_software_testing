from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': "Test",
            'author': "Test Author",
            'posts': [post.json() for post in b.posts]
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post("Test Post", "Test Content")

        expected = {
            'title': b.title,
            'author': b.author,
            'posts': [post.json() for post in b.posts]
        }

        self.assertDictEqual(expected, b.json())
