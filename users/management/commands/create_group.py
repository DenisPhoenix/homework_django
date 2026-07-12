from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Создание группы для модераторов продуктов"

    def handle(self, *args, **kwargs):
        moderator_group = Group.objects.create(name="Модератор продуктов")

        can_unpublish_product = Permission.objects.get(codename="can_unpublish_product")
        can_delete_product = Permission.objects.get(codename="delete_product")

        moderator_group.permissions.add(can_unpublish_product, can_delete_product)

        self.stdout.write(self.style.SUCCESS("Успешное создание группы: Модератор продуктов"))
