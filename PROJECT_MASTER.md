# PROJECT_MASTER.md

## Информация о проекте
- **Название проекта:** CatnBloom Digital Art Studio
- **Цель проекта:** Управление сайтом-портфолио на базе Jekyll и продажа цифровых работ.
- **Технологический стек:** Jekyll, HTML, CSS, Liquid, GitHub Pages.

---

## Структура проекта

- `_cottagecore/` — Markdown-файлы товаров коллекции Cottagecore
- `_witchy/` — Markdown-файлы товаров коллекции Witchy
- `_smart/` — Markdown-файлы помесячных Smart Collections (sc01–sc12)
- `_studio_notes/` — Markdown-файлы статей Studio Notes
- `_includes/` — Компоненты: header, footer, breadcrumbs, head, share-buttons, author-note, smart-wheel
- `_layouts/` — Шаблоны: collection, product-bridge, about, article, studio-notes, smart-home, smart-collection
- `assets/css/style.css` — Глобальные стили сайта
- `assets/images/` — Графические активы
- `assets/components/smart-wheel/` — wheel.js, wheel.css, wheel.svg, PNG-ресурсы
- **Корневые файлы:**
  - `_config.yml` — Конфигурация Jekyll + плагины
  - `CNAME` — Настройка домена
  - `robots.txt` — Индексирование
  - `cottagecore-cats.md` — Индекс коллекции Cottagecore
  - `witchy-cats-plants.md` — Индекс коллекции Witchy
  - `smart.md` — Индекс Smart Collections
  - `studio-notes.md` — Индекс Studio Notes
  - `about.md` — Страница О студии
  - `inventory.html` — Дашборд управления товарами
  - `PROJECT_MASTER.md` — Данный файл

---

## Content Model Lock v1.0

CatnBloom использует только два типа страниц:

### 1. SECTION
Содержит другие страницы.
Примеры: Cottagecore Cats, Witchy Cats Plants, Smart Collections, Studio Notes.
Template: Collection Page / Studio Notes / Smart Home.
Reference Master: `/cottagecore-cats/`
Schema: CollectionPage / Blog.

### 2. MATERIAL
Финальная страница назначения.
Примеры: C01-001, sn01-001, sc01.
Template: product-bridge / article / smart-collection.
Reference Master: `/cottagecore-cats/c01-001/`
Schema: Product / Article.

**Правило:** Страница содержит материалы → SECTION. Страница является конечным пунктом → MATERIAL. Третьего типа нет.

---

## История изменений

| Дата | Файл | Изменение | Зачем |
|:---|:---|:---|:---|
| 2026-06-02 | Инициализация | Зафиксирована структура проекта | Синхронизация с актуальным состоянием |
| 2026-06-02 | cottagecore-cats.md | Синхронизация метаданных с шаблоном collection | Работа автовывода товаров |
| 2026-06-02 | cottagecore-cats.md / index.md | Исправление конфликта путей и разметки | Устранение Liquid-ошибки сборки |
| 2026-06-02 | _config.yml | Аудит конфигурации коллекций | Согласование ключей имен |
| 2026-06-02 | _layouts/collection.html | Переход на динамический доступ site[page.collection_id] | Исправление логики Jekyll |
| 2026-06-02 | _layouts/collection.html | Защита от пустого массива коллекции | Обработка ошибок данных |
| 2026-06-02 | _cottagecore/c01-001.md | Очистка Front Matter | Активация индексации товара |
| 2026-06-03 | _layouts/collection.html | Стандартизация архитектуры (container) | Устранение нестабильности верстки |
| 2026-06-03 | _includes/header.html | Замена на parentElement.querySelector | Исправление поведения dropdown |
| 2026-06-03 | assets/css/style.css | Унификация z-index и позиционирования | Исправление mobile dropdown |
| 2026-06-03 | assets/css/style.css | Переход на opacity/visibility | Единая модель состояния UI |
| 2026-06-04 | Mobile dropdown | Тесты на iPhone и браузерах | Подтверждение корректности системы |
| 2026-06-05 | ARCHITECTURE | Принята стратегия SECTION / MATERIAL | Уход от теоретического проектирования |
| 2026-06-05 | _includes/breadcrumbs.html | Привязка к collection_name + title | Унификация отображения пути |
| 2026-06-06 | _layouts/collection.html | Showcase slider + Main grid | Двухуровневая выдача товаров |
| 2026-06-07 | footer system | Внедрение единого site-footer | Визуальная иерархия блоков |
| 2026-06-08 | UI icon system | Интеграция Lucide (buy/cart) | Семантика и фикс SVG |
| 2026-06-09 | assets/css/style.css | Полное восстановление модулей после CSS collapse | Устранение инцидента разрушения UI |
| 2026-06-13 | _includes/head.html | Создание SEO Engine v1.0 | Централизация мета-данных |
| 2026-06-13 | _layouts/collection.html + product-bridge | Рефакторинг под SEO Engine | Удаление дублирующей логики |
| 2026-06-14 | _includes/head.html | SEO Engine cleanup | Удаление дублей, fallback-логика |
| 2026-06-14 | SEO Metadata | noindex,nofollow для hidden страниц | Управление индексацией |
| 2026-06-14 | SHARE MODULE | Telegram/X/Pinterest/Facebook/Copy link | Социальный охват |
| 2026-06-14 | Content Model Lock v1.0 | Зафиксированы два типа страниц SECTION и MATERIAL | Архитектурный стандарт |
| 2026-06-15 | witchy-cats-plants.md | Создана SECTION №2 Witchy Cats + Plants | Подтверждена масштабируемость Content Model |
| 2026-06-16 | _layouts/collection.html | Удалены заголовки из Showcase и Grid | Визуальная плиточная выдача |
| 2026-06-16 | assets/css/style.css | Mobile showcase refactor (grid mode) | Отключение слайдера на mobile |
| 2026-06-23 | assets/css/style.css | Восстановление после CSS-резета Jun 16 | Возврат .detail-gallery, .buy-button и др. |
| 2026-06-23 | _config.yml | Добавлена коллекция smart | Регистрация Smart Collections |
| 2026-06-23 | _layouts/smart-home.html | Создан layout индекса Smart Collections | Колесо + сетка 12 месяцев |
| 2026-06-23 | _layouts/smart-collection.html | Создан layout помесячных страниц | Поиск продуктов по SKU из двух коллекций |
| 2026-06-23 | smart.md + _smart/sc01–sc12.md | Созданы индекс и 12 помесячных страниц | Smart Collections полностью развёрнуты |
| 2026-06-23 | assets/components/smart-wheel/wheel.js v1.1 | Исправлены URL, навигация window.location.href | Корректные переходы между месяцами |
| 2026-06-23 | assets/components/smart-wheel/wheel.css | Удалены глобальные переопределения body/button | Устранение конфликта с site CSS |
| 2026-06-23 | _includes/breadcrumbs.html | Добавлены кейсы smart-home и smart-collection | Навигационная цепочка Smart Collections |
| 2026-06-23 | _includes/header.html | Добавлена ссылка Smart Collections | Доступ из главного меню |
| 2026-06-23 | assets/components/smart-wheel/wheel.js v1.2 | BUGFIX: (sectorIndex + rotationOffset) % 12 | Устранение смещения навигации колеса |
| 2026-06-23 | _smart/sc01–sc12.md | BUGFIX: SKU uppercase (C01-001) | Liquid where: case-sensitive |
| 2026-06-25 | _layouts/about.html | Создан layout страницы About | Бренд-страница в едином стиле |
| 2026-06-25 | about.md | Создана страница /about/ | Разделы: Studio, What We Make, Artist, FAQ, Find Our Art |
| 2026-06-25 | _layouts/about.html | Статистика 6 карточек 3×2 + shuffle | Перемешивание при каждой загрузке |
| 2026-06-25 | _includes/breadcrumbs.html | Добавлен кейс layout: about | Home / Our Story |
| 2026-06-25 | assets/css/style.css | About Page стили: .about-stats, .about-faq, .faq-divider | Визуальная структура страницы About |
| 2026-06-25 | _config.yml | Добавлена коллекция studio_notes | Регистрация Studio Notes |
| 2026-06-25 | _layouts/studio-notes.html | Создан layout индекса Studio Notes | Сетка статей-карточек |
| 2026-06-25 | _layouts/article.html | Создан layout статьи | Left: hero + Read Also + галерея; Right: контент |
| 2026-06-25 | studio-notes.md + _studio_notes/sn01-001.md | Созданы индекс и пример статьи | Cottagecore — первая публикация |
| 2026-06-25 | _includes/header.html | Добавлена ссылка Studio Notes | Доступ из главного меню |
| 2026-06-25 | _includes/breadcrumbs.html | Добавлены кейсы studio-notes и article | Навигация Studio Notes |
| 2026-06-25 | assets/css/style.css | Article стили: .article-grid, .article-body, .read-also, .font-size-switcher | Визуальная система Studio Notes |
| 2026-06-26 | _includes/head.html | SEO Engine v2.0 | Article/AboutPage/Blog Schema, BreadcrumbList, og:type динамический |
| 2026-06-26 | _includes/author-note.html | Создан авторский блок под статьями | AI Search Protocol: идентификация автора |
| 2026-06-26 | robots.txt | Создан файл индексирования | Allow: / + Sitemap |
| 2026-06-26 | _config.yml | Добавлен плагин jekyll-sitemap | Автогенерация sitemap.xml |
| 2026-06-26 | AI + Google Visibility Protocol v1.0 | Принят редакционный протокол и Style Guide | Стандарты написания статей |
| 2026-06-27 | _layouts/article.html | BUGFIX: lightbox перехватывал ссылки Read Also | Загрузка lightbox только при detail_images |
| 2026-06-27 | _layouts/article.html | Галерея: .article-images → .detail-gallery / .gallery-item | Соответствие мастер-шаблону |
| 2026-06-27 | _layouts/about.html | Фото и галерея сделаны условными | Устранение пустых боксов |
| 2026-06-27 | _layouts/about.html + article.html | Защита от пустых строк в detail_images | img | strip + проверка на "" |
| 2026-06-27 | _studio_notes/sn01-001.md | Удалена пустая строка из detail_images | Устранение пустого блока в галерее |
| 2026-06-28 | assets/css/style.css | body: font-size 16px явно, line-height 1.3 → 1.6 | Читабельность основного текста |
| 2026-06-28 | assets/css/style.css | .icon-title svg: 18px → 24px | Восстановление размера декоративных иконок |
| 2026-06-28 | assets/css/style.css | h3: 1.1rem → 1.15rem + line-height 1.4 | Улучшение заголовков секций |
| 2026-06-28 | assets/css/style.css | .article-body: line-height 1.8, font-size 1.05rem | Читабельность длинных текстов |
| 2026-06-28 | assets/css/style.css | .about-section p: font-size 1rem, line-height 1.7 | Читабельность страницы О нас |
| 2026-06-28 | assets/css/style.css | .meta-date: margin-bottom → 0 | Выравнивание даты и рубрики на одной линии |

---

## Текущее состояние системы

### Завершено
- Две основные коллекции: Cottagecore Cats, Witchy Cats + Plants
- SEO Engine v2.0: Schema.org, OG, Canonical, BreadcrumbList, robots.txt, sitemap
- Smart Collections: колесо, 12 месяцев, навигация
- Studio Notes: layout статьи, Read Also, font-size switcher, author block
- About страница: статистика, галерея, FAQ, Find Our Art
- AI + Google Visibility Protocol v1.0 и Editorial Style Guide
- Глобальная типографика и иконки приведены к стандарту

### Активные ограничения
- Работа строго через GitHub Web Interface
- Не переименовывать файлы без прямого запроса
- Соблюдать протокол v2.0 в каждой сессии
- Всегда запрашивать актуальные файлы перед правками

---

## Запланировано — Очередь задач

### Приоритет 1 — Инфраструктура

| Задача | Статус | Примечание |
|:---|:---|:---|
| Contact страница + форма | ⏳ | Formspree → Gmail. Поля: Имя, Email, Тема, Сообщение |
| RSS-канал | ⏳ | Плагин jekyll-feed, одна строка в _config.yml |
| Подписка на рассылку | ⏳ | Mailchimp или ConvertKit embed в футере и на главной |

### Приоритет 2 — Главная страница

| Задача | Статус | Примечание |
|:---|:---|:---|
| index.md / home layout | ⏳ | Последние дизайны + последние статьи Studio Notes |
| Динамический баннер | ⏳ | Полная ширина, концепция уточняется |

### Приоритет 3 — Расширение функционала

| Задача | Статус | Примечание |
|:---|:---|:---|
| Google Custom Search | ⏳ | Виджет поиска, данные в Search Console |
| Load More (product grid) | ⏳ | Отложено до 12+ карточек в коллекции |
| Wheel overlay PNG | ⏳ | Механика готова, нужны PNG-файлы под каждый месяц |

### Постоянные задачи (контент)

| Задача | Статус | Примечание |
|:---|:---|:---|
| Новые карточки товаров | 🔄 | Cottagecore + Witchy коллекции |
| Статьи Studio Notes | 🔄 | По редакционному протоколу v1.0 |
| Тексты sc01–sc12 | 🔄 | Заменить рыбу на реальный авторский контент |
| Обновление Smart Collections | 🔄 | Подборки по месяцам по мере роста каталога |

### Проверочный чек-лист (технический)

| Задача | Статус |
|:---|:---|
| robots.txt проверить через Google Search Console | ⏳ |
| sitemap.xml убедиться что генерируется: catnbloom.com/sitemap.xml | ⏳ |
| Google Search Console подключить и отправить sitemap | ⏳ |
| Rich Results Test прогнать product-bridge и article страницы | ⏳ |
| OG image проверить через opengraph.xyz | ⏳ |
| default_og.jpg убедиться что файл существует | ⏳ |
| Lightbox проверить на продуктовой и в статье | ✅ |
| Mobile: меню, showcase, карточки статей | ⏳ |
