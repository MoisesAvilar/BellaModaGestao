from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from product.serializers import ProductSerializer
from product.models import Product


class ProductListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
