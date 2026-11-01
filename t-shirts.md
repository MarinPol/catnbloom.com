---
layout: landing
title: "T-Shirts with Cats & Flowers"
permalink: /t-shirts/

# SEO
seo_title: "T-Shirts with Cats & Flowers | CatnBloom Studio"
seo_description: "Explore illustrated T-shirts featuring CatnBloom Studio designs inspired by cats, flowers and botanical art. View each design and find it on TeePublic or Redbubble."

# Optional: image used for social sharing. If empty, hero_collage.main.src is used.
# og_image: ""

# =====================================================================
# STUDIO PICKS - THE ONLY PLACE YOU EDIT TO CHANGE THE SET OF DESIGNS
# One line per design: just the SKU. Order here = numbers 01-10 on the page.
# Title, thumbnail, story, "View design", TeePublic and Redbubble links are
# all taken from the product card with that SKU. Nothing is typed twice.
#
# Pattern: odd rows = Cottagecore (C01-*) on the light tee,
#          even rows = Witchy (C02-*) on the black tee.
#
# Print on the tee (transparent WebP, 300x360) is NOT stored in the repo.
# It is loaded from external storage by SKU:
#   picks_print_base + lowercase SKU + "." + picks_print_ext
#   e.g. https://ik.imagekit.io/catnbloom/prints/c01-001.webp
# Upload the file to ImageKit folder /prints/ named like the SKU - that is all.
# If the file is missing, the slide shows the product image instead.
#
# Optional per-pick keys (rarely needed):
#   name: "..."   shown only while the SKU has no card yet
#   tee: dark     force the black tee (default: C02-* dark, others light)
#   print: "https://..."   explicit print URL instead of the automatic one
#   print_x / print_y / print_w   fine tuning in percent of the tee photo
# To swap a design: change the sku. Nothing else.
# =====================================================================
picks_stage_image:
  src: "/assets/images/t-shirts/tee-base.webp"
  alt: "Plain white T-shirt hanging on a brick wall by a sunlit window"
picks_stage_image_dark:
  src: "/assets/images/t-shirts/tee-base-black.webp"
  alt: "Plain black T-shirt hanging on a brick wall by a sunlit window"
picks_print_base: "https://ik.imagekit.io/catnbloom/prints/"
picks_print_ext: "webp"

picks:
  - sku: "C01-001"
    print: "https://ik.imagekit.io/catnbloom/prints/C01-001.webp"
  - sku: "C02-001"
    print: "https://ik.imagekit.io/catnbloom/prints/C02-001.webp"
  - sku: "C01-004"
    print: "https://ik.imagekit.io/catnbloom/prints/C01-004.webp"
  - sku: "C02-002"
    print: "https://ik.imagekit.io/catnbloom/prints/C02-002.webp"
  - sku: "C01-035"
    print: "https://ik.imagekit.io/catnbloom/prints/C01-035.webp"
  - sku: "C02-008"
    print: "https://ik.imagekit.io/catnbloom/prints/C02-008.webp"
  - sku: "C01-038"
    print: "https://ik.imagekit.io/catnbloom/prints/C01-038.webp"
  - sku: "C02-019"
    print: "https://ik.imagekit.io/catnbloom/prints/C02-019.webp"
  - sku: "C01-039"
    print: "https://ik.imagekit.io/catnbloom/prints/C01-039_.webp"
  - sku: "C02-029"
    print: "https://ik.imagekit.io/catnbloom/prints/C02-029.webp"

# --- 1. Hero ---
hero_title: "T-Shirts with Cats & Flowers"
hero_subtitle: "Illustrated Designs by CatnBloom Studio"
hero_text: "Every CatnBloom T-shirt carries one of our own illustrations: a cat, a few plants, and a small story you can read at a glance."
hero_collections:
  - label: "Cottagecore Cats"
    url: "/cottagecore-cats/"
  - label: "Witchy Cats + Plants"
    url: "/witchy-cats-plants/"
# Hero v4 (new header). Files are baked from the author's SVG to final proportions
# (no distortion, brush edges kept). The plaque image is text-free and lives in
# style.css; the title bar, collection links and plaque text are live HTML.
hero_collage:
  main:
    src: "/assets/images/t-shirts/hero4-main.webp"
    alt: "Woman in a sunlit room wearing a CatnBloom Floral Balance T-shirt, petting an orange cat"
  tee:
    src: "/assets/images/t-shirts/hero4-tee.webp"
    alt: "Folded light blue T-shirt with The Lovers cat design on a wooden bench"
  oval:
    src: "/assets/images/t-shirts/hero4-oval.webp"
    alt: "Illustrated gray cat holding a purple flower and an autumn maple leaf"

# --- 2. What makes our designs different ---
differences_title: "What makes our designs different"
differences_deco:
  src: "/assets/images/t-shirts/deco-paw.webp"
differences:
  - title: "A story in every drawing"
    text: "Each design has a character, an action, and objects that relate to each other. Look closely and you can tell what is happening."
  - title: "Cats and plants, drawn together"
    text: "Flowers, pumpkins, books and brooms are part of the scene, not background decoration."
  - title: "Drawn by us, refined by hand"
    text: "Each design is built with digital linework and layered color cleanup by CatnBloom Studio."

# --- 3. Studio Picks (texts) ---
picks_title: "Studio Picks"
picks_note: "Our site is a studio showcase. The shirts are made and shipped by TeePublic and Redbubble."

# --- 4. A short history of the tee ---
history_title: "A short history of the tee"
history_items:
  - year: "1913"
    text: "The U.S. Navy starts issuing white cotton crew-neck undershirts to sailors."
    image:
      src: "/assets/images/t-shirts/history-1913.webp"
      alt: "Sailor in a white T-shirt and cap, early twentieth century"
  - year: "1938"
    text: "Sears advertises a cotton tee as both an undershirt and an outershirt."
    image:
      src: "/assets/images/t-shirts/history-1938.webp"
      alt: "Vintage Sears catalog page showing men in cotton T-shirts"
  - year: "1951"
    text: "Marlon Brando wears one in A Streetcar Named Desire. James Dean follows in 1955."
    image:
      src: "/assets/images/t-shirts/history-1951.webp"
      alt: "Black-and-white night street scene with a vintage car"
  - year: "1977"
    text: "Milton Glaser’s I ♥ NY logo, made for a 1977 tourism campaign, soon becomes a T-shirt classic."
    image:
      src: ""
      alt: ""
history_note: "From underwear to a blank canvas: today the tee can carry a small story, like ours."
history_deco:
  src: "/assets/images/t-shirts/history-cat.webp"
divider_image:
  src: "/assets/images/t-shirts/divider-grass.webp"
---
