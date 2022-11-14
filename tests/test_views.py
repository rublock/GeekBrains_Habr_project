import pytest
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser, Group
from django.http.response import HttpResponse
from django.test import RequestFactory, TestCase
from django.urls import reverse, reverse_lazy
from mainapp.models import Post
from userapp.models import User
from mainapp.views import post_delete, post_detail, post_edit, post_new
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        moder_gr = Group.objects.get(name="moderator")
        mixer.blend("mainapp.Post", id=1, active=True)
        cls.factory = RequestFactory()

    def test_new_post_for_authenticated(self):
        strong_password = "Str#410-P@55"
        user = User.objects.create_user(
            username="asdf", email="asdf@example.com", password=strong_password
        )
        self.client.login(username=user.username, password=strong_password)
        path = reverse("mainapp:post-new")
        request = self.client.get(path)
        request.user = user

        if isinstance(httpresp := request.json.args[0], HttpResponse):
            status_code = httpresp.status_code
        assert status_code == 200

    def test_new_post_for_unauthenticated(self):
        path = reverse("mainapp:post-new")
        request = self.client.get(path)
        request.user = AnonymousUser()

        if isinstance(httpresp := request.json.args[0], HttpResponse):
            status_code = httpresp.status_code
        assert status_code == 302

    def test_post_detail_authenticated(self):
        path = reverse("mainapp:post_detail", kwargs={"post_id": 1})
        request = self.factory.get(path)
        request.user = Post.objects.get(id=1).user
        response = post_detail(request, post_id=1)
        assert response.status_code == 200

    def test_post_detail_unauthenticated(self):
        path = reverse("mainapp:post_detail", kwargs={"post_id": 1})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_detail(request, post_id=1)
        assert response.status_code == 200

    def test_new_post_unauthenticated_create(self):
        path = reverse("mainapp:post-new")
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_new(request)
        assert "/users/login" in response.url

    def test_post_unauthenticated_edit(self):
        path = reverse("mainapp:post-edit", kwargs={"post_id": 1})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_edit(request, post_id=1)
        assert "/users/login" in response.url

    def test_post_unauthenticated_delete(self):
        path = reverse("mainapp:post_delete", kwargs={"post_id": 1})
        request = self.factory.get(path)
        request.user = AnonymousUser()
        response = post_delete(request, post_id=1)
        assert "/users/login" in response.url

    def test_post_authenticated_and_moderator_delete(self):
        moder_group = Group.objects.get(name="moderator")
        moderator = mixer.blend(
            "userapp.User", is_staff=True, is_active=True, username="Moderator"
        )
        moder_group.user_set.add(moderator)

        post_ids = (v for v in [10, 11, 12, 13, 14])
        posts = mixer.cycle(5).blend("mainapp.Post", active=True, id=post_ids)

        assert Post.objects.count() == 6

        for pst_id in range(10, 15):
            path = reverse_lazy("mainapp:post_delete", kwargs={"post_id": pst_id})
            request = self.factory.get(path)
            request.user = moderator
            response = post_delete(request, post_id=pst_id)
            assert response.url == "/"

        assert Post.objects.count() == 1

    def test_post_authenticated_and_admin_delete(self):
        admin = mixer.blend(
            "userapp.User",
            is_staff=True,
            is_active=True,
            is_superuser=True,
            username="Admin",
        )

        post_ids = (v for v in [10, 11, 12, 13, 14])
        posts = mixer.cycle(5).blend("mainapp.Post", active=True, id=post_ids)

        assert Post.objects.count() == 6

        for pst_id in range(10, 15):
            path = reverse("mainapp:post_delete", kwargs={"post_id": pst_id})
            request = self.factory.get(path)
            request.user = admin
            response = post_delete(request, post_id=pst_id)
            assert response.url == "/"

        assert Post.objects.count() == 1
