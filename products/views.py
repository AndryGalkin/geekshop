
import json
from django.shortcuts import render



# Create your views here.


def index(request):
    content = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', content)


def prod(request):
    content = {
        'title': 'GeekShop - каталог',
        'products': 'Prod',
    }

    with open('products/fixtures/products.json', encoding='utf8') as json_file:
        products = json.load(json_file)
        content['products'] = products

    return render(request, 'products/products.html', content)


