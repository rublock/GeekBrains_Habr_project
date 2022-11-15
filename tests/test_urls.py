from django.urls import reverse, resolve


class TestUrls:
    def test_post_detail_url(self):
        path = reverse("mainapp:post_detail", kwargs={"post_id": 1})
        assert resolve(path).view_name == "mainapp:post_detail"

    def test_author_posts_url(self):
        path = reverse("mainapp:author-posts", kwargs={"author_id": 1})
        assert resolve(path).view_name == "mainapp:author-posts"

    def test_post_delete_url(self):
        path = reverse("mainapp:post_delete", kwargs={"post_id": 1})
        assert resolve(path).view_name == "mainapp:post_delete"
