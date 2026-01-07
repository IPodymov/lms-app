# Установка и запуск

## Требования

- Python 3.10+
- pip
- Cloudinary аккаунт (для загрузки изображений)

## Шаги по установке

1. **Клонируйте репозиторий:**

   ```bash
   git clone <repository_url>
   cd lms-app
   ```

2. **Создайте виртуальное окружение:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # На macOS/Linux
   # venv\Scripts\activate   # На Windows
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка переменных окружения:**
   Создайте файл `.env` в корне проекта и добавьте следующие переменные:

   ```env
   # Ссылка подключения к Cloudinary (можно взять в Dashboard)
   CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>

   # Секретный ключ Django (опционально, если вынесете в .env)
   # SECRET_KEY=your_secret_key
   ```

5. **Примените миграции:**

   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя (для админки):**

   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

Проект будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
