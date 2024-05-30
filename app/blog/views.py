from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
)

from .forms import PostFormCreation, PostFormUpdation

# from forms import PostFormCreation
from .models import Category, Post

class PostViewList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        categories = []
        category = request.GET.get("category")
        
        if category:
            posts = Post.objects.filter(category_id=category)
        else:
            posts = Post.objects.all

        categories = Category.objects.all
        # return render (request, 'blog/blog.html', t'post_list': posts})
        return render(request, 'blog_list.html', { 'segment': 'blog', 'posts': posts, 'categories': categories, })


class PostViewCreation(LoginRequiredMixin, View):

    SAVE_AS_DRAFT = "SAVE_AS_DRAFT"
    PUBLISH = "PUBLISH"

    template_name = 'blog_create.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context["form"] = PostFormCreation()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form_creation = PostFormCreation(request.POST, request.FILES)
        post_status = request.POST["status"]
        if form_creation.is_valid():
            post = form_creation.save(commit=False)
            post.user = request.user
            post.save()
            form_creation.save_m2m()

            messages.success(self.request, f"Пост удачно опубликован.")
            return redirect(to="blog_detail", slug=post.slug)

        self.context["form"] = form_creation
        # messages.error(request, "Пожалуйста, заполните все неоходимые поля")
        return render(request, self.template_name, self.context)

class PostViewUpdation(LoginRequiredMixin, View):

    SAVE_AS_DRAFT = "SAVE_AS_DRAFT"
    PUBLISH = "PUBLISH"

    template_name = 'blog_update.html'
    context_object = {}

    def get(self, request, *args, **kwargs):

        old_post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        post_update_form = PostFormUpdation(instance=old_post,)

        self.context_object["form"] = post_update_form
        self.context_object["post"] = old_post
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        old_post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        post_update_form = PostFormCreation(request.POST, request.FILES, instance=old_post)

        action = request.POST.get("action")
        post_status = request.POST["status"]

        if post_update_form.is_valid():

            post = post_update_form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.date_updated = timezone.now()
            post.save()
            post_update_form.save_m2m()

            messages.success(self.request, f"Пост обновлен удачно.")
            return redirect(to="blog:blog_detail", slug=post.slug)

        self.context_object["post"] = post_update_form
        # messages.error(request, "Пожалуйста, заполните все необходимые поля")
        return render(request, self.template_name, self.context_object)

class PostViewDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['related_posts'] = Post.objects.filter(category=self.object.category, status=Post.PUBLISHED).order_by('?')[:3]
        kwargs['post'] = self.object
        return super().get_context_data(**kwargs)