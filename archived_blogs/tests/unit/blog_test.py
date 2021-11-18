from unittest import TestCase

from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        expected_repr = f"Blog(title={b.title}, author={b.author}, " \
                        f"Posts={b.posts})"

        self.assertEqual(b.__repr__(), expected_repr)

    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        expected_repr = f"Blog(title={b.title}, author={b.author}, " \
                        f"Posts={b.posts})"

        self.assertEqual(b.__repr__(), expected_repr)
