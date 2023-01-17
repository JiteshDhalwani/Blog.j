from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("create_blog", views.create_blog, name="create_blog"),
    path("view_blog/<int:blog_id>", views.view_blog, name="view_blog"),
    path("delete_blog/<int:blog_id>", views.delete_blog, name="delete_blog"),
    path("show_category/<str:category>", views.show_category, name="show_category"),
    path("display_user/<int:user_id>", views.display_user, name="display_user"),
    path("search", views.search, name="search"),
]