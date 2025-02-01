from django.shortcuts import render
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView

class FAQListView(APIView):
    def get(self, request):
        cache_key = "faq_list"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        cache.set(cache_key, serializer.data, timeout=60*60)  # Cache for 1 hour
        return Response(serializer.data)


class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
