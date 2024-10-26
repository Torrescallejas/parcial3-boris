from django.urls import include, path
from rest_framework import routers
from api.views import InvitadosViewSet

router = routers.DefaultRouter()
router.register(r'invitados', InvitadosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]