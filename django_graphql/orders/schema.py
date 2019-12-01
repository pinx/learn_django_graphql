import graphene
from graphene_django import DjangoObjectType

from django_graphql.orders.models import Order, OrderProduct


class OrderType(DjangoObjectType):
    class Meta:
        model = Order

    orderProducts = [OrderProduct]

    def resolve_orderProducts(self, info):
        return Order.orderproduct_set


class OrderProductType(DjangoObjectType):
    class Meta:
        model = OrderProduct


class Query(graphene.ObjectType):
    orders = graphene.List(OrderType)

    def resolve_orders(self, info, **kwargs):
        return Order.objects.prefetch_related('orderproduct_set').all()


schema = graphene.Schema(query=Query)
