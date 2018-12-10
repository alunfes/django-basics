from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productlist/<int:product_id>', views.productlist, name='productlist'),
]