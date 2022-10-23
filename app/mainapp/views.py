from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .models import Post
from .utils import *

menu = Category.objects.all()


class HomePageView(TemplateView):
    template_name = "home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Page404(TemplateView):
    template_name = "404_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DetailedArticle(TemplateView):
    template_name = "detailed_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def reg_page(request):
    return render(request, "register.html")


def terms_of_service(request):
    return render(request, "terms_of_service.html")


def all_posts(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |
                                    Q(description__icontains=search_query) |
                                    Q(content__icontains=search_query)).order_by("-created_at")

    else:
        posts = Post.objects.all().order_by("-created_at")
    return render(request, "home_page.html", {"posts": posts, "menu": menu})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "detailed_article.html", {"menu": menu, "post": post})


@user_passes_test(lambda u: u.is_superuser)
def create_demo_post(request):
    user = request.user
    DemoPosts.create_demo_post(user)
    return redirect("/")


@user_passes_test(lambda u: u.is_superuser)
def delete_demo_posts(request):
    posts = Post.objects.filter(title__startswith="DEMO ")
    [post.delete() for post in posts]
    return redirect("/")


def posts_category(request, alias):
    posts = Post.objects.filter(category__alias=alias).order_by("-created_at")
    # posts = Post.objects.filter(postCategory__id=pk)
    return render(request, "home_page.html", {"posts": posts, "menu": menu})
