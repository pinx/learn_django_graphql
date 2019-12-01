from django.contrib import admin

# Register your models here.
from django_graphql.orders.models import Order, OrderProduct

admin.site.register(Order)
admin.site.register(OrderProduct)
