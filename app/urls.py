from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('sale.urls')),
    path('api/v1/', include('stock.urls')),
]
