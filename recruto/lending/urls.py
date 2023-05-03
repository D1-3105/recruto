from django.urls import path, re_path
from .views import HelloView

urlpatterns = [
    path('', HelloView.as_view(), name='main'),
]