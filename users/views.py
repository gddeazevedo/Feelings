from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from .forms import UserSignUpForm


def sign_up(request: HttpRequest):
    if request.user.is_authenticated:
        redirect(to='blogs:root')

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
            return HttpResponseRedirect(reverse('blog:root'))

    return render(request, 'users/sign_up.html', {'form': form})


def sign_out(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('blog:root'))
