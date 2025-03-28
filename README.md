
Описание

ASMB Student Platfor е Django уеб приложение, което позволява на потребителите да създават, управляват и присъстват на събития. Потребителите могат да събират точки за всяко събитие, на което присъстват, което ги мотивира да бъдат по-активни.

--Функционалности

    -Създаване и управление на събития
    -Регистрация и влизане на потребители
    -Система за точки на база присъствия
    -Администраторски панел за управление на събития и потребители
    -API за интеграция с външни системи 

--Технологии

    -Backend: Django, Django REST Framework
    -Database: PostgreSQL / SQlite при разработка
    -Frontend: HTML, CSS, React

--Инсталация

    -Клониране на репозиторито:
        https://github.com/ValentinPashev/Points.git
        cd points
    
    -Създаване и активиране на виртуална среда:
    
        python -m venv venv
        venv\Scripts\activate  # За Windows
    
    -Инсталиране на зависимостите:
    
        -pip install -r requirements.txt

    -Извършване на миграции и стартиране на сървъра:
        python manage.py migrate
        python manage.py runserver

--Използване

    -Създайте суперпотребител, за да управлявате събития:

        python manage.py createsuperuser 
        Достъп до администраторския панел: http://127.0.0.1:8000/admin


--Автори

    Валентин Пашев
