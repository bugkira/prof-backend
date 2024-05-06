t# prof-backend
## Зависимости
Создаем виртуальное окружение

`python3 -m venv .venv`

Входим в виртуальное окружение

`source .venv/bin/activate` 

Устанавливаем зависимости

`pip install django django-mptt mptt-admin django-ckeditor`


## About
Макет дизайна по ссылке - https://www.figma.com/design/0L5ytO5WnLZS21dIxNNemU/%D0%9F%D0%A0%D0%9E%D0%A4?node-id=0-1&t=AyNVWlVSMbdXOJUP-0
### Как запустить?
Да как обычный джанго. Админка - admin / admin. 
`python manage.py runserver`

### Что надо?
Сделать модели для всей информации на страницах и сделать эндпойнты двух видов - категории со списками категорий/статей и, собственно, статьи. 
Желательно по мере разработки моделей обновлять код и добавлять элементы в base.html, чтобы можно было наглядно увидеть, что всё работает. Ничего сложного не надо, голый html.

### Что сделано?
Примитивная модель для контактной инфы в футере, модель категорий и какая-то простая модель для текста статьи. GPT4 уверяет меня, что для статьи достаточно хранить HTML-разметку, а все файлы внутри текста браузер сам подтянет с сервера.

### Почему так долго делается?
Оно слишком просто, я теряюсь и думаю, что всё не так однозначно.
