
import requests
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'textsearch.settings'
django.setup()

url = 'https://dummyjson.com/products?limit=1200&offset=200'
response = requests.get(url)
data = response.json()
from home.models import Product


for product in data['products']:
    # print(product['brand'])
    try:
        product = Product(
            title=product['title'],
            description=product['description'],
            category=product['category'],
            price=product['price'],
            brand=product['brand'] if 'brand' in product else None,
            sku=product['sku'],
            thumbnail=product['thumbnail'],
        )
        product.save()

    except Exception as e:
        print(f"Error creating product: {e}")
