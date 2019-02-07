import graphene

from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from api.models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class CarNode(DjangoObjectType):
    class Meta:
        model = Car
        # Allow for some more advanced filtering here
        filter_fields = {
            'price': ['exact'],
            'year_model': ['exact'],
            'mileage': ['exact'],
            'fiscal_power': ['exact'],
            'fuel_type': ['exact', 'icontains', 'istartswith'],
            'mark': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class Query(object):
    car = relay.Node.Field(CarNode)
    all_cars = DjangoFilterConnectionField(CarNode)

    # all_cars = graphene.List(CarType)
    #
    # car = graphene.Field(
    #     CarType,
    #     id=graphene.Int(),
    #     mark=graphene.String()
    # )
    #
    # def resolve_all_cars(self, info, **kwargs):
    #     return Car.objects.all()[:10]
    #
    # def resolve_car(self, info, **kwargs):
    #     id = kwargs.get('id')
    #     mark = kwargs.get('mark')
    #
    #     if id is not None:
    #         return Car.objects.get(pk=id)
    #
    #     if mark is not None:
    #         return Car.objects.filter(mark=mark).first()
    #
    #     return None
