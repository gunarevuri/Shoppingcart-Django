from rest_framework import serializers

from store.models import Product, ShoppingCartItem

class CartItemSerializer(serializers.ModelSerializer):
	quantity = serializers.IntegerField(min_value=1, max_value=100)
	class Meta:
		model = ShoppingCartItem
		fields = ('product', 'quantity')


class ProductSerializer(serializers.ModelSerializer):


	class Meta:
		model = Product
		fields = ('id', 'name', 'description', 'price', 'sale_start', 'sale_end', 'is_on_sale', 'current_price', 'cart_items','photo',)


	is_on_sale = serializers.BooleanField(read_only = True)
	current_price = serializers.FloatField(read_only = True)
	description = serializers.CharField(min_length = 2, max_length = 200)
	cart_items = serializers.SerializerMethodField()
	price = serializers.DecimalField(
		min_value = 1.00, max_value=10000, max_digits = None, decimal_places = 2)
	# time format hout/minute am/pm date month year"
	sale_start = serializers.DateTimeField(
		required=False,
		input_formats = ['%I:%M %p %d %B %Y'], format = None, allow_null = True,
		help_text='Accepted format is "12:01 AM 7 June 2020"',
		style = {'input_type': 'text', 'placeholder':'12:01 AM June 2020'},
	)
	sale_end = serializers.DateTimeField(
		required=False,
		input_formats = ['%I:%M %p %d %B %Y'], format = None, allow_null = True,
		help_text='Accepted format is "12:01 AM 7 June 2020"',
		style = {'input_type': 'text', 'placeholder': '12:01 AM June 2020'},
	)
	photo = serializers.ImageField(default = None)




	def get_cart_items(self, instance):
		items = ShoppingCartItem.objects.filter(product = instance)
		return CartItemSerializer(items, many = True).data



	# def to_representation(self, instance):
	#     data = super().to_representation(instance)
	#     data['is_on_sale'] = instance.is_on_sale()
	#     data['current_price'] = instance.current_price()
	#     return data

class ProductStatSerializer(serializers.Serializer):
	stats = serializers.DictField(
		child = serializers.ListField(
			child = serializers.IntegerField(),
		)
	)












