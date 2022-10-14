from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.views import View
from django.shortcuts import render, redirect
from django.conf import settings
from .models import User
from .utils import generate_token
from .forms import UserCreateForm



def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Активируйте свой профиль'

    email_body = render_to_string('registration/activate.html', {
      'user'  : user,
      'domain': current_site,
      'uid':urlsafe_base64_encode(force_bytes(user.pk)),
      'token': generate_token.make_token(user),
    })

    email = EmailMessage(subject=email_subject,
                         body=email_body,
                         from_email=settings.EMAIL_FROM_USER,
                         to=[user.email])

    email.send()


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified=True
        user.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             'Электронный адрес пользователя проверен, теперь можете войти в свою учетную запись.')

        return redirect('login')
    return render(request, 'registration/activate-failed.html', {'user':user})

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreateForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save()
            send_activation_email(user, request)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            if not user.is_email_verified:
                messages.add_message(request, messages.ERROR,
                             'ваш e-mail не верифицирован, пожалуйста проверьте входящее сообщение для активации пользователя на портале.')
                return render(request, self.template_name)

            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
