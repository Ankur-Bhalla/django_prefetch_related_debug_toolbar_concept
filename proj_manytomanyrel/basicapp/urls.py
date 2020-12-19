from django.urls import path
from basicapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
