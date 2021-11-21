from django import forms
from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class HotDrinksAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(slug='hotDrinks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ColdDrinksAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(slug='coldDrinks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class DessertAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return forms.ModelChoiceField(Category.objects.filter(slug='dessert'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(HotDrinks, HotDrinksAdmin)
admin.site.register(ColdDrinks, ColdDrinksAdmin)
admin.site.register(Desserts, DessertAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
