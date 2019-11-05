from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('', views.post_detail, name='navbookmark'),
    # path('post/<int:pk>/', views.navbookmark, name='bookmark'),
]