from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_publication=True)
        return queryset


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:home")


class BlogCreateView(CreateView):
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


class BlogUpdateView(UpdateView):
    model = Blog
    fields = [
        "title",
        "description",
        "preview",
        "is_publication",
        "counter_view",
    ]
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse("blog:blog_detail", kwargs={"pk": self.object.pk})


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.counter_view = F("counter_view") + 1
        obj.save(update_fields=["counter_view"])
        return obj
