from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import generic
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UpdateProfileForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponseRedirect
from django.urls import reverse


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            phone = form.cleaned_data['phone']
            user = form.save()
            Profile.objects.create(user=user, phone=phone)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    pass


class UserLogoutView(LogoutView):
    pass


class UserProfileView(generic.View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/account.html', context={})


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    def get(self, request, *args, **kwargs):
        form = UpdateProfileForm(initial={'phone': request.user.profile.phone,
                                          'username': request.user.username,
                                          'first_name': request.user.first_name,
                                          'last_name': request.user.last_name,
                                          'email': request.user.email})
        return render(request, 'users/profile.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        profile = request.user.profile
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            user = request.user
            profile = form.save(commit=False)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('account'))
        return render(request, 'users/profile.html', context={'form': form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'users/change-password.html'


class ChangePasswordViewDone(PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'


class HistoryOrderList(generic.ListView, LoginRequiredMixin):
    template_name = 'users/historyorder.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user = self.request.user
        queryset = user.orders.all()
        return queryset


class HistoryDetailOrder(generic.DetailView, LoginRequiredMixin):
    template_name = 'users/oneorder.html'
    context_object_name = 'order'

    def get_queryset(self):
        return self.request.user.orders.all()

