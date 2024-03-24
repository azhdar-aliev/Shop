from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CHOICES = [
        (1, 'XS'),
        (2, 'S'),
        (3, 'M'),
        (4, 'L'),
    ]

    MANUFACTURER_CHOICES = [
        ('RU', 'Россия'),
        ('TR', 'Турция'),
        ('CN', 'Китай'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(verbose_name='Цена')        # не отрицательное целое число
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True)             # время при создании обЬекта
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изминения')                 # время после пересохранения обЬекта
    size = models.IntegerField(choices=SIZE_CHOICES)
    manufacturer = models.CharField(max_length=2, choices=MANUFACTURER_CHOICES)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
