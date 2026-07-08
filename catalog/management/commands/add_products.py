from django.core.management import call_command
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

            call_command("loaddata", "catalog/fixtures/category_fixture.json")
            call_command("loaddata", "catalog/fixtures/product_fixture.json")
            self.stdout.write(self.style.SUCCESS("Фикстура загружена в базу данных"))
