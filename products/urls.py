from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>/', views.detail, name='detail'),
]
