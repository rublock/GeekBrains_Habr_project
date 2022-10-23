from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm
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
    posts = Post.objects.order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "home_page.html",
        {"page_obj": page_obj, "posts": posts, "menu": menu.all()},
    )

def author_posts(request, author_id):
    posts = Post.objects.filter(user_id=author_id).order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "home_page.html",
        {"page_obj": page_obj, "posts": posts, "menu": menu.all()},
    )

@login_required(login_url='/users/login')
def post_new(request):
    context = {}
    form = PostForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request, "article.html", context)


 

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "detailed_article.html", {"menu": menu.all(), "post": post})


def posts_category(request, alias):
    posts = Post.objects.filter(category__alias=alias).order_by("-created_at")
    return render(request, "home_page.html", {"posts": posts, "menu": menu.all()})


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


@user_passes_test(lambda u: u.is_superuser)
def create_category(request):
    user = request.user
    DemoPosts.create_category(user)
    return redirect("/")
