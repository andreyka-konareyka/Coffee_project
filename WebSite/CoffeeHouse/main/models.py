from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

#***************
# Category / категория
# Product / продукт
# CartProduct / корзина продуктов
# Cart / корзина
# Order / заказ
#**********
#Customer / пользователь


User = get_user_model()


class LatestProductManager:

    @staticmethod
    def get_product_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        product = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_product = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            product.extend(model_product)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(product, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to),
                                  reverse=True)
        return product


class LatestProducts:

    objects = LatestProductManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class HotDrinks(Product):

    volume = models.CharField(max_length=255, verbose_name='Объем')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class ColdDrinks(Product):

    volume = models.CharField(max_length=255, verbose_name='Объем')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class Desserts(Product):
    weight = models.CharField(max_length=255, verbose_name='Вес')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='корзина', on_delete=models.CASCADE, related_name='related_product')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #тут будет модель продукта
    object_id = models.PositiveIntegerField() #тут будет кол-во
    content_object = GenericForeignKey('content_type', 'object_id')
    count = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return 'Продукт: {} (для корзины)'.format(self.product.title)


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_product = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
