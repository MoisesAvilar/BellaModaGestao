from rest_framework import serializers
from stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = '__all__'

    def get_product_name(self, obj):
        return obj.product.description
