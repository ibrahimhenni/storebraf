from  souq.models import *
from rest_framework import serializers

class ApiAmazon(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = "__all__"
