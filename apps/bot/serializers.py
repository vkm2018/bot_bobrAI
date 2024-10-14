from rest_framework import serializers
from .models import InfoBot, ProfileTelegram, CommandBot


class InfoBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBot
        fields = '__all__'


class ProfileTelegramSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileTelegram
        fields = ['user_id', 'username']

class CommandBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandBot
        fields = ['profile', 'command', 'created_at']
