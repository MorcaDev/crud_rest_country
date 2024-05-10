from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Country
from .serializers import CountrySerializer

# Create your views here.
@api_view(["GET"])
def get_all_country(request):

    try:

        # query element
        all_countries = Country.objects.all()

        # serializers
        instance_serializer = CountrySerializer(all_countries, many=True)
        readable_format = instance_serializer.data

        # send all items
        return Response(readable_format)
    
    except:

        # handling errors
        return Response({"Error":"Something wrong happen"})

@api_view(["GET"])
def get_detail_country(request,pk=None):

    try:

        # selecting object from db
        specific_instance = Country.objects.get(id=pk)

        #serializer 
        instance_serializer = CountrySerializer(specific_instance)
        readable_format = instance_serializer.data

        # send specific item
        return Response(readable_format)
    
    except ObjectDoesNotExist:

        # handling errors
        return Response({"Error":"Item not calleable"}, 404)
    
    except:

        # handling errors
        return Response({"Error":"Something wrong happen"})

@api_view(["POST"])
def post_country(request):

    try:

        # get data from request
        sent = request.data

        # create serializer instance
        instance_serializer = CountrySerializer(data=sent)

        # validations with serializer
        if not instance_serializer.is_valid():

            return Response({"Error":"Not sufficient data"}, 500)
        
        # instance for db
        instance_serializer.save()

        # return successfull message
        return Response(instance_serializer.data)
        
    except :

        # handling errors
        return Response({"Error":"Something wrong happen"})

@api_view(["PUT"])
def put_country(request):

    try:

        picked_item             = Country.objects.get(id=request.data["id"])
        picked_item.name        = request.data["name"]
        picked_item.description = request.data["description"] 
        picked_item.code        = request.data["code"]
        picked_item.save()

        readable_format         = CountrySerializer(picked_item).data

        return Response(readable_format)

    except:

        return Response({"Error":"Information don't match"}) 

@api_view(["PATCH"])
def patch_country(request,pk=None):

    try:

        picked_item             = Country.objects.get(id=pk)
        picked_item.name        = request.data.get("name", picked_item.name) 
        picked_item.description = request.data.get("description", picked_item.description)
        picked_item.code        = request.data.get("code", picked_item.code)
        picked_item.save()

        readable_format         = CountrySerializer(picked_item).data

        return Response(readable_format)

    except ObjectDoesNotExist:

        return Response({"Error":"Object doesn't exist"}) 

    except :

        return Response({"Error":"Something Wrong happen"}) 

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_country(request):

    # identify item
    items = Country.objects.all()

    # delete
    items.delete()

    return Response("Delete sucessfully")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_detail_country(request,pk=None):

    try:

        # identify item
        item = Country.objects.get(id=pk)

        # delete
        item.delete()

        return Response("Delete sucessfully")
    
    except ObjectDoesNotExist:

        return Response({"Error":"Object doesn't exist"},404)