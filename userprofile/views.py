from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.models import User
from authentication.models import UserProfile
from .forms import UserForm, UserProfileForm


class ProfileView(LoginRequiredMixin, View):
    template_name = 'userprofile/userprofile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })
