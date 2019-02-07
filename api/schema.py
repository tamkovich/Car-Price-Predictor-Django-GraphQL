import graphene

from graphene_django.types import DjangoObjectType

from api.models import Car


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class Query(object):
    all_cars = graphene.List(CarType)

    car = graphene.Field(
        CarType,
        id=graphene.Int(),
        mark=graphene.String()
    )

    def resolve_all_cars(self, info, **kwargs):
        return Car.objects.all()[:10]

    def resolve_car(self, info, **kwargs):
        id = kwargs.get('id')
        mark = kwargs.get('mark')

        if id is not None:
            return Car.objects.get(pk=id)

        if mark is not None:
            return Car.objects.filter(mark=mark).first()

        return None
