from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from stock.models import Stock
from stock.serializers import StockSerializer


class StockListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
