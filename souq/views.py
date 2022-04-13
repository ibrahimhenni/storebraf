from sys import api_version
from urllib import response
from django.shortcuts import render ,redirect
from . models import *
from serializer import ApiAmazon
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets 
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def homeFunc(request):
    
    # products = Product.objects.all()
    
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    products = Product.objects.filter(Q(title__icontains=q))
    paginator = Paginator(products ,9)
    page = request.GET.get('page')
    products= paginator.get_page(page)
    
    context={
        'products':products,
    }
    return render (request ,"souq/index.html", context)

def privacyPolicyFunc(request):
    mypolicy=Storbraf.objects.all()
    return render(request,"souq/privacy-policy.html",{"mypolicy":mypolicy})


def aboutUsFunc(request):
    myabout=Storbraf.objects.all()
    return render(request,"souq/about-us.html",{"myabout":myabout})

def contactUsFunc (request):
    if request.method=='POST':
       contact=Contact() 
       name=request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       contact.name=name
       contact.email=email
       contact.subject=subject
       contact.save()
       return redirect("home")
    return render(request,"souq/contact.html")

#method 1
class Product_list(APIView):
    def get(self,request):
        products = Product.objects.all()
        api_products = ApiAmazon(products, many=True)
        return Response(api_products.data)
    
#method 2
class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ApiAmazon
    
#
# def get_data(request):
#     url_jsonFile=" webscriping/amazon_data.json"
#     api_data=requests.get(url_jsonFile).json()
#     return render(request,"souq/index.html",{'pi_data':api_data,})

