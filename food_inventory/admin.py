from django.contrib import admin

from food_inventory.models import Ingredient, Recipe

admin.site.register(Ingredient)
admin.site.register(Recipe)
