from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='edit')
]