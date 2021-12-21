from rest_framework.routers import DefaultRouter

from cars.views import CarsViewSet, PopularViewSet, RateViewSet

router = DefaultRouter()
router.register(r"cars", CarsViewSet, basename="cars")
router.register(r"popular", PopularViewSet, basename="popular")
router.register(r"rate", RateViewSet, basename="rate")
urlpatterns = router.urls
