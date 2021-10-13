# Куда пойти — Москва глазами Артёма

Cайт https://afisha.2qwerty.com/ о самых интересных местах в Москве. Авторский проект Артёма.

## Запуск
Для работы требуется python версии >=3.9 
- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE_URL` — однострочный адрес к базе данных, например: `sqlite:///db.sqlite3`. Больше информации в [документации](https://github.com/jacobian/dj-database-url)

## Добавление мест

Для добавления локаций можно командой `python3 manage.py load_place <link>`
где `link` - ссылка на json с описанием объекта, [пример](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json)  

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).