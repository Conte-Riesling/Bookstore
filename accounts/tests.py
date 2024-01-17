from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="root", email="root@gmail.com", password="12345"
        )
        self.assertEqual(user.username, "root")
        self.assertEqual(user.email, "root@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="root", email="root@gmail.com", password="12345"
        )
        self.assertEqual(admin_user.username, "root")
        self.assertEqual(admin_user.email, "root@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

