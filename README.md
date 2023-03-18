![example workflow](https://github.com/shmyrev/foodgram-project-react/actions/workflows/food_workflow.yml/badge.svg)  

## Описание проекта:  

url: 158.160.16.23  
Временный логин и пароль:  
email: admin@admin.ru  
password: 12345

### Foodgram, «Продуктовый помощник» - сайт с вашими рецептами.  
«Продуктовый помощник»: сайт, на котором пользователи могут публиковать  
рецепты, добавлять чужие рецепты в избранное и подписываться на публикации  
других авторов. Сервис «Список покупок» позволит пользователям создавать  
список продуктов, которые нужно купить для приготовления выбранных блюд.  

## Установка и запуск проекта:  

Данный проект настроин для приложения Continuous Integration и  
Continuous Deployment, а это значит:  
- автоматический запуск тестов  
- обновление образов на Docker Hub  
- автоматический деплой на боевой сервер при пуше в главную ветку main.  

Описание workflow в файле .github/workflows/food_workflow.yml:  

- сборка и доставка докер-образа для контейнера web на Docker Hub;  
- автоматический деплой проекта на боевой сервер;  
- отправка уведомления в Telegram о том, что процесс деплоя  
успешно завершился.  

### Подготовка сервера:

1. Войдите на свой удаленный сервер в облаке.  
2. Остановите службу nginx:  
```
sudo systemctl stop nginx
```
3. Установите docker:  
```
sudo apt install docker.io
```
4. Установите docker-compose:  
```
sudo apt install docker-ce docker-compose -y
```
5. Скопируйте файлы docker-compose.yaml и nginx/default.conf из вашего  
проекта на сервер в home/<ваш_username>/docker-compose.yaml и  
home/<ваш_username>/nginx/default.conf соответственно.  

В GitHub Actions необходимо указать секреты:  
1. Перейдите в настройки репозитория Settings, выберите на панели  
слева Secrets, нажмите New secret:  
2. Сохраните переменные:  
DokerHub:  
- DOCKER_USERNAME    логин для доступа на DockerHub  
- DOCKER_PASSWORD    пароль для доступа на DockerHub  
Сервер:  
- HOST               имя или ip сервера  
- USER               логин для доступа на сервер  
- SSH_KEY            ssh ключ, можно увидить  cat ~/.ssh/id_rsa  
- PASSPHRASE         секретная фраза для ssh ключа  
Создание .env файла:  
- ALLOWED_HOSTS      имя или ip сервера   
- DB_ENGINE          указываем, что работаем с postgresql  
- DB_NAME            имя базы данных  
- POSTGRES_USER      логин для подключения к базе данных  
- POSTGRES_PASSWORD  пароль для подключения к БД (установите свой)  
- DB_HOST            название сервиса (контейнера)  
- DB_PORT            порт для подключения к БД  
Телеграм бот:  
- TELEGRAM_TO        ID своего телеграм-аккаунта. Узнать у бота @userinfobot  
- TELEGRAM_TOKEN     токен вашего бота. Получить у бота @BotFather  


### Установка в ручном режиме.

Клонировать репозиторий и перейти в него в командной строке:  

```
https://github.com/shmyrev/yamdb_final.git
```

```
cd yamdb_final/
```

Переходим в папку с файлом docker-compose.yaml:

```
cd infra/
```

Создаем .env файл:

```
nano .env
```

Вносим эти данные:

```
TOKEN=54321 # указать секретный ключ для разработчиков

ALLOWED_HOSTS=0.0.0.0   # указать имя или ip сервера

DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql

DB_NAME=postgres # имя базы данных

POSTGRES_USER=postgres # логин для подключения к базе данных

POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)

DB_HOST=db # название сервиса (контейнера)

DB_PORT=5432 # порт для подключения к БД
```

Запускаем docker compose командой:

```
docker-compose up -d --build
```

Запускаем миграцмм:  

```
docker-compose exec web python manage.py makemigrations  
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:  

```
docker-compose exec web python manage.py createsuperuser
```

Создаем статику:  

```
docker-compose exec web python manage.py collectstatic --no-input
```

Заполнение базы тестовыми данными:  

```
docker-compose exec web python manage.py add_data  
```

Создаем дамп базы данных:  

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Останавть контейнер:

```
docker-compose down -v
```


## Примеры использования API:


Пример рабочего проекта на сервере можно посмотреть здесь:

```
http://158.160.16.23/
```

Дитальное описание и примеры работы API проекта представлены в 
документации в формате ReDoc:

```
http://158.160.16.23/redoc/
```

Получение произведений:

```
GET /api/recipe/
```

Добавление произведения (только администратор):

```
POST /api/recipe/
```

В параметрах передавать json

```
{
    "name": "Название произведения",
    "year": 1990,
    "description": "Описание произведения",
    "genre": [
    "fantasy"
    ],
    "category": "films"
}
```

## Используется:

```
Python 3.9 Django 3.2 Simple JWT
```