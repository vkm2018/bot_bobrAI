import asyncio
import requests
from aiogram.filters import Command, CommandStart
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from asgiref.sync import async_to_sync, sync_to_async
from django.conf import settings
from django.core.management import BaseCommand

from apps.bot.models import ProfileTelegram, InfoBot, CommandBot

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

class City(StatesGroup):
    name = State()

@dp.message(CommandStart())
async def start(message:types.Message):
    user, created = await sync_to_async(ProfileTelegram.objects.get_or_create)(
        user_id=message.from_user.id,
        username=message.from_user.username
    )

    command = message.text.split()[0]
    if command.startswith('/'):
        await sync_to_async(CommandBot.objects.create)(profile=user,command=command)
    if created:
       await message.reply(f'Добро пожаловать, {message.from_user.username}! '
                           f'Этот бот создан для проверки тестового задания компании BobrAI')
    else:
        await message.reply(f'Приветствую тебя вновь {message.from_user.username}')


@dp.message(Command('weather'))
async def weather(message: types.Message, state:FSMContext):
    await message.answer('Введите название города')
    await state.set_state(City.name)
    user = await sync_to_async(ProfileTelegram.objects.get)(
        user_id=message.from_user.id,
    )
    command = message.text.split()[0]
    if command.startswith('/'):
        await sync_to_async(CommandBot.objects.create)(profile=user, command=command)

@dp.message(City.name)
async def get_weather(message:types.Message):
    city = message.text
    try:


        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.TOKEN_WEATHER}&units=metric')
        if r.status_code != 200:
            raise Exception('Ошибка при получении данных')
        data = r.json()
        city = data["name"]
        current_temp = data['main']['temp']
        feels = data['main']['feels_like']
        desc = data['weather'][0]['description']
        hum = data['main']['humidity']
        wind = data['wind']['speed']
        await message.answer(f'Город:{city}\n'
              f'Температра: {current_temp}\n'
              f'Ощущаемая температура: {feels}\n'
              f'Описание: {desc}\n'
              f'Влажность: {hum}%\n'
              f'Скорость ветра: {wind}' )

        try:
            user = await sync_to_async(ProfileTelegram.objects.get)(
                user_id=message.from_user.id,
            )
            await sync_to_async(InfoBot.objects.create)(profile=user, city=city, current_temp=current_temp,
                                                        feels=feels, desc=desc, hum=hum, wind=wind)
        except ProfileTelegram.DoesNotExist:
            await message.reply('Пользователь не найден.')

    except Exception as e:

        await message.reply(f'Произошла ошибка: {str(e)}')



class Command(BaseCommand):
    help = 'Запускает Telegram-бот для BobrAI'

    def handle(self, *args, **options):
        # Запуск бота в асинхронном режиме
        asyncio.run(self.start_bot())

    async def start_bot(self):
        await dp.start_polling(bot)

