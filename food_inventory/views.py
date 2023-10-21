from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from food_inventory.forms import AddIngredientForm
from food_inventory.models import Ingredient, Recipe


def home_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if "ingredients" in request.POST:
            return redirect("ingredients")
        elif "Shopping List" in request.POST:
            return redirect("shopping_list")
        elif "Recipes" in request.POST:
            return redirect("recipes")
        else:
            return render(request, 'food/index.html')
    else:
        return render(request, 'food/index.html')


def ingredients_view(request: HttpRequest):
    if request.method == "POST":
        form = AddIngredientForm(request.POST)
        Ingredient.objects.create(
            name=form.data["name"],
            calories=form.data["calories"],
            fat=form.data["fat"],
            carbohydrates=form.data["carbohydrates"],
            protein=form.data["protein"],
            quantity=form.data["quantity"],
            )
        return redirect("ingredients")
    else:
        form = AddIngredientForm()
        ingredients = Ingredient.objects.all()
        return render(request, 'food/ingredients.html', {'ingredients': ingredients, "form": form})


def shopping_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'food/shopping_list.html')


def recipes_view(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all()
    return render(request, 'food/recipes.html', {'recipes': recipes})


def ingredient_detail_view(request: HttpRequest, ingredient_id: str) -> HttpResponse:
    ingredient = Ingredient.objects.get(name=ingredient_id)
    return render(request, 'food/ingredient_detail.html', {'ingredient': ingredient})


def recipe_detail_view(request: HttpRequest, recipe_id: str) -> HttpResponse:
    recipe = Recipe.objects.get(name=recipe_id)
    return render(request, 'food/recipe_detail.html', {'recipe': recipe})
