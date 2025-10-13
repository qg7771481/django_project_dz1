from decimal import Decimal

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL-слаг")
    description = models.TextField(blank=True, verbose_name="Опис")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category_detail', args=[self.slug])


class Product(models.Model):
    """Модель товару."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.DecimalField(default=Decimal(0.0), max_digits=2, decimal_places=1)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name="Категорія"
    )

    def get_absolute_url(self) -> str:
        """
        Функція повертає абсолютну адресу URL для об'єкта товару.
        Приклад http://127.0.0.1:8000/products/3/samsung/
        """
        return reverse(
            "products:product_detail",
            kwargs={"product_pk": self.pk, "product_slug": self.slug},
        )
