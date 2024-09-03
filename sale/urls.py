from django.urls import path
from sale.views import SaleListView, SaleRetrieveUpdateDestroyView


urlpatterns = [
    path('sale/', SaleListView.as_view(),
         name='sale_list_view'),
    path('sale/<int:pk>/', SaleRetrieveUpdateDestroyView.as_view(),
         name='sale_detail_view'),
]
