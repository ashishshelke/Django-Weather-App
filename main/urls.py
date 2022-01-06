from django.urls import path
from .views import home, newhome


urlpatterns = [
    path('', home, name='home'),
    path('new/', newhome, name='home'),
]
