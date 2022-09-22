from django.test import TestCase, Client

# Create your tests here.
class TestUrl (TestCase):
    def test_url(self):
        self.assertEqual(Client().get('/katalog').status_code,200)