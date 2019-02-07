import graphene

from graphene_django.types import DjangoObjectType

from api.models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class Query(object):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(self, info, **kwargs):
        return Car.objects.all()[:10]
