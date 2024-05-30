from ast import dump
import json
import pprint
from .models import Profile, Role
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django. contrib.auth.admin import User
from django.views import View

from .forms import RoleFormBase, UserFormUpdation, ProfileFormUpdation
# Create your views here.

def UserViewList(request):
  '''вывод записей'''
  profiles = Profile.objects.all()
  admins = Profile.objects.filter(user__is_superuser=1)
  staffs = Profile.objects.filter(role=None)
  roles = Role.objects.all()
  return render(request, 'user_list.html', { 'segment': 'user', 'profiles': profiles, 'admins': admins, 'statffs': staffs, 'roles': roles})

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
    
class RoleViewCreation(LoginRequiredMixin, View):
    template_name = 'role_create.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id = request.user.id)
        role = get_object_or_404(Role, id = self.kwargs.get("id"))
        #
        form = RoleFormBase(instance = role,)
        # pprint.pprint(vars(profile))
        return render(request, self.template_name, { 'user': user, 'form': form, })
    
    def post(self, request, *args, **kwargs):
        form = RoleFormBase(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            form.save_m2m()
            return redirect(to="profile",)
        return render(request, self.template_name, {'form': form})
    
class RoleViewUpdation(LoginRequiredMixin, View):
    template_name = 'role_update.html'
    def get(self, request, *args, **kwargs):
        role = get_object_or_404(Role, id=self.kwargs.get("id"))
        form = RoleFormBase(instance=role,)
        return render(request, self.template_name, {'form': form, 'role': role})

    def post(self, request, *args, **kwargs):
        role = get_object_or_404(Role, id=self.kwargs.get("id"))
        form = RoleFormBase(request.POST, request.FILES, instance=role)
        if form.is_valid():
            role = form.save(commit=False)
            role.save()
            form.save_m2m()
            return redirect(to="role:role_update", id=role.id)

        return render(request, self.template_name, {'form': form})