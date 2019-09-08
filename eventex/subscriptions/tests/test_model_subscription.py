from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ricardo Beckert',
            cpf='12345678901',
            email='beckert.ricardo@gmail.com', 
            phone='48-99999-0001'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscrition must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual('Ricardo Beckert', str(self.obj))
