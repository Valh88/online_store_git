from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from taggit.managers import TaggableManager
from django.db.models import Min


def user_directory_path(instance, image_name):
    return f'catalog/{instance.catalog.name}/{image_name}'


def photo_product_directory_path(instance, image_name):
    return f'products/{instance.product.id}/photo/{image_name}'


class Catalog(models.Model):
    name = models.CharField(max_length=15, verbose_name='name')
    # photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='photo')
    select_group = models.BooleanField(verbose_name='select group', default=False)
    is_active = models.BooleanField(default=True, verbose_name='is active')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'catalog'
        verbose_name_plural = 'catalogs'

    def min_price_catalog(self):
        products = Product.objects.filter(catalog=self.id)
        price = products.aggregate(Min('price'))
        return price['price__min']


class PhotoCatalog(models.Model):
    photo = models.ImageField(upload_to=user_directory_path, verbose_name='photo')
    catalog = models.ForeignKey(Catalog, related_name='photos', verbose_name='catalog', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'photo catalog'
        verbose_name_plural = 'photo catalogs'


class SubCatalog(models.Model):
    catalog = models.ForeignKey(Catalog, verbose_name='catalog', related_name='sub_catalogs', on_delete=models.CASCADE)
    name = models.CharField(max_length=15, verbose_name='name')
    is_active = models.BooleanField(default=True, verbose_name='is active')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'sub catalog'
        verbose_name_plural = 'sub catalogs'


class Product(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='products', verbose_name='catalog', on_delete=models.CASCADE)
    # sub_catalog = models.ForeignKey(SubCatalog, related_name='products', verbose_name=' sub catalog',
    #                                 on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, verbose_name='name product')
    tags = TaggableManager()
    description = models.TextField(max_length=500, verbose_name='description')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')
    count = models.IntegerField(verbose_name='count product', default=0)
    count_bay = models.IntegerField(verbose_name='count_purchases', default=0)
    limited_edition = models.BooleanField(verbose_name='limited edition', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='create data')
    updated = models.DateTimeField(auto_now=True, verbose_name='update data')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('product', args=str(self.pk))

    def images(self):
        images = PhotoProduct.objects.filter(product=self.id).first()
        print(images)
        if images:
            # return mark_safe(f'<img src="%s" style="width: 45px; height:45px;" />' % images.photo)
            return images.photo
        else:
            return 'No Image Found'

    images.short_description = 'Image'


class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to=photo_product_directory_path, verbose_name='photo')
    product = models.ForeignKey(Product, related_name='photos', verbose_name='product', on_delete=models.CASCADE)

    def image_tag(self):
        if self.photo:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.photo.url)
        else:
            return 'No Image Found'

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'photo product'
        verbose_name_plural = 'photo products'
