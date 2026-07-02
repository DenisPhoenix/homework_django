from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "create_at",
        "is_publication",
        "counter_view",
    )
    list_filter = ("title",)
    search_fields = ("title",)
