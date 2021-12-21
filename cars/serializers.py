import requests
from django.db.models import Avg, Count
from rest_framework import serializers

from cars.models import Cars, Rate


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            "car_id",
            "rating",
        )

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating has to be between 1 and 5.")
        return value


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = (
            "make",
            "model",
        )

    def validate(self, data):
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{data["make"]}?format=json'
        response = requests.get(url)
        response_data = response.json()["Results"]
        if len(response_data) > 0:
            if not any(d["Model_Name"] == data["model"] for d in response_data):
                raise serializers.ValidationError("The model is not in the database.")
            else:
                return data
        else:
            raise serializers.ValidationError(
                "The manufacturer is not in the database."
            )


class CarDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = (
            "id",
            "make",
            "model",
            "avg_rating",
        )

    def get_avg_rating(self, obj):
        avg_ratings = float(
            [
                x
                for x in Rate.objects.filter(car_id=obj)
                .aggregate(Avg("rating"))
                .values()
            ][0]
            or 0.0
        )
        return avg_ratings


class CarPopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = (
            "id",
            "make",
            "model",
            "rates_number",
        )

    def get_rates_number(self, obj):
        rates_number = int(
            [
                x
                for x in Rate.objects.filter(car_id=obj)
                .aggregate(Count("rating"))
                .values()
            ][0]
        )
        return rates_number
