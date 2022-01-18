from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError


from PIL import Image


class HotDrinksAdminForm(ModelForm):

    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображение с разрешением не менее {}x{}'.format(
            *self.MIN_RESOLUTION
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное разрешение изображения меньше минимального допустимого')


class HotDrinksAdmin(admin.ModelAdmin):

    form = HotDrinksAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='hotDrinks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ColdDrinksAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='coldDrinks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DessertAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='dessert'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(HotDrinks, HotDrinksAdmin)
admin.site.register(ColdDrinks, ColdDrinksAdmin)
admin.site.register(Desserts, DessertAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
