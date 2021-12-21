import pytest


@pytest.fixture
def car_create():
    return {"make": "Audi", "model": "A6"}


@pytest.fixture
def fake_car_create():
    return {"make": "fake", "model": "A6"}


@pytest.fixture
def rate_create():
    return {"rating": "4", "car_id": "1"}


@pytest.fixture
def sec_rate_create():
    return {"rating": "2", "car_id": "1"}


@pytest.fixture
def fake_rate_create():
    return {"rating": "6", "car_id": "1"}
