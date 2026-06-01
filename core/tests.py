from django.test import TestCase


class HomeViewTests(TestCase):
    def test_home_returns_success_message(self):
        response = self.client.get("/")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", data)
        self.assertIn("Django CI/CD", data["message"])
