from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.shortcuts import redirect
from .forms import AddReviewForm
from products.models import Product
from .models import Review


@require_POST
def review_add_to_product(request, product_id):
    review_form = AddReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.cleaned_data['review']
        name = review_form.cleaned_data['name']
        email = review_form.cleaned_data['email']
        product = get_object_or_404(Product, id=product_id)
        user = request.user
        try:
            Review.objects.create(review=review,
                                  user=user,
                                  name=name,
                                  product=product,
                                  email=email)
        except Exception:
            Review.objects.create(review=review,
                                  name=name,
                                  product=product,
                                  email=email)
    return HttpResponseRedirect(reverse('product', args=str(product_id)))
