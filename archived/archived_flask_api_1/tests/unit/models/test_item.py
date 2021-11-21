from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test',
                         "Name of item after creation not equal to the"
                         " constructor arg.")
        self.assertEqual(item.price, 19.99,
                         "Price of item after creation not equal to the"
                         " constructor arg."
                         )

    def test_item_json(self):
        item = ItemModel('test', 19.99)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(item.json(), expected,
                         f"JSON export is incorrect. Received {item.json()},"
                         f" expected {expected}")
