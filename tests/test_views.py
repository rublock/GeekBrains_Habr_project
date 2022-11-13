
import django.http
import pytest
from django.contrib import auth
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mainapp.models import Post
from userapp.models import User
from mainapp.views import post_delete, post_detail, post_edit, post_new
from mixer.backend.django import mixer

# region TO_DEL
import time
from icecream import ic
# endregion


@pytest.mark.django_db
class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend("mainapp.Post", id=1)
        cls.factory = RequestFactory()

    def test_new_post_for_authenticated(self):
        strong_password = "Str#410-P@55"
        user = User.objects.create_user(username='asdf', email='asdf@example.com', password=strong_password)
        self.client.login(username=user.username, password=strong_password)
        path = reverse("mainapp:post-new")
        request = self.client.get(path)
        request.user = user
        
        if isinstance(httpresp:=request.json.args[0], HttpResponse):
            status_code = httpresp.status_code
        
        assert status_code == 200

    def test_new_post_for_unauthenticated(self):
        path = reverse("mainapp:post-new")
        request = self.client.get(path)
        request.user = AnonymousUser()
        
        if isinstance(httpresp:=request.json.args[0], HttpResponse):
            status_code = httpresp.status_code
        assert status_code == 302        


    def test_post_detail_authenticated(self):
        
        path = reverse("mainapp:post_detail", kwargs={"post_id": 1})
        request = self.factory.get(path)
        ic(path)
        ic(request)
        request.user = Post.objects.get(id=1).user
        ic(Post.objects.get(id=1).user)
        response = post_detail(request, post_id=1)
        # assert response.status_code == 200

    # def test_post_detail_unauthenticated(self):
    #     path = reverse("mainapp:post_detail", kwargs={"post_id": 1})
    #     request = self.factory.get(path)
    #     request.user = AnonymousUser()
    #     response = post_detail(request, post_id=1)
    #     assert response.status_code == 200

    # def test_new_post_unauthenticated_create(self):
    #     path = reverse("mainapp:post-new")
    #     request = self.factory.get(path)
    #     request.user = AnonymousUser()
    #     response = post_new(request)
    #     assert "/users/login" in response.url

    # def test_post_unauthenticated_edit(self):
    #     path = reverse("mainapp:post-edit", kwargs={"post_id": 1})
    #     request = self.factory.get(path)
    #     request.user = AnonymousUser()
    #     response = post_edit(request, post_id=1)
    #     assert "/users/login" in response.url

    # def test_post_unauthenticated_delete(self):
    #     path = reverse("mainapp:post_delete", kwargs={"post_id": 1})
    #     request = self.factory.get(path)
    #     request.user = AnonymousUser()
    #     response = post_delete(request, post_id=1)
    #     assert "/users/login" in response.url

    