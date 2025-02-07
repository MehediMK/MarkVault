from django.urls import path, include
from .views import blog_list, create_blog


urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("create/", create_blog, name="create_blog"),
]
