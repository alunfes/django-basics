from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    plist = [1,2,3,4,5]
    return render(request, 'mysite/index.html', {'data':plist})

def productlist(request, product_id):
    return render(request, 'mysite/productlist.html', {'id':product_id})