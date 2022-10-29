from django.urls import path

from .apps import MainappConfig
from . import views

app_name = MainappConfig.name

urlpatterns = [
    path("search-post-json/", views.search_post_json, name="search-post-json"),
    path("", views.all_posts, name="home"),
    path("posts/<int:post_id>/", views.detail, name="detail"),
    path("post_new/", views.post_new, name="post-new"),
    path("post_edit/<int:post_id>/", views.post_edit, name="post-edit"),
    path("<int:author_id>/", views.author_posts, name="author-posts"),
    path("reg_page/", views.reg_page, name="reg_page"),
    path("terms_of_service/", views.terms_of_service, name="terms_of_service"),
    path("detailed_article/", views.DetailedArticle.as_view(), name="detailed_article"),
    path("create_demo_post/", views.create_demo_post, name="create_demo_post"),
    path("delete_demo_posts/", views.delete_demo_posts, name="delete_demo_posts"),
    path("create_category/", views.create_category, name="create_category"),
    path("<slug:alias>/", views.posts_category, name="posts_category"),
    path("page_404/", views.Page404.as_view(), name="page_404"),
]
