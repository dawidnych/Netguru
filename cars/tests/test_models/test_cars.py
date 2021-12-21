import pytest

from cars.models import Cars


@pytest.mark.django_db
class TestCars:
    def test_create_car(self, client, car_create, fake_car_create):
        assert Cars.objects.count() == 0
        client.post('/cars/', car_create)
        client.post('/cars/', fake_car_create)
        assert Cars.objects.count() == 1

    def test_delete_car(self, client, car_create):
        assert Cars.objects.count() == 0
        client.post('/cars/', car_create)
        assert Cars.objects.count() == 1
        client.delete('/cars/1/')
        assert Cars.objects.count() == 0

    def test_detail_car(self, client, car_create, rate_create, sec_rate_create):
        client.post('/cars/', car_create)
        client.post('/rate/', rate_create)
        client.post('/rate/', sec_rate_create)

        response = client.get('/cars/')
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 1
        assert data[0]['make'] == car_create['make']
        assert data[0]['model'] == car_create['model']
        assert data[0]['avg_rating'] == (int(rate_create['rating']) +
                                         int(sec_rate_create['rating']))/2

    def test_popular_car(self, client, car_create, rate_create, sec_rate_create):
        client.post('/cars/', car_create)
        client.post('/rate/', rate_create)
        client.post('/rate/', sec_rate_create)

        response = client.get('/popular/')
        data = response.json()
        assert data[0]['rates_number'] == 2
