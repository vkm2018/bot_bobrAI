from django.contrib import admin

from apps.bot.models import InfoBot, ProfileTelegram, CommandBot

# Register your models here.

admin.site.register(InfoBot)
admin.site.register(ProfileTelegram)
admin.site.register(CommandBot)