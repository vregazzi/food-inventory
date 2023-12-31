from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    quantity = models.IntegerField()

    def get_nutrition(self) -> dict[str, int]:
        return {
            'calories': self.calories,
            'protein': self.protein,
            'fat': self.fat,
            'carbohydrates': self.carbohydrates
        }


class Recipe(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    ingredients = models.JSONField()
    servings = models.IntegerField(default=0)

    def get_nutrition(self) -> dict[str, int]:
        nutrition = {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbohydrates': 0,
            }
        for ingredient in self.ingredients:
            obj = Ingredient.objects.get(name=ingredient)
            nutrition['calories'] += obj.calories
            nutrition['protein'] += obj.protein
            nutrition['fat'] += obj.fat
            nutrition['carbohydrates'] += obj.carbohydrates
        return nutrition
