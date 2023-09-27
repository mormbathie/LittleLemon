from django.test import TestCase
from LittleLemon.LittleLemon.Restaurant.models import MenuTable


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(tite="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")