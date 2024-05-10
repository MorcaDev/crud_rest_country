from django.core.exceptions import FieldError
from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:

        model = Country
        fields = ('id','name','description','code')


