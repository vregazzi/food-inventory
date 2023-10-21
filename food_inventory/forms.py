from django import forms


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
