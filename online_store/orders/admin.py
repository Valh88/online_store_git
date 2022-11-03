from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLines(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'delivery', 'status', 'created']
    actions = ['status_in_purchased', 'status_in_errors', 'status_in_waiting_payment',
               'purchase_online_cart', 'purchase_someone_cart', 'type_free_delivery', 'type_paid_delivery']

    inlines = [OrderItemInLines, ]

    def status_in_purchased(self, request, queryset):
        queryset.update(status='p')

    def status_in_errors(self, request, queryset):
        queryset.update(status='p')

    def status_in_waiting_payment(self, request, queryset):
        queryset.update(type_pay='w')

    def purchase_online_cart(self, request, queryset):
        queryset.update(type_pay='o')

    def purchase_someone_cart(self, request, queryset):
        queryset.update(status='s')

    def type_free_delivery(self, request, queryset):
        queryset.update(delivery='f')

    def type_paid_delivery(self, request, queryset):
        queryset.update(delivery='p')

    status_in_purchased.short_description = 'purchased'
    status_in_errors.short_description = 'errors'
    status_in_waiting_payment.short_description = 'waiting for payment'
    purchase_online_cart.short_description = 'online cart'
    purchase_someone_cart.short_description = 'payment from someone else account'
    type_free_delivery.short_description = 'free delivery'
    type_paid_delivery.short_description = 'paid delivery'


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'price', 'quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
