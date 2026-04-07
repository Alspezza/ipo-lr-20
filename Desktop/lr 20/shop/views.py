from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Category, Maker, Product, Bucket, BucketElem
from .serializers import (
    CategorySerializer, 
    MakerSerializer, 
    ProductSerializer, 
    BucketSerializer, 
    BucketElemSerializer
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Вот эта строка добавит ссылку на регистрацию в список:
        'register': reverse('register', request=request, format=format),
        
        # Остальные ссылки из вашего роутера (перечислите нужные):
        'products': reverse('product-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'makers': reverse('maker-list', request=request, format=format),
        'buckets': reverse('bucket-list', request=request, format=format),
    })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # Разрешаем доступ всем, чтобы новые люди могли регистрироваться
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MakerViewSet(viewsets.ModelViewSet):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BucketViewSet(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

class BucketElemViewSet(viewsets.ModelViewSet):
    queryset = BucketElem.objects.all()
    serializer_class = BucketElemSerializer
