from django.urls import path

from .apps import MainappConfig
from . import views

app_name = MainappConfig.name

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('', views.all_posts, name='home'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('page_404/', views.Page404.as_view(), name='page_404'),
    path('reg_page/', views.reg_page, name='reg_page'),
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('detailed_article/', views.DetailedArticle.as_view(), name='detailed_article'),
]
