from django.urls import path
from .views import SitesHomePage

urlpatterns = [
    path('', SitesHomePage.as_view(), name='sites-main'),
]



