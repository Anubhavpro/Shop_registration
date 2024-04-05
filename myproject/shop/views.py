from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from .utils import calculate_distance
from rest_framework.exceptions import ParseError

class ShopSearchView(APIView):
    def get(self, request):
        user_latitude = request.query_params.get('latitude')
        user_longitude = request.query_params.get('longitude')

        if user_latitude is None or user_longitude is None:
            raise ParseError("Latitude and longitude parameters are required.")

        try:
            user_latitude = float(user_latitude)
            user_longitude = float(user_longitude)
        except ValueError:
            raise ParseError("Invalid latitude or longitude provided.")

        shops = Shop.objects.all()
        sorted_shops = sorted(shops, key=lambda shop: calculate_distance(user_latitude, user_longitude, shop.latitude, shop.longitude))
        
        serializer = ShopSerializer(sorted_shops, many=True)
        return Response(serializer.data)
