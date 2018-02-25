разработка в ветке DEVELOP !!

Установка зависимостей:
```bash
pip install -U -r requirements.txt
```

Как получить requirements.txt, имея django проект?
```bash
pip freeze > requirements.txt
```

Перед загрузкой фикстур провести миграции, затем из дериктории проекта в терминале выполнить в такой последовательности:

1.

python manage.py loaddata group/fixtures/initial_data.json

2.

python manage.py loaddata students/fixtures/initial_data.json


В проект добавленна регистрация с подтверждением на почту
Для того чтобы она работала в settings.py нужно подставить актуальные данные для:

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''



команда для получения списка групп и количества в них студентов выполняется в терминале из корня проекта:

./manage.py modelsinfo


Сайт доступен длфя просмотра 90 дней со дня публикации по адресу:

ivanbabaievtestaccount.pythonanywhere.com

регистрацию не настраивал, работает локально.

авторизация по:

login - admin
pass  - admin123

либо

login - py.dev.ib@gmail.com
pass  - admin123
