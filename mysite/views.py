from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')

def productlist(request):
    plist = [1,2,3,4,5]
    return render(request, 'mysite/productlist.html', {'plist':plist})

def productdetail(request, product_id):
    return render(request, 'mysite/productdetail.html', {'id':product_id})