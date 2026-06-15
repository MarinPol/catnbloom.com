# PROJECT_MASTER.md

## Информация о проекте
- **Название проекта:** CatnBloom Digital Art Studio
- **Цель проекта:** Управление сайтом-портфолио на базе Jekyll и продажа цифровых работ.
- **Технологический стек:** Jekyll, HTML, CSS, Liquid, GitHub Pages.

## Структура проекта
- `_cottagecore/`: Содержит Markdown-файлы товаров коллекции Cottagecore.
- `_includes/`: Компоненты для переиспользования (хедер, хлебные крошки).
- `_layouts/`: Базовые шаблоны страниц (коллекции, карточки товаров).
- `_witchy/`: Содержит Markdown-файлы товаров коллекции Witchy.
- `assets/css/`: Файл `style.css` с глобальными стилями сайта.
- `assets/images/`:
    - `products/`: Изображения товаров для галерей.
    - `ctbl-icon.png`, `header-bg.jpg`, `header-mobile.jpg`: Графические элементы интерфейса.
- **Корневые файлы:**
    - `CNAME`: Настройка доменного имени.
    - `_config.yml`: Конфигурация проекта Jekyll.
    - `cottagecore-cats.md`: Индексная страница коллекции Cottagecore.
    - `inventory.html`: Дашборд для управления статусами товаров.
    - `PROJECT_MASTER.md`: Данный файл управления структурой.
    - `README.md`: Документация репозитория.

## Content Model Lock
CatnBloom uses only two page types:

### 1. SECTION
- **Contains other pages.**
- **Examples:** Cottagecore Cats, Witchy Cats Plants, Seasonal Sets.
- **Template:** Collection Page.
- **Reference Master:** `/cottagecore-cats/`
- **Schema:** CollectionPage.

### 2. MATERIAL
- **Standalone page (final destination).**
- **Examples:** C01-001, C01-002, C02-005.
- **Template:** Product Page.
- **Reference Master:** `/cottagecore-cats/c01-001/`
- **Schema:** Product.

**Rule:**
- If page contains materials → **SECTION**.
- If page is the final destination → **MATERIAL**.
- No third page type exists.

## История изменений
| Дата | Файл | Изменение | Зачем |
| :--- | :--- | :--- | :--- |
| 2026-06-02 | Инициализация | Создан PROJECT_MASTER.md | Фиксация архитектуры |
| 2026-06-14 | Content Model | Внедрена модель SECTION/MATERIAL | Упорядочивание контента |

## Текущий этап разработки
- **Завершено:**
    - Инициализация структуры проекта и `PROJECT_MASTER.md`.
    - Разработка шаблона `_layouts/collection.html`.
- **В работе:**
    - Финализация структуры контента согласно Content Model.
- **Запланировано:**
    - Подключение сезонного календаря (SVG).

## Известные ограничения
- Работа ведется строго через GitHub Web Interface.
- Не менять имена файлов без прямого запроса.
- Всегда соблюдать структуру протокола v2.0.
