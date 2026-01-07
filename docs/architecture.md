# Архитектура проекта

Проект построен на фреймворке **Django** и следует паттерну MVT (Model-View-Template).

## Структура приложений

Проект разделен на несколько Django-приложений (apps) для логического разделения функциональности:

### 1. `users`

Отвечает за управление пользователями и аутентификацию.

- **Models**:
  - `User`: Кастомная модель пользователя, наследуется от `AbstractUser`.
    - `is_student`: Булево поле, роль студента.
    - `is_author`: Булево поле, роль автора.
    - `avatar`: Изображение профиля (хранится в Cloudinary).

### 2. `courses`

Основное приложение для бизнес-логики курсов.

- **Models**:

  - `Course`: Модель курса.
    - `title`, `description`: Основная информация.
    - `cover`: Обложка курса (Cloudinary).
    - `author`: ForeignKey на User.
    - `students`: ManyToManyField на User (список записанных студентов).
    - `status`: draft/moderation/published.
  - `Chapter`: Модель главы курса.
    - `course`: ForeignKey на Course.
    - `title`, `description`: Содержание главы.
    - `order`: Порядок отображения.
  - `AuthorApplication`: Заявка пользователя на получение прав автора.

- **Views**:
  - `CourseListView`: Список опубликованных курсов.
  - `CourseDetailView`: Детальный просмотр курса со списком глав.
  - `CourseCreateView`: Создание курса.
  - `EnrollCourseView`: Запись студента на курс.

## Стек технологий

- **Backend**: Python, Django
- **Database**: SQLite (для разработки), легко заменяется на PostgreSQL.
- **Frontend**: Django Templates, CSS (BEM методология), HTML5.
- **File Storage**: Cloudinary (для хранения медиа-файлов в облаке).
- **Styling**: Кастомный CSS, вдохновленный дизайном Stepik.

## Структура папок

```text
lms-app/
├── config/                 # Конфигурация Django проекта (settings, urls, wsgi)
├── users/                  # App: Пользователи
├── courses/                # App: Курсы и заявки
├── static/                 # Статические файлы (CSS)
│   └── css/                # Модульная CSS структура (blocks, layout, variables)
├── templates/              # HTML Шаблоны
│   ├── base.html           # Базовый шаблон
│   ├── courses/            # Шаблоны курсов
│   ├── registration/       # Шаблоны авторизации
│   └── users/              # Шаблоны профиля
├── media/                  # Медиа файлы (локально, если не использовать Cloudinary)
├── docs/                   # Документация
├── requirements.txt        # Зависимости Python
├── manage.py               # Утилита управления Django
└── .env                    # Переменные окружения (не в git)
```
