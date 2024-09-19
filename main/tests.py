from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

class MainTest(TestCase):
    def test_main_template_uses_correct_page_title(self):
        response = Client().get("/")
        html_response = response. content.decode( "utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)