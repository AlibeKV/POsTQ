from django.urls import path , include

from rest_framework.routers import DefaultRouter

from .views import POstSet



urlpatterns = [
]

router = DefaultRouter()
router.register('1',POstSet, basename='Booking')


urlpatterns += router.urls
