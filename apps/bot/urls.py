from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.bot.views import LogView, StartCommandDocumentation, \
    WeatherCommandDocumentation

urlpatterns = [
    path('logs/', LogView.as_view(), name='log'),
    path('logs/<int:user_id>/', LogView.as_view(), name='user_log'),
    path('tg_bot/start/', StartCommandDocumentation.as_view(), name='start-command-doc'),
    path('tg_bot/weather/', WeatherCommandDocumentation.as_view(), name='weather-command-doc'),



]
