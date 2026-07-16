from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


class ProductService:
    @staticmethod
    def get_products_from_cache():
        if not CACHE_ENABLED:
            return Product.objects.all()

        return cache.get_or_set(
            "all_products_cache_key", lambda: list(Product.objects.select_related("category").all()), 60 * 2
        )
