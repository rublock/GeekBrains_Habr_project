import requests

from django.contrib.auth.decorators import login_required, user_passes_test
from bs4 import BeautifulSoup

from .models import Post, Category
from userapp.models import User


class DemoPosts:
    @classmethod
    def get_random_wikipost(cls):
        def del_link(link=None):
            link["href"] = "#"

        response = requests.get(
            "https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
        )
        bs = BeautifulSoup(response.content, "html.parser")
        edit_links = bs.find_all(
            name="span", attrs={"class": "mw-editsection"}, recursive=True
        )
        [edit_link.decompose() for edit_link in edit_links]
        content = bs.find(name="div", attrs={"id": "content"}).extract()
        all_links = content.find_all("a")
        [del_link(link) for link in all_links]
        return content.h1.text, content.decode()

    @classmethod
    def create_demo_post(cls, user: User, category=None, service=None):
        if not category:
            target_category, created = Category.objects.get_or_create(
                name="Demo", active=True
            )
        new_post_title, new_post_content = DemoPosts.get_random_wikipost()
        post = Post.objects.create(user=user, category=target_category)
        post.title = f"DEMO {new_post_title}"
        post.content = new_post_content
        post.save()
