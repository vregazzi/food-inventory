from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from food_inventory.forms import (AddIngredientForm, AddRecipeForm,
                                  EditIngredientForm, MakeShoppingListForm)
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
    if request.method == "POST":
        form = MakeShoppingListForm(request.POST)
        new_form = MakeShoppingListForm()
        recipe_obj = Recipe.objects.get(name=form.data["recipe"])
        needed_ingredients = dict(recipe_obj.ingredients)
        shopping_list: dict[str, int] = {}

        for ingredient in needed_ingredients:
            needed_quantity = needed_ingredients[ingredient] * int(form.data["quantity"])
            current_quantity = Ingredient.objects.get(name=ingredient).quantity
            if needed_quantity > current_quantity:
                shopping_list[ingredient] = needed_quantity - current_quantity

        if len(shopping_list) == 0:
            shopping_list["No ingredients needed!"] = 0

        return render(request, 'food/shopping_list.html', {'shopping_list': shopping_list, "form": new_form})
    else:
        form = MakeShoppingListForm()
    return render(request, 'food/shopping_list.html', {"form": form})


def recipes_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        Recipe.objects.create(
            name=form.data["name"],
            ingredients=form.data["ingredients"],
            servings=form.data["servings"],
            )
        return redirect("recipes")
    else:
        form = AddRecipeForm()
        recipes = Recipe.objects.all()
        return render(request, 'food/recipes.html', {'recipes': recipes, "form": form})


def ingredient_detail_view(request: HttpRequest, ingredient_id: str) -> HttpResponse:
    ingredient = Ingredient.objects.get(name=ingredient_id)
    if request.method == "POST":
        if "delete" in request.POST:
            ingredient.delete()
            return redirect("ingredients")
        elif "increment" in request.POST:
            ingredient.quantity += 1
            ingredient.save()
            return redirect("ingredient_detail", ingredient_id=ingredient_id)
        elif "decrement" in request.POST:
            ingredient.quantity -= 1
            ingredient.save()
            return redirect("ingredient_detail", ingredient_id=ingredient_id)
        else:
            form = EditIngredientForm(request.POST)
            ingredient.calories = form.data["calories"]
            ingredient.fat = form.data["fat"]
            ingredient.carbohydrates = form.data["carbohydrates"]
            ingredient.protein = form.data["protein"]
            ingredient.save()
            return redirect("ingredient_detail", ingredient_id=ingredient_id)
    else:
        form = EditIngredientForm()
        return render(request, 'food/ingredient_detail.html', {'ingredient': ingredient, "form": form})


def recipe_detail_view(request: HttpRequest, recipe_id: str) -> HttpResponse:
    recipe = Recipe.objects.get(name=recipe_id)
    if request.method == "POST":
        if "delete" in request.POST:
            recipe.delete()
            return redirect("recipes")
        elif "increment" in request.POST:
            recipe.servings += 1
            recipe.save()
        elif "decrement" in request.POST:
            recipe.servings -= 1
            recipe.save()
        return redirect("recipe_detail", recipe_id=recipe_id)
    else:
        return render(request, 'food/recipe_detail.html', {'recipe': recipe})
