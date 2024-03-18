from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='posts'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('post/create', views.create_post, name='post_create'),
    path('post/edit/<int:id>/',views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),

]