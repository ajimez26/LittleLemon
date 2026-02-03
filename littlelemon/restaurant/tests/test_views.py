from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer  # assuming you have a serializer

class MenuItemsViewTest(TestCase):
    def setUp(self):
        # Initialize test client
        self.client = APIClient()

        # Create some test MenuItem instances
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Pizza", price=150, inventory=50)
        self.item3 = MenuItem.objects.create(title="Burger", price=120, inventory=70)

    def test_get_all(self):
        # Make a GET request to your view endpoint
        response = self.client.get("/restaurant/menu-items/")  # replace with your actual URL

        # Serialize all MenuItem objects
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

