from mixer.backend.django import mixer
from userapp.models import User
from mainapp.models import Post


def test_user_avatar_is_default(db):
    user = mixer.blend("userapp.User", username="usermuser")
    assert user.avatar.name == "user.png"


def test_user_is_email_not_verified(db):
    user = mixer.blend("userapp.User", username="usermuser")
    assert user.is_email_verified == False


def test_10_users_create(db):
    user = mixer.cycle(10).blend("userapp.User")
    assert User.objects.count() == 10


def test_10_post_create(db):
    post = mixer.cycle(10).blend("mainapp.Post")
    assert Post.objects.count() == 10
