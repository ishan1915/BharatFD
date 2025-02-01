
from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )

    def test_translation_fallback(self):
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")
