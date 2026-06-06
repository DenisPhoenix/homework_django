# Домашняя работа. 22 Знакомство с Django

## Описание:

Создание проекта интернет-магазина с использование фреймворка Django:

1. Подключить PostgreSQL к проекту
2. Создать и настроить модели Product и Category
3. Перенести их в базу данных с помощью миграций
4. Зарегистрировать и настроить модели в админке
5. Наполнить базу данных через Django shell
6. Создать фикстуры для моделей и реализовать кастомную команду для добавления тестовых данных.

## Установка:

1. Установить основных зависимостей: "django", "python-dotenv", "psycopg2"

2. Установить дополнительных зависимостей: "flake8", "isort", "mypy", "black"

3. Настройка зависимостей:

```
# pyproject.toml
[tool.black]
line-length = 79
target-version = ['py314']
exclude = '''
(
  /(
      \.git

    | \.venv
    | build
    | dist
  )/
)
'''

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = "venv"

# .flake8
[flake8]
max-line-length = 119
exclude = .git, __pycache__, .venv
```

## Структура проекта

+ `config/`: Настройки проекта

+ `catalog/`: Приложение Каталог

+ `static/`: Статические данные

+ `manage.py`: Запуска команд Django

+ `.env_example`: Пример переменных окружения

+ `.gitignore`: Игнорируемые файлы для Git

+ `pyproject.toml`: Файл c зависимостями проекта

+ `.flake8`: Настройки линтера flake8

+ `README.md`: Файл с описанием проекта