from rest_framework.test import APITestCase

from store.models import Product

class ProductCreateTestCase(APITestCase):
	def test_create_product(self):
		initial_product_count = Product.objects.count()
		new_pro_data = {
			'name': "New Product from test",
			'price': '2345',
			'description': "awesome Product",
		}
		response = self.client.post('/api/products/new/', new_pro_data)
		if response.status_code != 201:
			print(response.data)
		self.assertEqual(Product.objects.count(), initial_product_count+1)
		self.assertEqual(float(response.data['price']), round(float(new_pro_data['price']),2))
		self.assertFalse(response.data['is_on_sale'])
		self.assertEqual(response.data['description'], new_pro_data['description'])


class ProductDestroyTestCase(APITestCase):
	def test_delete_product(self):
		initial_products_count = Product.objects.count()
		self.client.delete('api/products/delete/5/')
		# self.assertEqual(response.status_code, 204)
		print(initial_products_count)
		self.assertEqual(Product.objects.count(), initial_products_count-1)

class ProductListTestCase(APITestCase):
	def test_list_products(self):
		products = Product.objects.count()
		response = self.client.get('/api/products/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['count'], products)
		self.assertIsNone(response.data['next'])
		self.assertIsNone(response.data['previous'])



class ProductUpdateTestCase(APITestCase):
	def test_update_product(self):
		product = Product.objects.first()
		prod_data = {
		"name":"updated name",
		"description":"updated description",
		"price": "123",
		}
		response = self.client.patch('/api/products/{}/update/'.format(product.id),prod_data,format = 'json')
		update = Product.objects.get(id = product.id)
		self.assertEqual(update.name , "updated name")




