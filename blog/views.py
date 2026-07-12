from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"

    # def get_queryset(self):
    #     queryset = super().get_queryset().filter(is_publication=True)
    #     return queryset


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:home")
    permission_required = "blog.delete_blog"


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = [
        "title",
        "description",
        "preview",
        "is_publication",
        "counter_view",
    ]
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:home")
    permission_required = "blog.add_blog"


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = [
        "title",
        "description",
        "preview",
        "is_publication",
        "counter_view",
    ]
    template_name = "blog/blog_form.html"
    permission_required = "blog.change_blog"

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"
    permission_required = "blog.view_blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.counter_view = F("counter_view") + 1
        obj.save(update_fields=["counter_view"])
        return obj
