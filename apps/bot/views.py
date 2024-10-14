from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from apps.bot.models import InfoBot
from apps.bot.serializers import InfoBotSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

class LogView(generics.ListAPIView):
    queryset = InfoBot.objects.all()
    serializer_class = InfoBotSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_ad']

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id is not None:
            return InfoBot.objects.filter(profile=user_id)
        return InfoBot.objects.all()


class StartCommandDocumentation(APIView):

    @swagger_auto_schema(
        operation_summary="Команда /start",
        operation_description="""
        Команда `/start` приветствует пользователя и создает профиль в базе данных,
        если его еще нет. Возвращает приветственное сообщение.
        """,
        responses={200: openapi.Response('Успешный ответ')}
    )
    def get(self, request):
        return Response({
            "command": "/start",
            "description": "Приветствие пользователя и создание профиля в базе данных."
        })


class WeatherCommandDocumentation(APIView):

    @swagger_auto_schema(
        operation_summary="Команда /weather",
        operation_description="""
        Команда `/weather` запрашивает у пользователя название города.
        После ввода города бот возвращает информацию о погоде, используя OpenWeather API.
        """,
        responses={200: openapi.Response('Успешный ответ')}
    )
    def get(self, request):
        return Response({
            "command": "/weather",
            "description": "Запрос города и получение информации о погоде."
        })