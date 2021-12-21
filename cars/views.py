from rest_framework import viewsets

from cars.models import Cars, Rate
from cars.serializers import (CarDetailSerializer, CarPopularSerializer,
                              CarsSerializer, RateSerializer)


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CarDetailSerializer
        return CarsSerializer


class PopularViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarPopularSerializer
