from django.test import TestCase

class TryDjangoConfigTest(TestCase):
    def test_one(self):
        self.assertTrue(1==1)
        self.assertFalse(1==1)
        self.assertIsNone(1==2)
        self.assertIsNotNone(1==2)
        self.assertEqual(1,2)
        self.assertNotEqual(1,2)