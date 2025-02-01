from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi
    question_bn = models.TextField(blank=True, null=True)  # Bengali
    created_at = models.DateTimeField(auto_now_add=True)

    def get_translated_question(self, lang='en'):
        """Fetch translated question dynamically."""
        cache_key = f"faq_{self.id}_lang_{lang}"
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation

        if lang == "hi" and self.question_hi:
            translated_text = self.question_hi
        elif lang == "bn" and self.question_bn:
            translated_text = self.question_bn
        else:
            translated_text = translator.translate(self.question, dest=lang).text
            if lang == "hi":
                self.question_hi = translated_text
            elif lang == "bn":
                self.question_bn = translated_text
            self.save()

        cache.set(cache_key, translated_text, timeout=60*60)
        return translated_text
