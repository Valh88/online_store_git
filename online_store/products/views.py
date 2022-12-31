from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django import forms
from .models import Product
from django.views import generic
from cart.forms import CartAddProductForm
from reviews.forms import AddReviewForm
from .models import Catalog
from django.urls import reverse
from taggit.models import Tag
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.select_related('catalog').all()
    template_name = 'products/catalog.html'
    context_object_name = 'catalog'
    paginate_by = 8

    # def get_queryset(self):
    #     queryset = Product.objects.select_related('catalog').all()
    #     sort = self.request.GET.get('sort')
    #     if sort:
    #         if sort == 'price_min':
    #             queryset = queryset.order_by('price')
    #         elif sort == 'price_max':
    #             queryset.order_by('-price')
    #         elif sort == 'new_min':
    #             queryset.order_by('-updated')
    #         elif sort == 'new_max':
    #             queryset.order_by('updated')
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = cache.get_or_set('queryset', self.get_queryset(), 30)
        search = self.request.GET.get('search')
        if search:
            context['catalog'] = queryset.filter(name__icontains=search)

        form = CartAddProductForm()
        form.fields['quantity'].widget = forms.HiddenInput()
        context['form_add_cart'] = form
        return context

    # def get(self, request, *args, **kwargs):
    #     try:
    #         cat_name = kwargs['cat_name']
    #         if cat_name:
    #             products = self.get_queryset().filter(catalog__name=cat_name)
    #     except Exception:
    #         products = self.get_queryset()
    #
    #     search = self.request.GET.get('search')
    #     if search:
    #         products = self.get_queryset().filter(name__icontains=search)
    #     form = CartAddProductForm()
    #     form.fields['quantity'].widget = forms.HiddenInput()
    #     return render(request, template_name='products/catalog.html', context={'catalog': products,
    #                                                                            'form_add_cart': form})

    def post(self, request, *args, **kwargs):
        price = self.request.POST.get('price')
        price = price.split(';')
        title = self.request.POST.get('title')
        box = self.request.POST.get('box')
        delivery = self.request.POST.get('delivery')
        form = CartAddProductForm()
        form.fields['quantity'].widget = forms.HiddenInput()
        catalog = self.get_queryset().filter(price__range=(price[0], price[1]), name__icontains=title)
        if box:
            box = 'checked'
        if delivery:
            delivery = 'checked'
            
        # return render(request, 'products/catalog.html', context={'catalog': catalog,
        #                                                          'form_add_cart': form,
        #                                                          'box': box,
        #                                                          'delivery': delivery,
        #                                                          'price_min': price[0],
        #                                                          'price_max': price[1]})
        return render(request, 'include/product_list.html', context={'catalog': catalog,
                                                                    'form_add_cart': form,
                                                                    'box': box,
                                                                    'delivery': delivery,
                                                                    'price_min': price[0],
                                                                    'price_max': price[1]})


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        form = AddReviewForm()
        user = self.request.user
        if user.is_authenticated:
            form = AddReviewForm(initial={'name': f'{user.first_name} {user.last_name}',
                                          'email': user.email})
        context['review_form'] = form
        return context


def category_product(request, cat_name):
    products = Product.objects.select_related('catalog').filter(catalog__name=cat_name).all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page_number')
    page_obj = paginator.get_page(page_number)
    form = CartAddProductForm()
    form.fields['quantity'].widget = forms.HiddenInput()
    return render(request, template_name='products/catalog.html', context={'catalog': products,
                                                                           'form_add_cart': form,
                                                                           'page_obj': page_obj})


def tag_render(request, tag_slug=None):
    products = Product.objects.select_related('catalog').all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags=tag)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page_number')
    page_obj = paginator.get_page(page_number)

    form = CartAddProductForm()
    form.fields['quantity'].widget = forms.HiddenInput()
    return render(request, template_name='products/catalog.html', context={'catalog': products,
                                                                           'form_add_cart': form,
                                                                           'page_obj': page_obj})
