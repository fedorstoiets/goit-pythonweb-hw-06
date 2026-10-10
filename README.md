# goit-pythonweb-hw-06

Домашнє завдання №6 з курсу **FullStack Web Development with Python**.

У проєкті реалізовано базу даних PostgreSQL для навчальної системи зі студентами, групами, викладачами, предметами та оцінками.

Для роботи з базою даних використано:

- PostgreSQL
- Docker
- SQLAlchemy
- Alembic
- Faker

## Автор

**Fedor Stoietskyi**

---

## Мета проєкту

Необхідно було реалізувати базу даних, яка містить:

- студентів;
- групи;
- викладачів;
- предмети;
- зв'язок предметів із викладачами;
- оцінки студентів;
- дату отримання кожної оцінки.

Також необхідно:

- створити SQLAlchemy-моделі;
- використовувати Alembic для міграцій;
- заповнити базу випадковими даними через Faker;
- реалізувати 10 запитів до бази даних через SQLAlchemy.

---

# Структура проєкту

```text
goit-pythonweb-hw-06/
│
├── alembic/
│   ├── versions/
│   │   └── *_create_students_database_tables.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── database.py
├── models.py
├── seed.py
├── my_select.py
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md

Модель бази даних
Проєкт містить п'ять основних таблиць.
Group
Містить навчальні групи.
Основні поля:
id
name

Одна група може містити багато студентів.
Student
Містить інформацію про студентів.
Основні поля:
id
name
group_id

Кожен студент належить до однієї групи.
Teacher
Містить викладачів.
Основні поля:
id
name

Один викладач може викладати декілька предметів.
Subject
Містить навчальні предмети.
Основні поля:
id
name
teacher_id

Кожен предмет має викладача.
Grade
Містить оцінки студентів.
Основні поля:
id
student_id
subject_id
grade
date_received

Кожна оцінка пов'язана:
- зі студентом;
- із предметом;
- із датою її отримання.
Зв'язки між моделями
Спрощена структура бази:
Group
  |
  └── Student
        |
        └── Grade
              |
              └── Subject
                    |
                    └── Teacher

Основні зв'язки:
Group   1 ─── N Student
Student 1 ─── N Grade
Subject 1 ─── N Grade
Teacher 1 ─── N Subject

PostgreSQL у Docker
PostgreSQL запускається у Docker-контейнері.
Приклад:
docker run --name hw06-postgres \
  -p 5435:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=hw06password \
  -e POSTGRES_DB=postgres \
  -d postgres:15

У цьому середовищі використовується порт 5435 на локальному комп'ютері, оскільки інші PostgreSQL-контейнери вже використовують інші порти.
Схема підключення:
Application
    |
    v
127.0.0.1:5435
    |
    v
Docker PostgreSQL:5432

Підключення SQLAlchemy
Рядок підключення знаходиться у файлі:
database.py

Використовується SQLAlchemy разом із драйвером pg8000.
DATABASE_URL = (    "postgresql+pg8000://postgres:hw06password@127.0.0.1:5435/postgres")


Залежності
Основні залежності:
SQLAlchemy
alembic
pg8000
Faker
black

Встановлення:
python -m pip install -r requirements.txt

Alembic migrations
Для керування структурою бази даних використовується Alembic.
Ініціалізація:
alembic init alembic

Створення міграції:
alembic revision --autogenerate -m "Create students database tables"

Застосування:
alembic upgrade head

Перевірка:
alembic current

При успішному застосуванні поточна revision має статус:
(head)

Заповнення бази даних
Для генерації тестових даних використовується:
seed.py

Запуск:
python seed.py

Скрипт створює випадкові дані відповідно до умов завдання:
- 3 групи;
- 3–5 викладачів;
- 5–8 предметів;
- 30–50 студентів;
- 10–20 оцінок для кожного студента.
Приклад результату:
Database seeded successfully.
Groups: 3
Teachers: 4
Subjects: 7
Students: 44
Grades: 674

Для даних використовується пакет:
Faker

а всі операції виконуються через SQLAlchemy Session.
SQLAlchemy queries
У файлі:
my_select.py

реалізовано 10 функцій:
select_1
select_2
select_3
select_4
select_5
select_6
select_7
select_8
select_9
select_10

select_1
Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
select_1()


select_2
Знайти студента із найвищим середнім балом з певного предмета.
select_2(subject_id)


select_3
Знайти середній бал у групах з певного предмета.
select_3(subject_id)


select_4
Знайти середній бал на потоці по всій таблиці оцінок.
select_4()


select_5
Знайти курси, які читає певний викладач.
select_5(teacher_id)


select_6
Знайти список студентів у певній групі.
select_6(group_id)


select_7
Знайти оцінки студентів окремої групи з певного предмета.
select_7(group_id, subject_id)


select_8
Знайти середній бал, який ставить певний викладач зі своїх предметів.
select_8(teacher_id)


select_9
Знайти список курсів, які відвідує певний студент.
select_9(student_id)


select_10
Знайти список курсів, які певному студентові читає певний викладач.
select_10(student_id, teacher_id)


Запуск усіх запитів
Для перевірки:
python my_select.py

Приклад результату:
Select 1: [('Andrew Walker', Decimal('87.40')), ...]
Select 2: [('Elizabeth Branch', Decimal('98.00'))]
Select 3: [('CS-101', Decimal('77.44')), ...]
Select 4: 79.80
Select 5: ['Data Science', 'Physics']
Select 6: [...]
Select 7: [...]
Select 8: 79.29
Select 9: [...]
Select 10: ['Data Science', 'Physics']

Таким чином усі 10 обов'язкових SQLAlchemy-запитів протестовано успішно.
Повне відновлення бази
Для видалення таблиць через Alembic:
alembic downgrade base

Повторне створення:
alembic upgrade head

Повторне заповнення:
python seed.py

Перевірка підключення
Пряме підключення через pg8000:
python -c "import pg8000; c=pg8000.connect(user='postgres', password='hw06password', host='127.0.0.1', port=5435, database='postgres'); print('PG8000 DIRECT CONNECTION OK'); c.close()"

Очікуваний результат:
PG8000 DIRECT CONNECTION OK

Перевірка SQLAlchemy:
python -c "from database import engine; c=engine.connect(); print('SQLAlchemy connection OK'); c.close()"

Очікувано:
SQLAlchemy connection OK

Форматування
Код відформатовано за допомогою Black.
python -m black database.py models.py seed.py my_select.py alembic/env.py

Перевірка:
python -m black --check database.py models.py seed.py my_select.py alembic/env.py

Результат
У домашньому завданні реалізовано:
- PostgreSQL у Docker;
- SQLAlchemy ORM;
- п'ять пов'язаних моделей;
- SQLAlchemy relationships;
- Alembic migrations;
- Faker data generation;
- SQLAlchemy sessions;
- 30–50 студентів;
- 3 групи;
- 3–5 викладачів;
- 5–8 предметів;
- до 20 оцінок на студента;
- 10 обов'язкових SQLAlchemy-запитів;
- форматування коду Black.
Основні вимоги домашнього завдання виконано та протестовано.
```
