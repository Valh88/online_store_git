from products.models import Catalog
from cart.cart import Cart
from products.models import Product


def catalog(request):
    return {'menu': Catalog.objects.prefetch_related('products').filter(is_active=True).order_by('pk').all()}


def cart(request):
    return {'cart': Cart(request)}


def top_tags(request):
    tags = Product.tags.most_common()[:10]
    return {'tags': tags}
