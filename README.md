# Домашняя работа. 22 Знакомство с Django

## Описание:

Создание проекта интернет-магазина с использование фреймворка Django.

## Установка:

1. Установить основных зависимостей: "django", "python-dotenv"

2. Установить дополнительных зависимостей: "flake8", "isort", "mypy", "black"

3. Настройка зависимостей:

```
# pyproject.toml
[tool.black]
line-length = 119
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

+ `src/`: Исходный код

+ `tests/`: Тесты проекта

+ `.gitignore`: Игнорируемые файлы для Git

+ `pyproject.toml`: Файл c зависимостями проекта

+ `.flake8`: Настройки линтера flake8

+ `README.md`: Файл с описанием проекта