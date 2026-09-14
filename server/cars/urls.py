from cars.views import GearViewSet, FuelViewSet, ColorViewSet, BrandViewSet, CarStatusViewSet, ClientCarViewSet
from cars.views import CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cars', CarViewSet, basename = 'car')
router.register('client/cars', ClientCarViewSet, basename = 'client-car')
router.register('gears', GearViewSet, basename = 'gear')
router.register('fuels', FuelViewSet, basename = 'fuel')
router.register('colors', ColorViewSet, basename = 'color')
router.register('brands', BrandViewSet, basename = 'brand')
router.register('statuses', CarStatusViewSet, basename = 'status')

urlpatterns = router.urls
