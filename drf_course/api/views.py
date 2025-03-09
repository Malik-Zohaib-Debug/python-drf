from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Product
from api.serializers import ProductSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serialized_product = ProductSerializer(products, many=True)
    return Response(serialized_product.data)


@api_view(['GET'])
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serialized_product = ProductSerializer(product)
    return Response(serialized_product.data)