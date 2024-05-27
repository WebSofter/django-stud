from ast import dump
import json
import pprint
from .models import Profile
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
  users = User.objects.all
  # return render (request, 'blog/blog.html', t'post_list': posts})
  return render(request, 'user_list.html', { 'segment': 'user', 'users': users, })

class UserViewDetail(LoginRequiredMixin, View):

    template_name = 'user_detail.html'
    context = {}

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user = self.kwargs.get("id"))
        user = get_object_or_404(User, id = self.kwargs.get("id"))
        #
        profileForm = ProfileFormUpdation(instance = user,)
        userForm = UserFormUpdation(instance = user,)
        pprint.pprint(vars(profile))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})
    
    def post(self, request, *args, **kwargs):
        old_profile = get_object_or_404(Profile, user = self.kwargs.get("id"))
        old_user = get_object_or_404(User, id = self.kwargs.get("id"))
        profileForm = ProfileFormUpdation(request.POST, request.FILES, instance=old_user)
        userForm = UserFormUpdation(request.POST, instance = old_user,)
        if profileForm.is_valid() and userForm.is_valid():
            pprint.pprint(vars(userForm))
            pprint.pprint(vars(profileForm))
            user = userForm.save(commit=False)
            user.save()
            # user.save_m2m()
            #
            profile = profileForm.save(commit=False)
            profile.save()
            profileForm.save_m2m()
            return redirect(to="user_detail", id=profile.id)
        
        user = get_object_or_404(User, id = self.kwargs.get("id"))
        profile = get_object_or_404(Profile, user = self.kwargs.get("id"))
        return render(request, self.template_name, {'user': user, 'profile': profile, 'profileForm': profileForm, 'userForm': userForm})
