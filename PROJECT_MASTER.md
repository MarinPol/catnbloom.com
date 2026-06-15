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
- Contains other pages.
- Examples: Cottagecore Cats, Witchy Cats Plants, Seasonal Sets.
- Template: Collection Page.
- Reference Master: `/cottagecore-cats/`
- Schema: CollectionPage.

### 2. MATERIAL
- Standalone page (final destination).
- Examples: C01-001, C01-002, C02-005.
- Template: Product Page.
- Reference Master: `/cottagecore-cats/c01-001/`
- Schema: Product.

**Rule:**
- If page contains materials → **SECTION**.
- If page is the final destination → **MATERIAL**.
- No third page type exists.

## История изменений
| Дата | Файл | Изменение | Зачем |
|:---|:---|:---|:---|
| 2026-06-02 | Инициализация | Зафиксирована структура согласно image_1f53dc.png | Синхронизация с актуальным состоянием |
| 2026-06-02 | cottagecore-cats.md | Синхронизация метаданных с шаблоном collection | Работа автовывода товаров |
| 2026-06-02 | cottagecore-cats.md / index.md | Исправление конфликта путей и разметки | Устранение Liquid-ошибки сборки |
| 2026-06-02 | _config.yml | Аудит конфигурации коллекций | Согласование ключей имен |
| 2026-06-02 | _layouts/collection.html | Переход на динамический доступ site[page.collection_id] | Исправление логики Jekyll |
| 2026-06-02 | _layouts/collection.html | Защита от пустого массива коллекции | Обработка ошибок данных |
| 2026-06-02 | _config.yml | Верификация ключей | Подтверждение cottagecore/witchy |
| 2026-06-02 | _layouts/collection.html | Фильтр default: empty | Стабилизация данных |
| 2026-06-02 | _cottagecore/c01-001.md | Очистка Front Matter | Активация индексации товара |
| 2026-06-03 | _layouts/collection.html | Стандартизация архитектуры (container) | Устранение нестабильности верстки |
| 2026-06-03 | _layouts/collection.html | Рефакторинг структуры | Стабилизация для диагностики меню |
| 2026-06-03 | _includes/header.html | Замена на parentElement.querySelector | Исправление поведения dropdown |
| 2026-06-03 | assets/css/style.css | Унификация z-index и позиционирования | Исправление mobile dropdown |
| 2026-06-03 | assets/css/style.css | Переход на opacity/visibility | Единая модель состояния UI |
| 2026-06-03 | _includes/header.html | Рефакторинг JS-зависимостей | Идентичность меню на всех страницах |
| 2026-06-04 | Mobile dropdown investigation | Тесты на iPhone и браузерах | Подтверждение корректности системы |
| 2026-06-05 | ARCHITECTURE / SECTION / MATERIAL | Принята стратегия опоры на рабочие страницы | Уход от теоретического проектирования |
| 2026-06-05 | SECTION (Collection) | Определение эталона SECTION | Использование опыта коллекции |
| 2026-06-05 | MATERIAL (Product Page) | Определение эталона MATERIAL | Использование геометрии продуктов |
| 2026-06-05 | SECTION ↔ MATERIAL Audit | Сравнительный анализ страниц | Определение общесайтовых компонентов |
| 2026-06-05 | SECTION Development Strategy | Приоритет Collection Page | Фиксация реального стандарта |
| 2026-06-05 | MATERIAL Development Strategy | Точечная ревизия после SECTION | Исключение параллельного рефакторинга |
| 2026-06-05 | Design System Planning | Поэтапная стратегия стандартов | Исключение повторного проектирования |
| 2026-06-05 | Standardization Workflow | Утвержден порядок работ | Единый подход для всех страниц |
| 2026-06-05 | Future Architecture Rule | Формирование стандартов из файлов проекта | Сохранение преемственности |
| 2026-06-05 | _layouts/collection.html | Внедрение breadcrumbs.html | Унификация навигации |
| 2026-06-05 | _layouts/collection.html | Передача collection_name/slug | Восстановление хлебных крошек |
| 2026-06-05 | _includes/breadcrumbs.html | Привязка к collection_name + title | Унификация отображения пути |
| 2026-06-05 | product-bridge.html | Без изменений | Стабилизация продуктового слоя |
| 2026-06-06 | _layouts/collection.html | Унификация с MATERIAL grid | Перенос hero_image в left-block |
| 2026-06-06 | _layouts/collection.html | Интеграция hero_image | Обеспечение единой геометрии |
| 2026-06-06 | collection showcase system | Внедрение двухуровневой выдачи | Showcase slider + Main grid |
| 2026-06-06 | collection showcase stabilization | Исправление логики flex-basis | Корректный viewport для слайдера |
| 2026-06-06 | collection grid image constraint | Нормализация размеров через object-fit | Устранение искажений карточек |
| 2026-06-06 | breadcrumbs system stabilization | Разделение логики по типам layout | Изоляция MATERIAL и SECTION |
| 2026-06-06 | breadcrumbs collection title fix | Привязка к page.hero_title | Исправление fallback-заголовка |
| 2026-06-07 | footer system implementation | Внедрение единого site-footer | Визуальная иерархия блоков |
| 2026-06-07 | breadcrumbs product link fix | Исправление логики URL (slug/id) | Восстановление ссылок на коллекции |
| 2026-06-08 | UI icon system implementation | Интеграция Lucide (buy/cart) | Семантика и фикс SVG-удаления |
| 2026-06-09 | _layouts/collection.html | Восстановление CSS-архитектуры | Устранение инцидента разрушения UI |
| 2026-06-09 | assets/css/style.css | Полное восстановление модулей | Устранение CSS collapse |
| 2026-06-09 | _layouts/collection.html | Улучшение типографики героя | Визуальная иерархия отступов |
| 2026-06-09 | _layouts/collection.html | Интеграция иконок в контент | Читаемость секций коллекции |
| 2026-06-13 | _includes/head.html | Создание SEO Engine | Централизация мета-данных |
| 2026-06-13 | _layouts/collection.html + product-bridge | Рефакторинг под SEO Engine v1.0 | Удаление дублирующей логики |
| 2026-06-13 | _layouts/product-bridge.html | Стабилизация SEO-перехода | Исключение ложных ошибок |
| 2026-06-14 | SEO Engine Audit | Проверка дублей мета-тегов | Оптимизация ресурсов |
| 2026-06-14 | _includes/head.html + product-bridge | SEO Engine cleanup | Удаление дублей и fallback-логика |
| 2026-06-14 | SEO Metadata Audit | Верификация (Canonical/OG/Schema) | Соответствие стандартам 2026 |
| 2026-06-14 | SEO Metadata | Директива noindex,nofollow | Обработка статуса hidden |
| 2026-06-14 | SHARE MODULE | Интеграция универсальных ссылок | Социальный охват |
| 2026-06-14 | SEO Engine Architecture | Завершение перехода на SEO-движок | Финализация системы |

## Текущий этап разработки
- **Завершено:**
    - Инициализация структуры проекта и `_layouts/collection.html`.
    - Внедрение breadcrumbs.html.
    - Завершение перехода на централизованный SEO-движок.
- **В работе:**
    - Финализация шаблонов `_layouts/collection.html` и `_layouts/product-bridge.html`.
- **Запланировано:**
    - Организация структуры смарт-коллекций.
    - Подключение сезонного календаря (SVG).
    - Разработка RSS-канала.
    - Отложенное тестирование Load More (требуется 12-15 товаров).

## Известные ограничения
- Работа ведется строго через GitHub Web Interface.
- Не менять имена файлов без прямого запроса.
- Всегда соблюдать структуру протокола v2.0.
