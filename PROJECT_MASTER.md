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
| 2026-06-02 | Инициализация | Зафиксирована структура | Синхронизация |
| 2026-06-02 | cottagecore-cats.md | Синхронизация метаданных | Работа автовывода |
| 2026-06-02 | cottagecore-cats.md | Исправление конфликта путей | Устранение Liquid-ошибки |
| 2026-06-02 | _config.yml | Аудит конфигурации | Согласование ключей |
| 2026-06-02 | _layouts/collection.html | Динамический доступ site[id] | Исправление логики |
| 2026-06-02 | _layouts/collection.html | Защита от пустого массива | Обработка ошибок |
| 2026-06-02 | _config.yml | Верификация ключей | Подтверждение типов |
| 2026-06-02 | _layouts/collection.html | Фильтр default: empty | Стабилизация данных |
| 2026-06-02 | _cottagecore/c01-001.md | Очистка Front Matter | Индексация товара |
| 2026-06-03 | _layouts/collection.html | Стандартизация архитектуры | Устранение нестабильности |
| 2026-06-03 | _layouts/collection.html | Рефакторинг структуры | Диагностика меню |
| 2026-06-03 | _includes/header.html | JS parentElement.querySelector | Исправление dropdown |
| 2026-06-03 | assets/css/style.css | Унификация z-index | Фикс mobile dropdown |
| 2026-06-03 | assets/css/style.css | Переход на opacity/visibility | Единая модель UI |
| 2026-06-03 | _includes/header.html | Рефакторинг JS-зависимостей | Идентичность меню |
| 2026-06-04 | Mobile investigation | Тесты на iPhone | Подтверждение корректности |
| 2026-06-05 | ARCHITECTURE | Strategy: SECTION / MATERIAL | Уход от теории |
| 2026-06-05 | SECTION / MATERIAL | Определение эталонов | Стандартизация |
| 2026-06-05 | Audit | Сравнительный анализ страниц | Общесайтовые компоненты |
| 2026-06-05 | Strategy | Приоритет Collection Page | Фиксация стандарта |
| 2026-06-05 | Workflow | Утвержден порядок работ | Единый подход |
| 2026-06-05 | _layouts/collection.html | Внедрение breadcrumbs.html | Навигация |
| 2026-06-05 | _includes/breadcrumbs.html | Привязка к collection_name | Отображение пути |
| 2026-06-06 | _layouts/collection.html | Унификация с MATERIAL grid | Геометрия блоков |
| 2026-06-06 | collection showcase | Двухуровневая выдача | Showcase + Main grid |
| 2026-06-06 | collection grid | object-fit constraint | Устранение искажений |
| 2026-06-06 | breadcrumbs | Изоляция MATERIAL и SECTION | Исправление логики |
| 2026-06-07 | footer system | Внедрение site-footer | Визуальная иерархия |
| 2026-06-07 | breadcrumbs | Исправление логики URL | Восстановление ссылок |
| 2026-06-08 | UI icon system | Интеграция Lucide | Семантика и SVG |
| 2026-06-09 | _layouts/collection.html | Восстановление CSS | Фикс UI collapse |
| 2026-06-09 | _layouts/collection.html | Типографика героя | Иерархия отступов |
| 2026-06-13 | _includes/head.html | Создание SEO Engine | Мета-данные |
| 2026-06-13 | SEO Engine v1.0 | Рефакторинг шаблонов | Удаление дублей |
| 2026-06-14 | SEO Metadata Audit | Верификация (OG/Schema) | Соответствие 2026 |
| 2026-06-14 | SEO Metadata | Директива noindex | Обработка hidden status |
| 2026-06-14 | SHARE MODULE | Интеграция ссылок | Социальный охват |
| 2026-06-14 | SEO Engine | Финализация архитектуры | Интеллектуальный fallback |

## Текущий этап разработки
- **Завершено:**
    - Инициализация архитектуры и SEO Engine.
    - Внедрение breadcrumbs и модуля SHARE.
- **В работе:**
    - Финализация шаблонов `_layouts/collection.html` и `_layouts/product-bridge.html`.
    - Тестирование Load More (отложено из-за объема контента).
- **Запланировано:**
    - Организация смарт-коллекций.
    - Подключение сезонного календаря (SVG).
    - Разработка RSS-канала.

## Известные ограничения
- Работа ведется строго через GitHub Web Interface.
- Не менять имена файлов без прямого запроса.
- Всегда соблюдать структуру протокола v2.0.
