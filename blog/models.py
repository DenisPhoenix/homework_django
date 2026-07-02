from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    description = models.TextField(
        verbose_name="Содержимое", help_text="Введите содержимое"
    )
    preview = models.ImageField(
        upload_to="blogs/",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Вставьте изображение",
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    is_publication = models.BooleanField(
        default=False,
        verbose_name="Признак публикации",
        help_text="Укажите признак публикации",
    )
    counter_view = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
        help_text="Введите количество просмотров",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
