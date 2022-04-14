from django.contrib import admin
from django.db import router
from django.urls import path ,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

r=routers.DefaultRouter()
r.register('',views.ProductList)

urlpatterns = [
    
    path('', views.homeFunc , name="home"),
    path('about-us', views.aboutUsFunc , name="about-us"),
    path('contact-us', views.contactUsFunc , name="contact-us"),
    path('privacy-policy', views.privacyPolicyFunc , name="privacy-policy"),
    path('product-api/' ,views.Product_list.as_view(), name="amazon-api"),
    path('productapi/', include(r.urls)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)