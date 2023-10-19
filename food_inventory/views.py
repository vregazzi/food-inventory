from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from food_inventory.forms import ProductIdForm


def home_view(request: HttpRequest):
    if request.method == 'POST':
        if "Inventory" in request.POST:
            return redirect("inventory")
        elif "Shopping List" in request.POST:
            return redirect("shopping_list")
    else:
        return render(request, 'food/index.html')


def inventory_view(request: HttpRequest):
    return render(request, 'food/inventory.html')


def shopping_list_view(request: HttpRequest):
    return render(request, 'food/shopping_list.html')
