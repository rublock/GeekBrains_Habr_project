from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.conf import settings
from .models import User
from .utils import generate_token
from userapp.forms import MyUserRegisterForm
from django.contrib import auth
from userapp.forms import MyUserLoginForm
from django.urls import reverse


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = "Активируйте свой профиль"

    email_body = render_to_string(
        "registration/activate.html",
        {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user.email],
    )

    email.send()


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Электронный адрес пользователя проверен, теперь можете войти в свою учетную запись.",
        )

        return redirect("users:login")
    return render(request, "registration/activate-failed.html", {"user": user})



def login(request):
    login_form = MyUserLoginForm(data=request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return redirect("/")
    content = {"login_form": login_form}
    return render(request, "userapp/login.html", content)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    if request.method == "POST":
        register_form = MyUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            # Mail activation
            send_activation_email(user, request)
            if not user.is_email_verified:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ваш e-mail не верифицирован, пожалуйста проверьте входящее сообщение для активации пользователя на портале. Если вы не получили сообщение, проверьте папку "Спам".',
                )
                content = {"register_form": register_form}
                return render(request, "userapp/register.html", content)
            return HttpResponseRedirect(reverse("users:login"))
    else:
        register_form = MyUserRegisterForm()
    content = {"register_form": register_form}

    return render(request, "userapp/register.html", content)