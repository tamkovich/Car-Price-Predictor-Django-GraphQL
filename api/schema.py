import graphene
import django_filters

from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from api.models import Car
from logic_application.network import Network


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


class Query(graphene.ObjectType):
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


class CreateCar(graphene.Mutation):
    price = graphene.Int()

    year_model = graphene.Int()
    mileage = graphene.Int()
    fiscal_power = graphene.Int()
    fuel_type = graphene.String()
    mark = graphene.String()

    class Arguments:
        price = graphene.Int()

        year_model = graphene.Int()
        mileage = graphene.Int()
        fiscal_power = graphene.Int()
        fuel_type = graphene.String()
        mark = graphene.String()

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    def mutate(self, info, *args, **kwargs):
        print(kwargs)
        car = Car.objects.create(**kwargs)
        ok = True
        return CreateCar(car=car, ok=ok)


class PredictCarPrice(graphene.Mutation):
    price = graphene.Int()
    
    year_model = graphene.Int()
    mileage = graphene.Int()
    fiscal_power = graphene.Int()
    fuel_type = graphene.String()
    mark = graphene.String()

    class Arguments:
        year_model = graphene.Int()
        mileage = graphene.Int()
        fiscal_power = graphene.Int()
        fuel_type = graphene.String()
        mark = graphene.String()

    def mutate(self, info, *args, **kwargs):
        network = Network()
        print(kwargs)
        res = network.predict(kwargs)
        kwargs.update(res)
        car = Car(**kwargs)
        print(res)
        return car


class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    predict_car_price = PredictCarPrice.Field()
