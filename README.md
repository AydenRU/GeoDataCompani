# GeoDataCompani

Учебный проект для практики с **Pydantic**, **SQLAlchemy**, **Alembic**, **Redis**, **FastAPI** и **PostgreSQL**.  
Сборка и запуск предусмотрены через **Docker / docker-compose**.  

В репозитории присутствуют:  
`app/`, `Dockerfile`, `docker-compose.yaml`, `alembic.ini`, `requirements.txt` и сопутствующие файлы.

---

## Коротко (Overview)

GeoDataCompani — учебный/демонстрационный сервис для работы с геоданными и примера использования современного Python-стека:

- Валидация и модели данных — **Pydantic**  
- ORM и работа с БД — **SQLAlchemy** (+ Alembic для миграций)  
- Кеширование / очередь — **Redis**  
- HTTP API — **FastAPI** (автодокументация: `/docs`, `/redoc`)  
- БД разработки — **PostgreSQL**  
- Контейнеризация — **Docker + docker-compose**

---

## Технологии / стек

- Python (версия указана в `requirements.txt`)  
- FastAPI  
- Pydantic  
- SQLAlchemy  
- Alembic  
- Redis  
- PostgreSQL  
- Docker / docker-compose  

---

## Структура репозитория
/app/ # исходники FastAPI, модели, Pydantic-схемы и т.д.
Dockerfile
docker-compose.yaml # настройка сервисов (Postgres, Redis, web)
alembic.ini
requirements.txt # зависимости
.gitignore
.dockerignore

yaml
Копировать код

---

## Основные возможности

- 📌 **CRUD-операции** над сущностями (компании, адреса, географические объекты)  
- 🔍 Получение списка объектов и детальной информации по `id`  
- ➕ Добавление новых данных через POST-запросы  
- ✏️ Обновление существующих записей  
- ❌ Удаление записей  
- ⚡ Использование Redis для кеширования часто запрашиваемых данных  
- 📊 Автоматическая документация API через Swagger (`/docs`)