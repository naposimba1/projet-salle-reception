from rest_framework import routers
from django.urls import path, include

from sallereception.settings import REST_FRAMEWORK
from .views import *


router = routers.DefaultRouter()

router.register("client", ClientViewSet)
router.register("type_fete", Type_FeteViewSet)
router.register("type_decor", Type_DecorViewSet)
router.register("reservation", ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
