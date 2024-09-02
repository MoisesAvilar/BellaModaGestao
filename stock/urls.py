from django.urls import path
from stock.views import StockListView, StockRetrieveUpdateDestroy


urlpatterns = [
    path('stock/', StockListView.as_view(), name='stock_list_view'),
    path('stock/<int:pk>/', StockRetrieveUpdateDestroy.as_view(),
         name='stock_detail_view')
]
