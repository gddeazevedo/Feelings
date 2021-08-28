from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from .forms import UserSignUpForm


def sign_up(request: HttpRequest):
    if request.user.is_authenticated:
        redirect(to='blogs:root_path')

    if request.method == 'GET':
        form = UserSignUpForm()
    elif request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_user = authenticate(
                username=user.username,
                password=request.POST['password1']
            )
            login(request, auth_user)
            return HttpResponseRedirect(reverse('blog:root_path'))

    return render(request, 'users/sign-up.html', {'form': form})


def logout(request: HttpRequest):
    pass
