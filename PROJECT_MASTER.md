PROJECT PASSPORT v2.0

Финальный регламент взаимодействия (AI + GitHub Web Interface)

1. ИСТОЧНИКИ ИСТИНЫ (Приоритет)

PROJECT_MASTER.md (Архитектура и журнал)

SYSTEM LOG (История конкретного файла)

Текущий код файла (предоставленный пользователем)

Память ИИ вторична и не является источником истины.

2. ПРАВИЛА РАБОТЫ

GitHub Web Interface Only: Никаких CLI/Bash, если не запрошено.

Файл-за-файлом: Редактируем только один файл за раз.

Полный файл: ИИ обязан возвращать код целиком, готовый к вставке. Фрагменты запрещены.

Запреты: Не переименовывать файлы, не менять пути и ссылки без прямого разрешения.

Защита от галлюцинаций: Если ИИ не уверен, он обязан запросить актуальный код файла.

3. АЛГОРИТМ ВЗАИМОДЕЙСТВИЯ (Каждую сессию)

Пользователь присылает сообщение:

Работаем по протоколу v2.0. Файл [ИМЯ]. Вот код: [КОД]. Вот PROJECT_MASTER.md: [КОД]. Задача: [ЗАДАЧА].

ИИ обязан:

Найти и прочитать SYSTEM LOG внутри файла.

Написать БЛОК ПОНИМАНИЯ (пересказать связи и суть задачи).

Выдать ПОЛНЫЙ ФАЙЛ с правками.

Выдать ЧЕК-ЛИСТ ПРОВЕРКИ.

Выдать MASTER LOG ENTRY (строку для PROJECT_MASTER.md).

4. КОМАНДА «СИНХРОНИЗАЦИЯ»

Если ИИ путает контекст: пользователь пишет «СИНХРОНИЗАЦИЯ». ИИ обязан остановиться, перечитать SYSTEM LOG и PROJECT_MASTER.md и пересказать текущее состояние проекта без написания кода.



PROJECT_MASTER.md

## Информация о проекте

- **Название проекта:** CatnBloom Digital Art Studio

- **Цель проекта:** Управление сайтом-портфолио на базе Jekyll и продажа цифровых работ.

- **Технологический стек:** Jekyll, HTML, CSS, Liquid, GitHub Pages.

Структура проекта

_cottagecore/: Markdown-файлы товаров коллекции Cottagecore.

_includes/: Компоненты для переиспользования (хедер, футер, хлебные крошки, smart-wheel.html).

_layouts/: Базовые шаблоны страниц (collection.html, product-bridge.html, smart-collection.html).

_smart/: Markdown-файлы для системы Smart Collection (sc01.md).

_witchy/: Markdown-файлы товаров коллекции Witchy.

assets/:

components/smart-wheel/: Исходные данные для навигационного колеса.

css/: Глобальные стили проекта (style.css).

images/: Графические активы проекта.

Корневые файлы:

_config.yml: Конфигурация проекта.

CNAME: Настройка домена.

cottagecore-cats.md: Индексная страница коллекции Cottagecore.

inventory.html: Дашборд управления товарами.

PROJECT_MASTER.md: Файл управления структурой.

README.md: Документация.

witchy-cats-plants.md: Индексная страница коллекции Witchy.

CONTENT MODEL LOCK

CatnBloom uses only two page types.

1. SECTION

Contains other pages.

Examples:

Cottagecore Cats

Witchy Cats Plants

Seasonal Sets

Template:Collection Page

Reference Master:/cottagecore-cats/

Schema:CollectionPage

2. MATERIAL

Standalone page.

Examples:

C01-001

C01-002

C02-005

Template:Product Page

Reference Master:/cottagecore-cats/c01-001/

Schema:Product

Rule

If page contains materials → SECTION.

If page is the final destination → MATERIAL.

No third page type exists.

Current Masters:

SECTION → Cottagecore Cats Collection

MATERIAL → C01-001 Product Page

================

## История изменений

[Дата] | Файл | Изменение | Зачем

--- | --- | --- | ---

История изменений

2026-06-02 | Инициализация | Зафиксирована структура согласно image_1f53dc.png | Синхронизация с актуальным состоянием

2026-06-02 | cottagecore-cats.md | Синхронизация метаданных с шаблоном collection | Работа автовывода товаров

2026-06-02 | cottagecore-cats.md / index.md | Исправление конфликта путей и разметки | Устранение Liquid-ошибки сборки

2026-06-02 | _config.yml | Аудит конфигурации коллекций | Согласование ключей имен

2026-06-02 | _layouts/collection.html | Переход на динамический доступ site[page.collection_id] | Исправление логики Jekyll

2026-06-02 | _layouts/collection.html | Защита от пустого массива коллекции | Обработка ошибок данных

2026-06-02 | _config.yml | Верификация ключей | Подтверждение cottagecore/witchy

2026-06-02 | _layouts/collection.html | Фильтр default: empty | Стабилизация данных

2026-06-02 | _cottagecore/c01-001.md | Очистка Front Matter | Активация индексации товара

2026-06-03 | _layouts/collection.html | Стандартизация архитектуры (container) | Устранение нестабильности верстки

2026-06-03 | _layouts/collection.html | Рефакторинг структуры | Стабилизация для диагностики меню

2026-06-03 | _includes/header.html | Замена на parentElement.querySelector | Исправление поведения dropdown

2026-06-03 | assets/css/style.css | Унификация z-index и позиционирования | Исправление mobile dropdown

2026-06-03 | assets/css/style.css | Переход на opacity/visibility | Единая модель состояния UI

2026-06-03 | _includes/header.html | Рефакторинг JS-зависимостей | Идентичность меню на всех страницах

2026-06-04 | Mobile dropdown investigation | Тесты на iPhone и браузерах | Подтверждение корректности системы

2026-06-05 | ARCHITECTURE / SECTION / MATERIAL | Принята стратегия опоры на рабочие страницы | Уход от теоретического проектирования

2026-06-05 | SECTION (Collection) | Определение эталона SECTION | Использование опыта коллекции

2026-06-05 | MATERIAL (Product Page) | Определение эталона MATERIAL | Использование геометрии продуктов

2026-06-05 | SECTION ↔ MATERIAL Audit | Сравнительный анализ страниц | Определение общесайтовых компонентов

2026-06-05 | SECTION Development Strategy | Приоритет Collection Page | Фиксация реального стандарта

2026-06-05 | MATERIAL Development Strategy | Точечная ревизия после SECTION | Исключение параллельного рефакторинга

2026-06-05 | Design System Planning | Поэтапная стратегия стандартов | Исключение повторного проектирования

2026-06-05 | Standardization Workflow | Утвержден порядок работ | Единый подход для всех страниц

2026-06-05 | Future Architecture Rule | Формирование стандартов из файлов проекта | Сохранение преемственности

2026-06-05 | _layouts/collection.html | Внедрение breadcrumbs.html | Унификация навигации

2026-06-05 | _layouts/collection.html | Передача collection_name/slug | Восстановление хлебных крошек

2026-06-05 | _includes/breadcrumbs.html | Привязка к collection_name + title | Унификация отображения пути

2026-06-05 | product-bridge.html | Без изменений | Стабилизация продуктового слоя

2026-06-06 | _layouts/collection.html | Унификация с MATERIAL grid | Перенос hero_image в left-block

2026-06-06 | _layouts/collection.html | Интеграция hero_image | Обеспечение единой геометрии

2026-06-06 | collection showcase system | Внедрение двухуровневой выдачи | Showcase slider + Main grid

2026-06-06 | collection showcase stabilization | Исправление логики flex-basis | Корректный viewport для слайдера

2026-06-06 | collection grid image constraint | Нормализация размеров через object-fit | Устранение искажений карточек

2026-06-06 | breadcrumbs system stabilization | Разделение логики по типам layout | Изоляция MATERIAL и SECTION

2026-06-06 | breadcrumbs collection title fix | Привязка к page.hero_title | Исправление fallback-заголовка

2026-06-07 | footer system implementation | Внедрение единого site-footer | Визуальная иерархия блоков

2026-06-07 | breadcrumbs product link fix | Исправление логики URL (slug/id) | Восстановление ссылок на коллекции

2026-06-08 | UI icon system implementation | Интеграция Lucide (buy/cart) | Семантика и фикс SVG-удаления

2026-06-09 | _layouts/collection.html | Восстановление CSS-архитектуры | Устранение инцидента разрушения UI

2026-06-09 | assets/css/style.css | Полное восстановление модулей | Устранение CSS collapse

2026-06-09 | _layouts/collection.html | Улучшение типографики героя | Визуальная иерархия отступов

2026-06-09 | _layouts/collection.html | Интеграция иконок в контент | Читаемость секций коллекции

2026-06-13 | _includes/head.html | Создание SEO Engine | Централизация мета-данных

2026-06-13 | _layouts/collection.html + product-bridge | Рефакторинг под SEO Engine v1.0 | Удаление дублирующей логики

2026-06-13 | _layouts/product-bridge.html | Стабилизация SEO-перехода | Исключение ложных ошибок

2026-06-14 | SEO Engine Architecture | Завершение перехода на централизованный SEO-движок | Внедрение автоматического fallback-рендеринга мета-данных, устранение дублей в шаблонах и настройка интеллектуального управления индексацией через Front Matter.

2026-06-14 | SEO Engine Audit | Проверка дублей мета-тегов | Оптимизация ресурсов

2026-06-14 | _includes/head.html + product-bridge | SEO Engine cleanup | Удаление дублей и fallback-логика

2026-06-14 | SEO Metadata Audit | Верификация (Canonical/OG/Schema) | Соответствие стандартам 2026

2026-06-14 | SEO Metadata | Директива noindex,nofollow | Добавлена условная meta robots директива noindex,nofollow для страниц со статусом hidden через page.status в head.html.

2026-06-14 | SHARE MODULE | UI-компонент с универсальными ссылками на Telegram/X/Pinterest/Facebook/Copy link) - fixed placement on product (after collection description via include) and collection pages, updated CSS + Pinterest behavior aligned to OG metadata (no custom crop logic applied).

2026-06-14 | Content Model Lock v1.0 | Fixed CatnBloom architecture to two document types only — SECTION (Collection Page template, reference: Cottagecore Cats) and MATERIAL (Product Page template, reference: C01-001); all future pages must inherit from one of these locked master templates.

2026-06-15 | witchy-cats-plants.md | Создана и протестирована SECTION №2 (Witchy Cats + Plants) на базе SECTION Master (Cottagecore Cats) | Подтверждена работоспособность и масштабируемость Content Model Lock v1.0

2026-06-16 | _layouts/collection.html | Удалены заголовки товаров из Showcase и Product Grid | SECTION Master переведен на визуальную плиточную выдачу без дублирования ссылочных заголовков

2026-06-16 | _layouts/collection.html | Добавлен title attribute в ссылки Showcase и Grid | Восстановлена полная структура файла, сохранена плиточная визуальная модель SECTION без текстовых заголовков

2026-06-16 | _assets/css/style.css | Mobile showcase refactor (grid mode) | Отключение слайдер-логики на mobile: скрытие navigation arrows (.showcase-btn), замена flex/transform поведения на grid (2 колонки), фиксация 3 рядов без прокрутки, сохранение desktop slider-архитектуры без изменений, устранение конфликтов viewport/overflow в mobile breakpoint

2026-06-23 | CSS Восстановление | Обнаружен CSS-резет от Jun 16, который удалил блоки кнопок, галереи и UI-элементов. Восстановлены .detail-gallery (flex-версия из Jun 14), .buy-button, .switch-tab, .platform-switcher, .author-note-box, .extra-links-section, .extra-link, .tags-container, .product-tag, .meta-date. Мобильный fix для showcase сохранён. Файл assets/css/style.css заменён финальной версией.

2026-06-23 | CSS Галерея | Отсутствие стилей .detail-gallery приводило к расползанию фото на продуктовых страницах — блок не пережил резет Jun 16 и не был замечен сразу из-за кэша Cloudflare.

2026-06-23 | Smart Collection Module (Wheel Integration) | Добавлен новый раздел Smart Collection как отдельный layout _layouts/smart-collection.html, использующий интерактивный wheel-модуль вместо hero-изображения. Интегрирован компонент smart-wheel.html с SVG-колесом (12-секторная навигация по месяцам), overlay-кликабельными секторами и JS-логикой фиксированного поворота (0° = January, шаг 30°). Реализовано разделение слоёв: фон сцены, SVG wheel, UI overlay (marker + optional assets), с изоляцией от core-collection layout. Подготовлена структура для подключения monthly MD-карточек (sc01–sc12) через smart-коллекцию без влияния на основную систему коллекций.

2026-06-23 | _config.yml | Добавлена коллекция smart (output: true, permalink /smart/:path/, default layout smart-collection) | Регистрация Smart Collections как полноценной Jekyll-коллекции

2026-06-23 | _layouts/smart-home.html | Создан новый layout для индексной страницы Smart Collections | Отображение колеса в нейтральной позиции + сетка 12 месяцев из site.smart

2026-06-23 | _layouts/smart-collection.html | Создан и доработан layout для помесячных страниц | Поиск продуктов по SKU из обеих коллекций (cottagecore + witchy), Showcase + Grid, предварительный поворот колеса к текущему месяцу

2026-06-23 | smart.md | Создана корневая страница раздела /smart/ | Входная точка Smart Collections с описанием и навигацией по месяцам

2026-06-23 | _smart/sc01.md–sc12.md | Созданы все 12 помесячных страниц | sc01 (январь) — полный контент, sc02–sc12 — тематические тексты-рыбы для последующей замены автором

2026-06-23 | assets/components/smart-wheel/wheel.js v1.1 | Исправлены URL месяцев (example.com → /smart/sc01/–sc12/), навигация заменена с window.open+reload на window.location.href | Корректные переходы между разделами в том же табе

2026-06-23 | assets/components/smart-wheel/wheel.css | Удалены глобальные переопределения body, button, .panel | Устранение конфликта с site CSS — фон сайта перестал становиться чёрным при подключении компонента

2026-06-23 | _includes/breadcrumbs.html | Добавлена обработка layout smart-home (Home / Smart Collections) и smart-collection (Home / Smart Collections / Месяц) | Единообразная навигационная цепочка для нового раздела

2026-06-23 | _includes/header.html | Добавлена ссылка Smart Collections в основную навигацию | Доступ к разделу из главного меню сайта

2026-06-23 | assets/css/style.css | Добавлен блок .smart-months-grid — сетка 3 колонки (2 на mobile) для карточек месяцев на индексе | Визуальная структура индексной страницы Smart Collections

2026-06-23 | assets/components/smart-wheel/wheel.js v1.2 | BUGFIX: секторы SVG-оверлея статичны, колесо вращается — при клике реальный месяц вычисляется как (sectorIndex + rotationOffset) % 12 | Устранение смещения навигации на предповёрнутом колесе (Декабрь→клик Март открывал Апрель и т.д.)

2026-06-23 | _smart/sc01.md–sc12.md | BUGFIX: SKU в списке products указывались строчными (c01-001), тогда как в карточках товаров поле sku: uppercase (C01-001) — Liquid where: case-sensitive, продукты не находились и не рендерились | Исправлено на заглавные во всех 12 файлах

2026-06-25 | _layouts/about.html | Создан новый layout страницы About на базе product-bridge (две колонки) | Бренд-страница в едином стиле с остальным сайтом

2026-06-25 | about.md | Создана страница /about/ с текстами коллеги | Разделы: The Studio, What We Make, The Artist, FAQ, Find Our Art

2026-06-25 | _includes/breadcrumbs.html | Добавлен кейс layout: about | Хлебные крошки: Home / Our Story

2026-06-25 | _includes/header.html | Ссылка Our Story уже присутствовала — изменений не потребовалось | Подтверждена корректность навигации

2026-06-25 | about.md + _layouts/about.html | Обновлены тексты всех секций по редакции коллеги | Финальная версия контента страницы

2026-06-25 | _layouts/about.html | Статистика переработана: 6 карточек 3×2 с текстовыми фразами вместо цифр | Cats & Plants / Cottagecore & Botanicals / Tarot & Witchy / Creative Practice since 2020 / Made for Wear / Human-Created

2026-06-25 | _layouts/about.html | Добавлен shuffle карточек статистики (алгоритм Фишера-Йейтса) | Карточки перемешиваются в случайном порядке при каждой загрузке страницы

2026-06-25 | _layouts/about.html | Добавлена галерея под главным фото (detail_images) | Единообразие с продуктовыми страницами

2026-06-25 | _layouts/about.html | Секция Find Our Art переведена на кнопки-переключатели Apparel / Stickers & Notebooks | Единый стиль с product-bridge

2026-06-25 | assets/css/style.css | Добавлены стили About Page: .about-stats (grid 3×2), .about-stat, .about-section, .about-faq, .faq-item, .faq-divider | Визуальная структура страницы About

2026-06-25 | assets/css/style.css | .buy-button: display inline-flex → flex + width 100% | Исправлено: кнопка Browse занимала только половину ширины на странице About

2026-06-25 | Studio Notes Architecture | Принято название раздела Studio Notes, утверждена архитектура ARTICLE как производного от MATERIAL | Единый каркас left/right без изобретения третьей геометрии

2026-06-25 | _config.yml | Добавлена коллекция studio_notes (output: true, permalink /studio-notes/:path/, default layout article) | Регистрация Studio Notes как Jekyll-коллекции

2026-06-25 | _layouts/studio-notes.html | Создан layout индексной страницы раздела (на базе collection.html) | Отображение сетки статей с карточками: изображение, категория, заголовок, excerpt, дата

2026-06-25 | _layouts/article.html | Создан layout статьи (на базе product-bridge.html) | Left: hero image + Read Also + доп. изображения; Right: категория, дата, h1, excerpt, {{ content }}, теги, share

2026-06-25 | studio-notes.md | Создана индексная страница раздела /studio-notes/ | Входная точка Studio Notes с описанием раздела

2026-06-25 | _studio_notes/sn01-001.md | Создан пример статьи — Why Cottagecore Never Really Goes Away | Демонстрация структуры: YAML-шапка + Markdown-тело статьи с заголовками и абзацами

2026-06-25 | _includes/header.html | Добавлена ссылка Studio Notes в основную навигацию | Доступ к разделу из главного меню

2026-06-25 | _includes/breadcrumbs.html | Добавлены кейсы studio-notes (Home / Studio Notes) и article (Home / Studio Notes / Заголовок) | Полная навигационная цепочка для нового раздела

2026-06-25 | assets/css/style.css | Добавлены блоки: .article-grid, .article-card, .article-category, .article-meta-top, .article-body, .article-read-also, .read-also-item, .article-images | Визуальная система Studio Notes

2026-06-26 | _includes/head.html | SEO Engine v2.0 — расширение Schema.org покрытия | Добавлены: Article Schema (headline, author, publisher, datePublished, dateModified) для layout article; AboutPage Schema для layout about; Blog Schema для layout studio-notes; Brand + SKU + Offers + dateModified в Product Schema; BreadcrumbList Schema универсально для всех типов страниц; og:type теперь динамический (article / product / website по layout)

2026-06-26 | _includes/author-note.html | Создан новый include — авторский блок под статьями | "Written by CatnBloom Studio" с ссылкой на /about/ — требование AI Search Protocol: каждая статья должна идентифицировать реального автора

2026-06-26 | _layouts/article.html | Интеграция author-note.html | Авторский блок добавлен между тегами и share-buttons в правом блоке

2026-06-26 | robots.txt | Создан новый файл в корне репозитория | User-agent: * Allow: / + ссылка на sitemap.xml — обязательный элемент индексации

2026-06-26 | _config.yml | Добавлен плагин jekyll-sitemap | Автоматическая генерация sitemap.xml для всех коллекций: cottagecore, witchy, smart, studio_notes + страницы сайта — подтверждение индексации через Google Search Console

2026-06-26 | AI + Google Visibility Protocol v1.0 | Принят редакционный протокол и Style Guide | Утверждены принципы: одна статья = один вопрос, структура факт → объяснение → авторская позиция → связанные работы, запрет AI-словаря, human review перед публикацией

2026-06-27 | _layouts/article.html | Исправлен критический баг: lightbox перехватывал ссылки Read Also — перенесена загрузка jQuery и lightbox.min.js в условный блок (только при наличии detail_images) | Устранение открытия lightbox вместо перехода на статью

2026-06-27 | _layouts/article.html | Галерея переведена с .article-images на .detail-gallery / .gallery-item — единый паттерн с product-bridge | Соответствие мастер-шаблону

2026-06-27 | _layouts/about.html | Главное фото и галерея сделаны условными (только при наличии page.photo и page.detail_images) | Устранение пустых боксов при отсутствии файлов

2026-06-27 | _layouts/about.html | Добавлена загрузка lightbox CSS/JS (условно) | Корректное открытие галереи страницы О нас

2026-06-27 | _layouts/about.html + article.html | Добавлена защита от пустых строк в detail_images: {% assign img_clean = img | strip %}{% if img_clean != "" %} | Устранение пустых квадратов при наличии "" в YAML

2026-06-27 | _studio_notes/sn01-001.md | Удалена пустая строка из detail_images | Устранение пустого блока в галерее статьи

2026-06-28 | assets/css/style.css | Типографика: body font-size 16px явно, line-height 1.3 → 1.6 | Читабельность основного текста

2026-06-28 | assets/css/style.css | Иконки: .icon-title svg 18px → 24px | Восстановление исходного размера декоративных иконок

2026-06-28 | assets/css/style.css | h3: 1.1rem → 1.15rem + line-height 1.4 | Улучшение заголовков секций

2026-06-28 | assets/css/style.css | .article-body: line-height 1.7 → 1.8, font-size 1rem → 1.05rem | Читабельность длинных текстов

2026-06-28 | assets/css/style.css | .about-section p: font-size 1rem, line-height 1.7 | Читабельность страницы О нас

2026-06-28 | assets/css/style.css | .meta-date: margin-bottom 12px → 0 | Выравнивание даты и рубрики на одной линии

2026-06-29 | _includes/head.html | OG image chain: добавлен page.photo в fallback | Исправлена отсутствующая OG-картинка при шаринге страницы About

2026-06-29 | smart.md + _smart/sc01.md | Добавлено поле og_image: /assets/images/smart/smcol-og.webp | Устранение подстановки SVG колеса вместо нормального фото при шаринге Smart Collections

2026-06-29 | assets/images/smart/ | Загружено smcol-og.webp — OG-изображение для всего раздела Smart Collections | Авторское фото с колесом и котами 1200×630px

2026-06-29 | _layouts/contact.html | Создан новый layout страницы Contact | Форма обратной связи + соцсети + Google Maps + защита от спама

2026-06-29 | contact.md | Создана страница /contact/ | Устранение 404 по ссылке в меню, добавлен google_maps_url

2026-06-29 | _includes/breadcrumbs.html | Добавлен кейс layout: contact | Home / Contact

2026-06-29 | assets/css/style.css | Добавлены стили Contact Page: .contact-form, .contact-field, .contact-social-btn (Instagram/Pinterest/Facebook), .contact-success | Визуальная система страницы Contact

2026-06-29 | _layouts/contact.html | Переключение с Formspree на Web3Forms | Formspree не доставлял письма напрямую на Gmail; Web3Forms отправляет письма без посредников, лимит 250/мес вместо 50

2026-06-29 | _layouts/contact.html | Web3Forms access key f9e29840 | Подключён аккаунт ccatnbloom@gmail.com

2026-06-29 | assets/css/style.css | .contact-social-btn: flex-direction row, border-radius 20px, padding уменьшен | Кнопки соцсетей компактные таблетки вместо полноширинных блоков

2026-06-29 | _layouts/about.html | Добавлен блок Follow Us с тремя кнопками соцсетей (Instagram/Pinterest/Facebook) в левую колонку под статистикой | Единообразие с Contact страницей

2026-06-29 | _layouts/about.html | Удалена ссылка @catnbloom из правой колонки | Соцсети теперь только в левом блоке через кнопки

2026-06-30 | _layouts/contact.html | Три блока левой колонки обёрнуты в .contact-info-card | Визуальное разделение Write to Us / Find Us / Leave a Review на мобиле и десктопе

2026-06-30 | assets/css/style.css | Добавлены .contact-info-card стили (фон #f7f7f2, зелёная черта) | Читабельность блоков Contact страницы

2026-06-30 | assets/css/style.css | .about-stat: белый фон, рамка #c8d9b8, тень, шрифт крупнее | Карточки статистики стали заметнее на странице About

2026-07-01 | feed.xml | Создан RSS-канал для рассылки | Собирает товары cottagecore+witchy, Smart Collections и статьи Studio Notes по флагам send_to_newsletter и updated_at (окно 7 дней)

2026-07-01 | _includes/footer.html | Добавлен блок подписки на рассылку | Форма email + кнопка Subscribe, стиль в цветах сайта, legal disclaimer

2026-07-01 | assets/css/style.css | Добавлены стили .footer-newsletter | Зелёный фон, форма подписки, адаптив

2026-07-01 | _layouts/product-bridge.html | Last updated: site.time → page.updated_at | default: page.date_added | Дата обновления берётся из файла товара, не из момента деплоя

2026-07-01 | _cottagecore/c01-001.md | Добавлены поля updated_at и send_to_newsletter | Образец для всех товарных md-файлов

2026-07-01 | feed.xml | BUGFIX: == true → {% if item.send_to_newsletter %} | Liquid не поддерживает сравнение булевых через == true, статьи не попадали в ленту

2026-07-04 | _smart/sc01.md + smart.md | Добавлено og_image: /assets/images/smart/smcol-og.webp | OG-картинка для шаринга Smart Collections

2026-07-04 | _includes/head.html | Добавлен page.photo в цепочку OG image fallback | About страница теперь корректно передаёт фото при шаринге

2026-07-06 | feed.xml | Добавлен инлайн-стиль (max-width:100%; height:auto; display:block; margin:10px auto) во все 3 img-тега (products, smart, studio_notes) | Исправление разрыва верстки RSS-ридеров из-за оригинального размера картинок разных секций

2026-07-06 | feed.xml | Добавлен жёсткий HTML-атрибут width="600" во все 3 img-тега (products, smart, studio_notes), инлайн-стиль max-width сохранён для современных ридеров | Устранение гигантских картинок в The Old Reader, который вырезает style при кэшировании старой версии фида

2026-07-06 | _includes/footer.html + assets/css/style.css + about.html | Перенос блока соцсетей из contact.html в общий footer (+ добавлена RSS-иконка на /feed.xml), about.html очищен от дублирующего блока Follow Us | Единая точка соцсетей для всех страниц, устранение дублирования, подготовка RSS автообнаружения (head.html — ожидает файл для точной вставки)

2026-07-06 | _includes/head.html | Добавлен <link rel="alternate" type="application/rss+xml"> сразу после canonical | RSS автообнаружение фида /feed.xml браузерами, завершение задачи по добавлению RSS-иконки в футер

2026-07-06 | _includes/footer.html + assets/css/style.css | Переверстка footer с column-flex на 2-ярусную структуру (Grid 3 колонки: брендинг/категории/подписка + нижний ярус с disclaimer и соцсетями через border-top), убраны точки-разделители у тегов, форма подписки — инпут+кнопка в ряд (max-width 360px), соцконки почернены с увеличенным хитбоксом, добавлен mobile @media 768px (grid→1 колонка, newsletter наверх через order:-1, форма снова column) | Устранение пустого пространства и центрированной "колонки" на десктопе, современный responsive-макет

2026-07-06 | _includes/footer.html + assets/css/style.css | Исправлена верстка footer: заголовок подписки переведён на body-шрифт (font-weight 600), убран uppercase у "Categories", пропорции инпут/кнопка подписки изменены на 72%/26%, соцсети увеличены (44px клик-зона, тёмный цвет), disclaimer перенесён под форму подписки (правая сторона), соцсети — слева, добавлена мобильная адаптация 100%-ширины формы | Устранение нарушений дизайн-системы по чек-листу

2026-07-07 | Album Page Type (new) | Создан третий тип страницы Album: _layouts/album.html (упрощённая витрина по SKU, без hero/about, с Load More), _config.yml (коллекция albums, permalink /albums/:path/), assets/css/style.css (.album-hero/.album-hidden/.album-load-more), _includes/breadcrumbs.html (кейс layout: album → Home / Albums / Название), _includes/header.html (пункт меню Monochrome). Пример: _albums/monochrome.md | Введён лёгкий формат подборки поверх core/smart коллекций для перелинковки без создания новых SECTION/MATERIAL сущностей. Открытый долг: индекс-страница /albums/.

2026-07-07 | _includes/header.html | Пункт меню "Monochrome" заменён на dropdown "Albums" (по паттерну Shop Collections), Monochrome перенесён внутрь как первый пункт | Подготовка меню к масштабированию — новые альбомы добавляются без переработки структуры

2026-07-07 | _includes/breadcrumbs.html | Кейс layout: album — "Albums" переведён из <a href="/albums/"> в статичный <span class="crumb-static"> | Индекс /albums/ не планируется (решение автора), устранена потенциальная 404-ссылка в хлебных крошках

2026-07-07 | _layouts/album.html | Добавлен блок Share this design через {% include share-buttons.html %} (обёрнут в .container, после Load More, перед footer) | Единообразие с product/collection страницами — все страницы типа Album (включая Monochrome) теперь имеют блок шеринга. Открытый долг: page.image_url/seo_description не заданы у альбомов — Pinterest share неполный до добавления этих полей в _albums/*.md

2026-07-07 | _includes/header.html | Дропдаун Albums переведён с ручных ссылок на динамический Liquid-цикл по site.albums (sort by title) | Устранение необходимости ручной правки меню при добавлении нового альбома (кейс lovers.md, который не появился в меню)

2026-07-07 | _includes/header.html | Дропдаун Shop Collections переведён с ручных ссылок на динамический Liquid-цикл по site.pages (layout: "collection", sort by title) | Устранение необходимости ручной правки меню при добавлении новой SECTION-коллекции в будущем (аналогично решению для Albums)

2026-07-08 | _albums/monochrome.md | Добавлено поле og_image в front matter (по паттерну Smart Collections) | Закрытие критического долга OG/Pinterest-шаринга для Album-страниц (зафиксирован 2026-07-07). Требуется: 1) правка head.html — подключение page.og_image в fallback-цепочку для layout: album, 2) загрузка файла monochrome-og.webp в assets/images/albums/. Файл head.html запрошен у пользователя — не редактировался вслепую (Защита от галлюцинаций, п.2 протокола).

2026-07-08 | _includes/head.html | Аудит fallback-цепочки OG image — подтверждено, что page.og_image уже стоит первым приоритетом в цепочке (og:image и twitter:image), правка не требуется | Закрытие критического долга OG/Pinterest-шаринга для Album-страниц (2026-07-07): выяснилось, что проблема была только в отсутствии поля og_image у самих Album-файлов (monochrome.md), а не в логике head.html. Задача закрыта правкой monochrome.md (2026-07-08). Остаётся: загрузить monochrome-og.webp в assets/images/albums/.

2026-07-08 | _includes/head.html | Задача 2: добавлена ветка layout: album в JSON-LD блок (CollectionPage + ItemList по SKU из products), добавлен явный кейс album в BreadcrumbList (Albums → page.url, т.к. индекс /albums/ не создаётся) | Устранение отсутствия Schema.org для Album-страниц — до правки JSON-LD для layout: album не генерировался вообще (ветки не существовало), критично для AI Search / SEO Protocol v3.1

2026-07-08 | _includes/head.html + _albums/monochrome.md | Верификация по рендеру страницы /albums/monochrome/ | Подтверждено: JSON-LD CollectionPage с ItemList (4 SKU) генерируется корректно, BreadcrumbList с fallback на page.url корректен, og:image/twitter:image подхватывают monochrome-og.webp. Остаётся проверить физическое наличие файла monochrome-og.webp в assets/images/albums/.

2026-07-08 | _includes/head.html | Добавлено автовычисление og_image для коллекции albums (fallback: /assets/images/albums/{page.slug}-og.webp, если page.og_image не задан вручную), применено к og:image и twitter:image | Устранение необходимости вручную прописывать og_image в каждом albums-файле. lovers.md/mini.md — тестовые placeholder-файлы, не реальный контент, вопрос по отсутствию физических -og.webp для них снят автором. Логика готова к любым будущим реальным альбомам без повторного редактирования head.html. Вопрос по og:image для товаров (teepublic vs локальный d1.jpg) остаётся открытым.

2026-07-08 | _includes/head.html | Правка отменена: автовычисление og_image для albums НЕ используется. Подтверждено автором — для albums og_image указывается вручную в каждом md-файле (по образцу monochrome.md). head.html использует только page.og_image с фоллбеком на site.default_og_image, без специальной ветки для /albums/. | Ранее предложенный fallback на {page.slug}-og.webp избыточен и противоречит принятому ранее решению о ручном указании og_image per-album.

2026-07-08 | _includes/head.html | Удалена ветка auto_og (автовычисление og_image для albums по маске {slug}-og.webp), og:image/twitter:image переведены на прямое использование page.og_image в общей fallback-цепочке | Приведение файла в соответствие с решением автора: og_image для albums указывается только вручную per-файл, автофоллбек признан избыточным и потенциально маскирующим отсутствие файла

2026-07-09 | albums | протестировано - seo_description и og_image подхватываются корректно во всех нужных местах, album.html их не трогает — всё как и планировалось.

2026-07-11 | index.md (new) + _layouts/home.html (new) + assets/css/style.css | Создана Главная страница: Hero, Studio Intro, Shop Collections (динамический цикл по site.pages layout:collection + site.albums + статичная карточка Smart Collections), Latest Designs (showcase-слайдер по последним 10 товарам cottagecore+witchy, sort date_added), Latest from the Studio (3 последние статьи, article-card), Meet the Artist, Trust Block (about-stats без цифр/отзывов — только факты), Closing Banner. Все блоки переиспользуют существующие CSS-классы (.smart-month-card, .showcase-*, .article-card, .about-stats), новый CSS добавлен в конец style.css отдельным блоком "HOME PAGE" без правок существующих модулей. Newsletter не дублирован (уже в footer). Header/footer/collection.html не редактировались. | Закрытие самой приоритетной открытой задачи из раздела "В работе". Открытый долг: Schema.org для layout:home требует head.html (не редактировался вслепую — файл не был предоставлен); нужна сверка полей note.date/category/excerpt в studio_notes коллекции.

2026-07-11 | home.html + assets/css/style.css | Добавлена секция Curtain Reveal (после Trust Block, перед Closing Banner): сцена catnbloom-banner.webp + два подвижных полотна curtain_between.webp (background-position left/right top, background-size 200%), открытие через IntersectionObserver (threshold 0.4, once) добавлением класса is-open, CSS transition 1.4s на translateX(±100%), CTA-текст с задержкой fade-in. Новый CSS-блок "CURTAIN REVEAL (Home)" добавлен в конец style.css без правок существующих модулей. | Реализация задачи Curtain Reveal Banner по концепции автора. Открытый долг: подтвердить финальный путь загрузки catnbloom-banner.webp / curtain_between.webp в assets/images/ (сейчас /assets/images/home/ — предположение по конвенции сайта, не подтверждено файлами).

2026-07-11 | home.html + assets/css/style.css | Реализован Curtain Reveal Banner: секция #curtainReveal добавлена после Trust Block, перед Closing Banner. Сцена catnbloom-banner.webp на заднем плане, два полотна curtain_between.webp (одинаковый холст 2560×519) разрезаны программно через background-position left/right top + background-size 200% 100% на .curtain-left/.curtain-right. Открытие — IntersectionObserver (threshold 0.4, срабатывает один раз) добавляет класс is-open, панели уезжают transform: translateX(±100%) за 1.4s. CTA (заголовок + кнопка Explore Collections) проявляется с задержкой fade-in после открытия. Пути изображений подтверждены автором: /assets/images/home/. Новый CSS-блок "CURTAIN REVEAL (Home)" добавлен в конец style.css, существующие модули не затронуты. Задача закрыта.

2026-07-12 | home.html + assets/css/style.css | Полная перевёрстка Главной по графической схеме структуры сайта: убрана зелёная Hero-секция с H1, добавлен .home-top-grid (рамка CatnBloom Studio + текст с буквицей слева / три карточки коллекций в столбик справа, цвета brown/purple/green), добавлена розовая .home-quote-banner на всю ширину (hero_subtitle + Read Our Story), .home-split-row (Latest Designs шире + одна карточка Latest from the Studio), добавлен .home-divider перед Meet the Artist, Curtain CTA упрощён до одной контрастной розовой кнопки по центру. | Приведение Главной в соответствие с авторской схемой структуры (struktura_saita.webp)

2026-07-12 | home.html + assets/css/style.css | Консолидация CSS: удалены дублирующиеся блоки CURTAIN REVEAL (старый 1.4s из curtain-css-block.txt и новый 2.2s из хвоста HOME PAGE) — заменены единым блоком. CTA-кнопка смещена вниз сцены (align-items: flex-end, padding-bottom 8%), чтобы не перекрывать wordmark "Cat n Bloom". Добавлена CSS-анимация curtain-scene-wiggle (лёгкое покачивание всей сцены ±3px/±0.15deg, 4.5s infinite), запускается через JS спустя 2.3s после открытия занавеса — временное решение до появления отдельного PNG-слоя с руками/вешалками. | Закрытие задачи по правке занавеса: скорость, позиция кнопки, "манящее" движение

2026-07-12 | assets/css/style.css | Правки Главной (без home.html): буквица переведена на рукописный Caveat (500, #8a6a4a) вместо жирной Georgia-italic; .home-collection-card-title/-sub увеличены (1.1rem/0.92rem), .home-top-grid сужен до 1.9fr/1.15fr под более широкий сайдбар; .home-quote-banner получил явный font-family Georgia/serif; .home-closing-banner переделан из тёмно-зелёного 40px-баннера в светло-зелёный (#e9f1e6/#33502f), serif, центр, высота идентична .home-quote-banner (padding 20px26px, min-height 76px). | Закрытие пунктов 2,5,6,7 чек-листа автора. Открытый долг: пункты 1,3,4 требуют home.html (не предоставлен в этой сессии) и/или загрузки title-phame.webp в assets/images/home/ + решения по недостающему col-02-prw.webp.

2026-07-12 | home.html | Исправлен путь картинки карточки Witchy Cats + Plants: col-1-prw.webp → col-02-prw.webp (по факту загруженных файлов в assets/images/home/) | Устранение пропавшей картинки; title-phame.webp подтверждён загруженным — рамка вокруг фразы восстановлена без правок кода. style.css сверен — изменений не требуется, все 7 пунктов авторского чек-листа закрыты.

2026-07-12 | home.html + assets/css/style.css | BUGFIX: устранена лишняя высота .home-closing-banner — причиной был вложенный <div class="container"> (общий layout-класс с margin:40px auto + padding:20px), раздувавший высоту флекс-баннера сверх заданных min-height:76px. Убран .container из разметки, .home-closing-banner p получил max-width:1050px вместо него. | Устранение расхождения высоты между .home-quote-banner и .home-closing-banner на проде

2026-07-12 | home.html + assets/css/style.css | Latest Designs вынесены в отдельную full-width секцию (карточки крупнее за счёт полной ширины 1140px вместо 2.2fr колонки), Latest from the Studio перемещён из пары с Latest Designs в .home-split-row рядом с Meet the Artist | Приведение Главной в соответствие со скриншотом-референсом автора

2026-07-12 | assets/css/style.css | Увеличен размер имени студии в рамке (.home-name-frame > span: 1.6rem → 1.9rem), увеличен интерлиньяж вступительного текста (.home-intro-text: line-height 1.7 → 2.05) | Устранение мелкого шрифта имени и избыточной пустоты в конце текстового блока

2026-07-13 | home.html | Ссылка карточки Smart Collections переведена на клиентский JS: id="smartCollectionsLink" + script в конце файла вычисляет текущий месяц через new Date() в браузере посетителя и подставляет href="/smart/scNN/" | Устранение зависимости от site.time (даты сборки Jekyll на GitHub Pages) — переключение месяца теперь происходит по дате визита пользователя, а не по дате последнего коммита. Fallback href="/smart/" сохранён на случай отключённого JS.

2026-07-13 | home.html + assets/css/style.css + assets/images/home/{banner-arms,banner-logo,banner-characters,banner-frame1}.webp | Баннер Curtain Reveal переведён с одной плоской PNG-сцены на 4 стековых прозрачных слоя (characters/arms/logo + новая графика шторки frame1). JS переключён с #curtainScene на #curtainArms — независимое покачивание рук/лап с вешалками ("манящий" жест) запускается только на своём слое через 2.3s после открытия, не трогая фон и лого. Добавлен .curtain-logo { transform: scale(0.65) } только в mobile media query — лого уменьшается без обрезки соседних слоёв. Старые catnbloom-banner.webp / curtain_between.webp больше не подключаются. | Закрытие открытого долга "раздельное покачивание рук" — ранее блокировалось отсутствием отдельного PNG-слоя, теперь слой прислан и подключён.

2026-07-13 | home.html + assets/css/style.css | BUGFIX: панели .curtain-left/.curtain-right ошибочно использовали banner-frame1.webp (фоновый градиент) вместо banner-curtain.webp (ткань шторы) — шторы были практически невидимы. Исправлено: панели → banner-curtain.webp; banner-frame1.webp вынесен в новый слой .curtain-backdrop (z-index:0) позади персонажей по назначению. Добавлена анимация curtain-characters-idle (лёгкий bob ±2px) на слой персонажей, запускается синхронно с curtain-arms-wiggle через 2.3s после открытия — герои снова "живые", не только руки. | Устранение критической визуальной ошибки: отсутствие видимых штор при открытии баннера

2026-07-13 | assets/css/style.css + assets/images/home/curtain_between.webp | BUGFIX: (1) curtain_between.webp содержал прозрачную полосу ~150-280px по центру шва — при закрытых шторах давала "дыру", через которую видно нижние слои; залатано растяжкой соседних непрозрачных пикселей ткани построчно. (2) z-index .curtain-frame поднят выше .curtain-characters/.curtain-arms — статичная рама-штора теперь перекрывает руки/персонажей по краям (эффект "прячется за шторой"), а не наоборот. (3) Увеличена амплитуда curtain-arms-sway (±4px/1° → ±7px/2°) и curtain-characters-bob (±2px → ±5px + rotate) — покачивание теперь заметно на масштабе баннера. home.html не менялся. | Устранение видимой "дыры" в шторе, обрубленных рук поверх ткани и статичности персонажей

2026-07-14 | index.md + home.html | Правки текста Главной по замечаниям коллеги: сокращён список товаров в studio_intro, усилена финальная фраза intro, переписан meet_artist_text, Trust Block расширен с 3 до 4 карточек (Carefully Refined / Character First / Drawn for Everyday Joy), Closing Banner → "See you in the next illustration.", добавлена SEO-строка (.home-section-lead, новый класс) под Latest Designs | Реализация редакторских правок коллеги. Открытый долг: стиль для .home-section-lead не добавлен в style.css — файл не был предоставлен в этой сессии.

2026-07-14 | home.html + assets/css/style.css | Trust Block пересмотрен по итогам ревью автора: удалена карточка Independent Studio, у Human-Made убрана подпись "No AI-generated artwork" (заголовок оставлен), Carefully Refined/Character First/Drawn for Everyday Joy сохранены — итого 5 карточек. .home-trust-stats переведён с 3 на 5 колонок (desktop), mobile-override с 1 на 2 колонки | Уточнение состава карточек Trust Block по скриншоту-правке автора поверх правок коллеги

2026-07-14 | home.html | Trust Block: карточки переставлены так, чтобы двухстрочная "Cats & Flowers" оказалась по центру (позиция 3 из 5) — новый порядок Human-Made / Carefully Refined / Cats & Flowers / Character First / Drawn for Everyday Joy | Визуальное выравнивание грида по скриншоту-правке автора

2026-07-14 | assets/css/style.css | Исправлен .home-photo-strip: desktop object-fit cover→contain (height:auto, max-height:420px, фон #1a1a1a под пропорции), mobile override уменьшен до 90px с сохранённым cover как узкая полоса-заглушка | Устранение обрезки краёв панорамного фото стола студии на десктопе — изображение теперь видно полностью, обрезка оставлена только на мобильной версии по требованию автора

2026-07-15 | index.md + home.html | Финальная правка текста Главной: meet_artist_text (illustration→design, artist→designer, упрощена концовка), заголовок секции "Meet the Artist"→"Meet the Designer", closing banner "next illustration"→"next story" | Приведение текста в соответствие с реальным профилем автора (дизайнер, не иллюстратор)

2026-07-15 | assets/css/style.css | Добавлен блок :root с полным набором токенов (типографика, вертикальный ритм, цвет) из CatnBloom_Design_System_v1_0.md и CatnBloom_Color_Tokens_v1_0.md, вставлен после @import шрифта перед RESET-блоком, остальной код не изменён | Шаг 0 плана унификации типографики и цвета — база для последующей замены хардкода на переменные без визуальных изменений на этом этапе

2026-07-17 | _2_CatnBloom_Decision_Checklist_v1_1.md | Финализирован опросник Шагов 1–5 (типографика/цвет/карточки), добавлен пункт 1.7 (навигационное меню: .nav-right a → 15–16px/600, .dropdown-menu a → 14px, отдельная шкала вне Body Medium), заполнена таблица умышленных исключений (буквица line-height 1.85, .article-body line-height 1.7, отступы секций Главной 96/48px, отдельные токены card-title/inline-H2/inline-H3, шкала меню) | Закрытие решений перед переносом в CSS-токены Шага 0; подготовка к Шагу 6 (witchy-палитра) и пересборке preview-файлов с финальными цифрами

2026-07-17 | assets/css/style.css + _2_CatnBloom_Decision_Checklist_v1_1.md | Объявлены недостающие CSS-токены Шагов 1–3 v1.1 (--font-h3-icon, --font-h2-inline/-h3-inline, --font-card-title, --font-nav/-nav-dropdown, --line-article-body, --font-intro/--line-intro, --font-footer-newsletter-title/-sub, --section-gap-lg/-md, --studio-card-*) в новом блоке STEP 6 — v1.1 DECISION TOKENS. Замена хардкода на var() НЕ выполнялась (отдельный шаг Implementation Order). Чек-лист повышен до v1.2, отмечен прогресс. | Закрытие пункта "токены не приведены к значениям v1.1" из прошлой сессии

2026-07-17 | assets/css/style.css | Применены токены --font-nav (16px) и --font-nav-dropdown (14px) к .nav-right a и .dropdown-menu a (desktop+mobile), хардкод 14px/13px удалён, mobile-версии dropdown добавлен явный font-size (ранее не задан) | Закрытие пункта 1.7 чек-листа v1.2 — замена хардкода на var() для навигационного меню

2026-07-18 | CatnBloom_Color_Tokens_v1_1.md (rename v1.0→v1.1) + _2_CatnBloom_Decision_Checklist_v1_3.md (rename v1.2→v1.3) + assets/css/style.css | Закрыт Шаг 6: 6 токенов Witchy/Home-группы (wine/wine-deep/plum/mauve/sage-dark/blush-bg) переведены в статус RESERVED — перекраска Witchy НЕ проводится, реальные роли (блоки Главной) задокументированы в md-разделе 4а, в style.css добавлен только пояснительный комментарий над блоком токенов, значения/имена/usages не менялись | Закрытие открытого пункта чек-листа 4.5/п.3 без изменения визуала и логики сайта — токены сохранены "на память" под будущие точечные акценты

2026-07-18 | assets/css/style.css | Шаг 6: пересобраны preview 1-3 с финальными компромиссными значениями v1.3 (вместо буквальной спецификации). Шаг 7: заменён хардкод на var() по всему файлу — цвет (включая консолидацию text-tertiary→text-secondary и witchy/wine-группу на местах реального использования: .home-name-frame>span, .extra-link, .home-card-*, .home-quote-banner), типографика (H1/H3-icon/inline-H2/inline-H3/card-title+line-clamp/card-excerpt+line-clamp/article-body/about-section/intro/footer-newsletter), Studio Notes grid (gap/padding/inner-gap), дифференцированные отступы секций главной (48px тесно связанные / 96px перед curtain-reveal). Nav (п.1.7) был готов ранее, не трогалась | Закрытие пунктов 4-5 списка оставшихся шагов чек-листа v1.3

2026-07-18 | assets/css/style.css | Шаг 8: заменён хардкод на var() в трёх пропущенных Шагом 7 зонах — footer left/middle columns (.footer-col-title→--font-footer-newsletter-title, .footer-copyright/.footer-brand-list li/.footer-tags-list li→--font-body), .smart-month-label/.smart-month-sub (→--font-body/--font-caption), .faq-question/.faq-answer (→--font-body). Удалён мёртвый дубль-блок .about-section p | Закрытие визуального разрыва между токенизированными и нетронутыми зонами, обнаруженного по скриншоту-ревью автора

2026-07-19 | PROJECT_MASTER.md | Архитектурная заморозка (Шаг 2 плана): зафиксирован финальный список Jekyll-коллекций (cottagecore, witchy, smart, studio_notes, albums — все output:true с закреплёнными permalink) и финальный набор шаблонов (collection, product-bridge, smart-collection, smart-home, article, studio-notes, about, contact, album, home). jekyll-sitemap подтверждён подключённым, robots.txt ссылается на /sitemap.xml. | Протокольная фиксация текущей архитектуры перед дальнейшей работой над картой сайта (Шаг 3) — новые типы страниц/коллекций/permalink без отдельного разрешения автора не создаются

## Текущий этап разработки

- **Завершено:** feed.xml создана и структурирована главная страница унифицированы единые стили сайта и они отражены в обновленном файле style.css, включая типографику и цветовые решения





Планирование задач



—-

Из чек-листа который мы составляли — страница /contact/ так и не создана, ссылка в меню ведёт в 404. Это первоочерёдно.

Load More для product grid — отложено до накопления контента, актуально когда карточек станет 12+.

Wheel overlay (шапочки на колесе) — PNG ещё не загружены, механика готова.

Новые задачи — как я их понимаю по приоритету:

- **В работе:**

Карта сайта. 

Google Search ← после наполнения контентом 6. Load More ← после 12+ карточек

- **Запланировано:**


[ ] Mobile — проверить меню, showcase, карточки статей на телефоне
[ ] Core Web Vitals — после подключения Search Console проверить показатели скорости
[ ] jekyll-sitemap плагин — убедиться что GitHub Pages его подхватил (в настройках репо Pages должен быть включён)

## Известные ограничения

- Работа ведется строго через GitHub Web Interface.

- Не менять имена файлов без прямого запроса.

- Всегда соблюдать структуру протокола v2.0.

=====================

Также при создании файлов и редактировании учитываем

Чек-лист №1: Инженерный контроль архитектуры (Профилактика хаоса)

Задача не допустить появления «заплаток» и сохранить единство шаблонов при создании новых страниц.

[ ] Структурный стандарт: Страница использует тот же базовый каркас (<div class="container">, left-block, right-block), что и утвержденный product.html?

[ ] Глобальные компоненты: Шапка (header.html) и подвал (footer.html) подключены через {% include %} в самом начале и в самом конце файла? Никакой верстки шапки внутри файла страницы!

[ ] CSS-изоляция: Все стили вынесены в assets/css/style.css? Нет ли в шаблоне страницы тегов <style>, которые переопределяют поведение меню или подвала?

[ ] Скрипты: Логика меню (toggleMenu) вызывается из глобального JS-файла? Нет ли в файле дублирующихся скриптов?

[ ] DRY-принцип: Есть ли элементы, которые мы повторили дважды? Если да — выносим их в отдельный файл в _includes/.

[ ] Контроль «чистоты»: После правок мы проверяем, не «поплыло» ли меню на другой странице (например, на старом продукте)?

Чек-лист №2: Соответствие AI Search и SEO (Протокол v3.1)

Да подготовки контента, чтобы его понимали поисковые роботы и системы ответов.

[ ] Иерархия контента: Есть ли в первом абзаце суть страницы (что это за дизайн или коллекция), чтобы ИИ-агент сразу получил ответ?

[ ] Сеть сущностей: Есть ли на странице ссылки на связанные сущности (Коллекция → Продукт, Продукт → Статья, Коллекция → Колесо навигации)?

[ ] Интеграция Schema.org: Добавлен ли JSON-LD блок (соответственно типу страницы: Product, CollectionPage, Article)?

[ ] Human Proof: Есть ли в тексте авторские заметки или описание художественных решений? Нет ли искусственных маркетинговых слов?

[ ] Брендовая идентичность: Понятно ли из контекста страницы, что это CatnBloom Studio? (Указано ли это в заголовках, мета-данных или через структуру перелинковки?)

[ ] Читаемость для роботов: Используются ли списки, таблицы или FAQ для подачи данных? (ИИ лучше индексирует структурированные факты, чем сплошной текст).

Необходимо подвергать файлы "инженерной сверке" по Чек-листу №1, чтобы ликвидировать все «заплатки» и привести шаблоны к эталону.

Прошедший тестирование код «замораживается» как новый стандарт.
