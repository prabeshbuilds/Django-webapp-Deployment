from django.test import TestCase


class HomeViewTests(TestCase):
    def test_home_returns_success_message(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {"message": "Django CI/CD is running successfully!"},
        )
