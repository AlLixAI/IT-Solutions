FROM python:3.11-slim

# Создаем рабочий каталог
WORKDIR /fastapi_app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

EXPOSE 8000

# Запускаем FastAPI приложение с помощью uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
