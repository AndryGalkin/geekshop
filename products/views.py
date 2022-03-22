from django.shortcuts import render

# Create your views here.


def index(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', content)


def prod(request):

    content = {
        'title': 'GeekShop - каталог',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
             'comment': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
             'price': '6 090,00 руб.',
             'img_url': 'static/vendor/img/products/Adidas-hoodie.png'},
            {'name': 'Синяя куртка The North Face',
             'comment': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
             'price': '23 725,00 руб.',
             'img_url': 'static/vendor/img/products/Blue-jacket-The-North-Face.png'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
             'comment': 'Материал с плюшевой текстурой. Удобный и мягкий.',
             'price': '3 390,00 руб.',
             'img_url': 'static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'},
            {'name': 'Черный рюкзак Nike Heritage',
             'comment': 'Плотная ткань. Легкий материал.',
             'price': '2 340,00 руб.',
             'img_url': 'static/vendor/img/products/Black-Nike-Heritage-backpack.png'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
             'comment': 'Гладкий кожаный верх. Натуральный материал.',
             'price': '13 590,00 руб.',
             'img_url': 'static/vendor/img/products/Black-Dr-Martens-shoes.png'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
             'comment': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
             'price': '2 890,00 руб.',
             'img_url': 'static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'}
        ],
    }

    return render(request, 'products/products.html', content)


