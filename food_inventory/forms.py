from django import forms


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


class IncrementIngredientButton(forms.Form):
    # two buttons for increasing and decreasing quantity of ingredient object
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'size': 20,
                'autofocus': True,
                }
            )
        )
    submit = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'submit',
                'value': '+',
                }
            )
        )


class DecrementIngredientButton(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'size': 20,
                'autofocus': True,
                }
            )
        )
    submit = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'submit',
                'value': '-',
                }
            )
        )
