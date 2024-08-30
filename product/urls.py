from django.urls import path
from product.views import ProductListView, ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list_view'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(),
         name='product_detail_view')
]
