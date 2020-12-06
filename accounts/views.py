from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView,CreateView, DetailView
from accounts.forms import UserCreateForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from accounts import models

# Create your views here.


class HomePage(TemplateView):
    template_name='index.html'


class SignUp(CreateView):
    form_class=UserCreateForm
    template_name='accounts/signup.html'
    success_url='/accounts/login'
    
class CreateProfile(LoginRequiredMixin,CreateView):
    model = Profile
    fields = ('contact','gender','profile_pic')
    template_name = 'Profile/profile_form.html'

    def form_valid(self, form):
        if Profile.objects.filter(user = self.request.user).exists():
            return redirect('accounts:profile', username=self.request.user.username,pk=Profile.objects.filter(user = self.request.user)[0].pk)
        profile = form.save(commit=False)
        profile.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        username = self.kwargs.get('username')
        pk = self.object.pk
        return reverse_lazy('accounts:homepage', kwargs={'username':username,'pk':pk})

class DetailProfile(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'Profile/profile_detail.html'
    
    def VerifyProfile(self,request, username):
         try:
            profile = Profile.objects.get(user__username=username)
         except:
            return redirect('accounts:CreateProfile',username=username)
         return redirect('accounts:profile' ,username=username#,pk=profile.pk)

