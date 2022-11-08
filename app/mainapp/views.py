from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse, Http404

from .forms import PostForm, CommentForm
from .models import Post, Comment
from .utils import *
from userapp.models import User


menu = Category.objects.all()


class HomePageView(TemplateView):
    template_name = "home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def error_404_view(request, exception):
    return render(request, "404.html")


def error_400_view(request, exception):
    return render(request, "400.html")


def error_403_view(request, exception):
    return render(request, "403.html")


def error_500_view(request):
    return render(request, "500.html", status=500)


class DetailedArticle(TemplateView):
    template_name = "detailed_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def reg_page(request):
    return render(request, "register.html")


def terms_of_service(request):
    return render(request, "terms_of_service.html")


def statistic(request):
    active_posts = Post.objects.filter(active=True, is_deleted=False)
    on_moderation_posts = Post.objects.filter(active=False, is_deleted=False)
    deleted_posts = Post.objects.filter(is_deleted=True)
    verified_user = User.objects.filter(is_email_verified=True, delete=False)
    not_verified_user = User.objects.filter(is_email_verified=False, delete=False)
    deleted_user = User.objects.filter(delete=True)
    return render(
        request,
        "statistic.html",
        {
            "active_posts": active_posts,
            "on_moderation_posts": on_moderation_posts,
            "deleted_posts": deleted_posts,
            "verified_user": verified_user,
            "not_verified_user": not_verified_user,
            "deleted_user": deleted_user,
            "menu": menu.filter(active=True),
        },
    )


def all_posts(request):
    search_query = request.GET.get("search", "")

    if search_query:
        posts = Post.objects.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(content__icontains=search_query)
        ).order_by("-created_at")

    else:
        post_count = Post.objects.all().count
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
        {
            "page_obj": page_obj,
            "posts": posts,
            "menu": menu.filter(active=True),
            "post_count": post_count,
        },
    )


def author_posts(request, author_id):
    posts = Post.objects.filter(user_id=author_id).order_by("-created_at")
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "home_page.html",
        {"page_obj": page_obj, "posts": posts, "menu": menu.filter(active=True)},
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

    context = {"form": form, "menu": menu.filter(active=True)}
    return render(request, "article.html", context)


@login_required(login_url="/users/login")
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            result = form.save(commit=False)
            if request.user.is_superuser:
                result.user = post.user
            else:
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


@login_required(login_url="/users/login")
def post_delete(request, post_id):
    post_owner = Post.objects.values("user").get(pk=post_id)["user"]
    if request.user.id == post_owner or request.user.is_superuser:
        Post.objects.get(pk=post_id).delete()
    return redirect("/")


def post_detail(request, post_id):
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
        {
            "menu": menu.filter(active=True),
            "post": post,
            "form": form,
            "comment": comment,
        },
    )


def posts_category(request, alias):
    search_query = request.GET.get("search", "")
    for e in Category.objects.all():
        if alias == e.alias:
            if search_query:
                posts = Post.objects.filter(
                    Q(title__icontains=search_query)
                    | Q(description__icontains=search_query)
                    | Q(content__icontains=search_query)
                ).order_by("-created_at")
            else:
                post_count = Post.objects.filter(category__alias=alias).count
                posts = Post.objects.filter(category__alias=alias).order_by(
                    "-created_at"
                )
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
                {
                    "page_obj": page_obj,
                    "posts": posts,
                    "menu": menu.filter(active=True),
                    "post_count": post_count,
                },
            )
    raise Http404("Category not found")


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


@login_required(login_url="/users/login")
def comment_delete(request, pk):
    comment_owner = Comment.objects.values("user").get(pk=pk)["user"]
    if request.user.id == comment_owner or request.user.is_superuser:
        Comment.objects.get(pk=pk).delete()
    return redirect(request.META["HTTP_REFERER"])
