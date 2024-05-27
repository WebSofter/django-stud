from ast import dump
import json
import pprint
from .models import Profile, Role
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django. contrib.auth.admin import User
from django.views import View

from .forms import UserFormUpdation, ProfileFormUpdation
# Create your views here.

def UserViewList(request):
  '''вывод записей'''
  #
#   if request.method == 'POST':
#     form = PostForm(request.POST)
#     form.save()
#     return redirect('/blog/')
#     # if form.is_valid():
#     #   form.save()
#     #   return redirect('/blog/')
#     # else:
#     #   print("Не заполнены нужные поля")
#   else:
#     form = PostForm()
  #
  profiles = Profile.objects.all()
  # return render (request, 'blog/blog.html', t'post_list': posts})
  return render(request, 'user_list.html', { 'segment': 'user', 'profiles': profiles, })

class UserViewDetail(LoginRequiredMixin, View):
    template_name = 'user_detail.html'
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id") if self.kwargs.get("id") else request.user.id
        print(id)
        roles = Role.objects.all
        #
        user = get_object_or_404(User, id = id)
        profile = get_object_or_404(Profile, user_id=id)
        #
        profileForm = ProfileFormUpdation(instance = profile,)
        userForm = UserFormUpdation(instance = user,)
        # pprint.pprint(vars(profile))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})

class UserViewUpdation(LoginRequiredMixin, View):
    template_name = 'user_update.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id") if self.kwargs.get("id") else request.user.id
        roles = Role.objects.all
        #
        user = get_object_or_404(User, id = id)
        profile = get_object_or_404(Profile, user_id=id)
        #
        profileForm = ProfileFormUpdation(instance = profile,)
        userForm = UserFormUpdation(instance = user,)
        # pprint.pprint(vars(profile))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})
    
    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("id") if self.kwargs.get("id") else request.user.id
        #
        old_user = get_object_or_404(User, id = id)
        old_profile = get_object_or_404(Profile, user_id=id)
        profileForm = ProfileFormUpdation(request.POST, request.FILES, instance=old_profile)
        userForm = UserFormUpdation(request.POST, instance = old_user,)
        if profileForm.is_valid() and userForm.is_valid():
            # pprint.pprint(vars(userForm))
            # pprint.pprint(vars(profileForm))
            user = userForm.save(commit=False)
            user.save()
            userForm.save_m2m()
            #
            profile = profileForm.save(commit=False)
            profile.save()
            profileForm.save_m2m()
            return redirect(to="user_detail", id=user.id)
        
        user = get_object_or_404(User, id = self.kwargs.get("id"))
        profile = get_object_or_404(Profile, user = self.kwargs.get("id"))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})

class UserViewCreation(LoginRequiredMixin, View):
    template_name = 'user_create.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id") if self.kwargs.get("id") else request.user.id
        roles = Role.objects.all
        #
        user = get_object_or_404(User, id = id)
        profile = get_object_or_404(Profile, user_id=id)
        #
        profileForm = ProfileFormUpdation(instance = profile,)
        userForm = UserFormUpdation(instance = user,)
        # pprint.pprint(vars(profile))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})