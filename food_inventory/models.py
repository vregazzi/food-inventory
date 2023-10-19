from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    calories = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carbohydrates = models.IntegerField()
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
    # field for ingredients and quantity
    ingredients = models.JSONField()
    # ingredients = dict[str, int]

    def get_nutrition(self) -> dict[str, int]:
        nutrition = {
            'calories': 0,
            'protein': 0,
            'fat': 0,
            'carbohydrates': 0
        }
        return nutrition
