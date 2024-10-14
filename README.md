
Запустить локольно:

1. Клонирование:
``` 
mkdir telegram_bot_service
cd stripe_service
git clone <SSH repo_url>
```

2. Зависимости
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Создать БД
4. Найти в телеграм бота bobrAI_test_bot
5. Необходимо создать .env и по аналогии .env.example заполнить параметры подключений
6. Вставить Токены. 
```
TG_TOKEN = '8068324610:AAHqdUK157mytKeeStUCCpYQB3s_qpCJKWo'
OW_TOKEN = 'c315b6867bdff6b304c9bcfb6ce9b574'
```
7. Сделать миграции и создать супер пользователя

```
./manage.py migrate
./manage.py createsuperuser
```
8. Запустить сервер
   
```
/manage.py runserver
```
10. Запустить бота
    
```
/manage.py bot
```

7. Документация Swagger
```
http://127.0.0.1:8000/swagger/
```
