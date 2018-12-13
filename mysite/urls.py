from django.urls import path

from . import views

app_name  ='mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('productlist', views.productlist, name='productlist'),
    path('productdetail/<int:product_id>', views.productdetail, name='productdetail'),
]