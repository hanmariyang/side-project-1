from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('review/', views.review, name='review'),
    path('detail/', views.detail, name="detail"),
    path('detail/delete/<int:id>', views.delete_detail, name='delete'),
]