from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps import apis

router = routers.DefaultRouter()
router.register('user', apis.UserViewset, basename='all_user')
router.register('prescription', apis.PrescriptionViewSet, basename='all_prescription')
router.register('diabetes', apis.DiabetesViewSet, basename='all_diabetes')
router.register('medicine', apis.MedicineViewSet, basename='all_medicine')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
#    path('day/', views.say_day)
]

urlpatterns += router.urls
