from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = [
        "title",
        "description",
        "preview",
        "is_publication",
        "counter_view",
    ]


class BlogListView(ListView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = [
        "title",
        "description",
        "preview",
        "is_publication",
        "counter_view",
    ]


class BlogDeleteView(DeleteView):
    model = Blog
