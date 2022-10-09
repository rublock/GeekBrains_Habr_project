from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from userapp.forms import UserCreate


class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreate()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreate(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
