from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse

from .forms import PostForm, CommentForm
from .models import Post, Comment
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
    search_query = request.GET.get("search", "")

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(content__icontains=search_query)
        ).order_by("-created_at")

    else:
        posts = Post.objects.order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_obj = request.GET.get("page")
    try:
        posts = paginator.page(page_obj)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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


@login_required(login_url="/users/login")
def post_new(request):
    context = {}
    form = PostForm(request.POST, request.FILES)

    if request.method == "POST":
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "article.html", context)


@login_required(login_url="/users/login")
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = request.user
            result.save()
            return redirect("/")
    elif request.method == "GET":
        data = {
            "title": post.title,
            "description": post.description,
            "category": post.category,
            "content": post.content,
        }
        form = PostForm(initial=data)
    else:
        pass

    context = {"form": form}
    return render(request, "article.html", context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            # Заложил для дальнейшей реализации Комментармй на комментарий
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            comm.user = request.user
            comm.post = post
            comm.save()
    else:
        form = CommentForm()
    return render(
        request,
        "detailed_article.html",
        {"menu": menu.all(), "post": post, "form": form, "comment": comment},
    )


def posts_category(request, alias):
    search_query = request.GET.get("search", "")

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(content__icontains=search_query)
        ).order_by("-created_at")

    else:
        posts = Post.objects.filter(category__alias=alias).order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_obj = request.GET.get("page")
    try:
        posts = paginator.page(page_obj)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "home_page.html",
        {"page_obj": page_obj, "posts": posts, "menu": menu.all()},
    )


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


def search_post_json(request):
    search = request.GET.get("search", "")

    if not search:
        posts = Post.objects.none().values("id", "title")
    else:
        posts = (
            Post.objects.filter(Q(title__icontains=search))
            .order_by("-created_at")
            .values("id", "title")[:10]
        )

    posts = list(posts)

    return JsonResponse(posts, safe=False)
