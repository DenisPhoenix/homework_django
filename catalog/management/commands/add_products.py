from django.core.management.base import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление тестовых продуктов в базу данных"

    def handle(self, *args, **kwargs):
        # Удаление всех записей с таблиц
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Сброс счетчика id
        with connection.cursor() as cursor:
            cursor.execute("""
                ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;
                ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;
            """)

        # Добавление категории в БД
        category, _ = Category.objects.get_or_create(name="Овощи")

        # Список с продуктами
        products = [
            {"name": "Помидоры", "price": "25", "category": category},
            {"name": "Огурцы", "price": "30", "category": category},
            {"name": "Марковка", "price": "28", "category": category},
            {"name": "Лук", "price": "15", "category": category},
        ]

        # Добавление продуктов в БД
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added product: {product.name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Product already exists: {product.name}"
                    )
                )
