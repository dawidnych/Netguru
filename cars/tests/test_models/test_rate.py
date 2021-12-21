import pytest

from cars.models import Rate


@pytest.mark.django_db
class TestRate:
    def test_create_rate(self, client, car_create, rate_create, fake_rate_create):
        assert Rate.objects.count() == 0
        client.post("/cars/", car_create)
        client.post("/rate/", rate_create)
        client.post("/rate/", fake_rate_create)
        assert Rate.objects.count() == 1
