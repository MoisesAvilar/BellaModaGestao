from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sale.models import Sale
from sale.serializers import SaleSerializer


class SaleListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
