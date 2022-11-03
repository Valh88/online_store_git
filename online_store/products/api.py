from rest_framework import viewsets
from .serializers import ProductSerializer, CatalogSerializer
from products.models import Product, Catalog
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import DjangoModelPermissions


class ProductViewSet(viewsets.ModelViewSet, CreateModelMixin, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CatalogViewSet(viewsets.ModelViewSet, CreateModelMixin, ListModelMixin):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = [DjangoModelPermissions]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
