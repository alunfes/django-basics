from django.urls import path

from . import views

app_name  ='mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('productlist/<int:product_id>', views.productlist, name='productlist'),
]