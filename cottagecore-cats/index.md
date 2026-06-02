---
layout: default
permalink: /cottagecore-cats/
hero_title: "Cottagecore Cats"
hero_subtitle: "Cozy cats, flowers & soft aesthetics"
intro: "A collection of soft, floral cat illustrations inspired by cottagecore life."
tagline: "Wearable art for soft living"
---

<nav class="breadcrumbs">
  <a href="/">Home</a>
  <span>/</span>
  <span class="current-page">{{ page.hero_title }}</span>
</nav>

<header class="collection-hero">
  <h1>{{ page.hero_title }}</h1>
  <p class="subtitle">{{ page.hero_subtitle }}</p>
</header>

{% if page.intro %}
<section class="collection-intro">
  <p>{{ page.intro }}</p>
</section>
{% endif %}

<section class="product-grid" id="grid">
  {% assign collection_name = 'cottagecore' %}
  {% for item in site[collection_name] %}
    {% if item.status != 'hidden' %}
    <a class="product-card load-item" href="{{ item.url }}">
      <img src="{{ item.image_url | default: '/assets/images/placeholder.jpg' }}"
           alt="{{ item.alt_text | default: item.title }}">
      <div class="product-title">{{ item.headline | default: item.title }}</div>
      <div class="product-sku">{{ item.sku }}</div>
    </a>
    {% endif %}
  {% endfor %}
</section>

<button id="loadMoreBtn" class="load-more">
  Load more
</button>

<footer class="collection-footer">
  <p>{{ page.tagline }}</p>
</footer>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const items = document.querySelectorAll('.load-item');
  const btn = document.getElementById('loadMoreBtn');
  let visible = 24;

  function updateView() {
    items.forEach((el, index) => {
      el.style.display = index < visible ? 'flex' : 'none';
    });
    if (visible >= items.length && btn) {
      btn.style.display = 'none';
    }
  }

  if (btn) {
    btn.addEventListener('click', () => {
      visible += 24;
      updateView();
    });
  }
  updateView();
});
</script>
