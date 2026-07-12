from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ("published", "Опубликован"),
        ("unpublished", "Не опубликован"),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите продукт",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание",
    )
    image = models.ImageField(
        upload_to="products/photo",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Вставьте изображение",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        help_text="Введите категорию",
        related_name="products",
    )
    price = models.FloatField(
        verbose_name="Цена за покупку",
        blank=True,
        null=True,
        help_text="Введите цену за покупку",
    )
    status = models.CharField(
        max_length=20, verbose_name="Статус публикации", choices=STATUS_CHOICES, default="unpublished"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        blank=True,
        null=True,
        help_text="Введите дату создания",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="дата последнего изменения",
        blank=True,
        null=True,
        help_text="Введите дату последнего изменения",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        blank=True,
        null=True,
        help_text="Введите категорию",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]
