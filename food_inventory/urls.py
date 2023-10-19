"""
URL configuration for food_inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from food_inventory.views import home_view, inventory_view, shopping_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # type: ignore
    path('inventory/', inventory_view, name='inventory'),
    path('shopping_list/', shopping_list_view, name='shopping_list'),
]
