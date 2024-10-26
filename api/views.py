from io import BytesIO

import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Invitados, Celebraciones
from api.serializers import InvitadosSerializer

# Create your views here.
class InvitadosViewSet(viewsets.ModelViewSet):
    queryset = Invitados.objects.all()
    serializer_class = InvitadosSerializer

    @action(detail=False, methods=["GET"])
    def crearInvitado(self, request):
        nombre = request.query_params.get('nombre')
        email = request.query_params.get('email')
        celebracion_id = request.query_params.get('celebracion_id')
        presente = 0

        if not (nombre and email and celebracion_id):
            return Response(
                {"error": "Faltan datos para crear el invitado"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            celebracion = Celebraciones.objects.get(id=celebracion_id)
        except Celebraciones.DoesNotExist:
            return Response(
                {"error": "La celebracion no existe"},
                status=status.HTTP_404_NOT_FOUND
            )

        invitado = Invitados(nombre=nombre, email=email, celebracion=celebracion, presente=0)
        invitado.save()

        qr_data = f"id:{invitado.id}"
        qr_image = qrcode.make(qr_data)

        buffer = BytesIO()
        qr_image.save(buffer, "PNG")
        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/png")

    @action(detail=False, methods=["GET"])
    def actualizarInvitado(self, request):
        invitado_id = request.query_params.get('id')
        presente = request.query_params.get('presente')

        if not invitado_id:
            return Response(
                {"error": "El parametro 'id' es necesario"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            invitado = Invitados.objects.get(id=invitado_id)
        except Invitados.DoesNotExist:
            return Response(
                {"error": "Invitado no existe"},
                status=status.HTTP_404_NOT_FOUND
            )

        if presente is not None:
            invitado.presente = presente

        invitado.save()

        serializer = InvitadosSerializer(invitado)

        return Response(serializer.data, status=status.HTTP_200_OK)