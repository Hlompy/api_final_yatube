# API к проекту "Yatube"

## Описание

Проект представляет собой API для проекта yatube.

Функционал: Авторизация по токену

Обработка GET, POST, PATCH, PUT и DELETE запросов к базе данных проекта Yatube

## Установка

### 1) Склонировать репозиторий

### 1) Создать и активировать виртуальное окружение для проекта
```
python -m venv venv
source venv/scripts/activate
```
### 3)Установить зависимости(также "заморозить" их)
```
pip install -r requirements.txt
pip freeze requirements.txt
```
### 4)Сделать миграции
```
python manage.py makemigrations
python manage.py migrate
```
### 5)Запустить сервер
```
python manage.py runserver
```

## Примеры

Для доступа к API необходимо получить токен: 
Нужно выполнить POST-запрос ```/api/v1/token/``` передав поля username и password. API вернет токен

Передавайте токен в заголовке Authorization: Bearer <ваш_токен>

Дальше, передав токен можно будет обращаться к методам, например: 
```
/api/v1/posts/
/api/v1/groups/
/api/v1/follow
```
