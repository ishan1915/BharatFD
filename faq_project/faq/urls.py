from django.urls import path
from .views import FAQListView, FAQDetailView

urlpatterns = [
    path('faqs/', FAQListView.as_view(), name='faq-list'),
    path('faqs/<int:pk>/', FAQDetailView.as_view(), name='faq-detail'),
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
