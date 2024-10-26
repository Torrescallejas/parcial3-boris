from rest_framework import serializers
from api.models import Celebraciones, Invitados


class CelebracionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebraciones
        fields = ['id', 'nombre', 'fecha', 'hora', 'ubicacion']

class InvitadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitados
        fields = ['id', 'nombre', 'email', 'celebracion', 'presente']