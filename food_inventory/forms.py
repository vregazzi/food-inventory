from django import forms

from food_inventory.models import Recipe


class EditIngredientForm(forms.Form):
    calories = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    fat = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    carbohydrates = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    protein = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )


class AddIngredientForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'size': 20,
                'autofocus': True,
                }
            )
        )
    calories = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    fat = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    carbohydrates = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    protein = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )


class AddRecipeForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'size': 20,
                'autofocus': True,
                }
            )
        )
    ingredients = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'size': 20,
                'autofocus': True,
                }
            )
        )
    servings = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )


class MakeShoppingListForm(forms.Form):
    names = Recipe.objects.values_list('name', flat=True)
    recipe = forms.ChoiceField(choices=[(name, name) for name in names])
    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'size': 50}
            )
        )
