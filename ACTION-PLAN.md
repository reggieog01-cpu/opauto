# OP Auto Clicker — SEO Action Plan

Prioritized list of fixes, ordered by impact-to-effort ratio. See `FULL-AUDIT-REPORT.md` for context on each item.

---

## 🔴 Critical (Fix before deploy)

### 1. Add Open Graph + Twitter Card meta to all 4 pages
**Effort**: 15 min · **Impact**: Massive (every shared link looks broken without it)

Add inside `<head>` on every page (replace per-page values):

```html
<meta property="og:type" content="website">
<meta property="og:title" content="<same as <title>>">
<meta property="og:description" content="<same as meta description>">
<meta property="og:url" content="https://opauto.app/<path>">
<meta property="og:image" content="https://opauto.app/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="OP Auto Clicker">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="<same>">
<meta name="twitter:description" content="<same>">
<meta name="twitter:image" content="https://opauto.app/og-image.png">
```

### 2. Add favicon + apple-touch-icon + theme-color
**Effort**: 20 min (create one SVG) · **Impact**: High brand polish

```html
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0F172A">
```

A simple "OP" wordmark on green (`#22C55E`) background works.

### 3. Generate the OG image
**Effort**: 30 min · **Impact**: Critical for social sharing

1200×630 PNG showing "OP Auto Clicker" wordmark + the app mockup + "Free for Windows" + green accent. Place at `/og-image.png`.

### 4. Create `llms.txt`
**Effort**: 10 min · **Impact**: Future-proofing AI search

Place at `/llms.txt`:

```
# OP Auto Clicker

> OP Auto Clicker is a free, open-source auto-clicking program for Windows.
> Supports up to 100+ clicks per second, custom intervals from 1ms,
> hotkey toggles, and fixed-position clicking.

## Quick facts
- Works on Windows 7, 8, 10, 11 (32-bit and 64-bit)
- File size: 512 KB, no installation required
- Free and open source
- Not affiliated with any commercial auto-clicker

## Pages
- [Home](https://opauto.app/): Features, demos, comparison
- [Download](https://opauto.app/download): Latest v3.0.0, install steps, system requirements
- [FAQ](https://opauto.app/faq): 20 questions across 4 categories
- [About](https://opauto.app/about): Project story, values, timeline
```

---

## 🟠 High Priority (Within 1 week)

### 5. Fix `faq.html` heading hierarchy
**Effort**: 5 min · **Impact**: Accessibility + SEO

In `faq.html`, change all 4 instances of:
```html
<div class="faq-cat-title">Getting Started</div>
```
to:
```html
<h2 class="faq-cat-title">Getting Started</h2>
```

The CSS already styles `.faq-cat-title` correctly — no visual change.

### 6. Add `<lastmod>` to every entry in `sitemap.xml`
**Effort**: 2 min · **Impact**: Crawl signal

```xml
<url>
  <loc>https://opauto.app/</loc>
  <lastmod>2026-04-29</lastmod>
  <changefreq>weekly</changefreq>
  <priority>1.0</priority>
</url>
```

Repeat for all 4 entries. Update `<lastmod>` whenever the page changes.

### 7. Fix Google Fonts FOIT — add `display=swap`
**Effort**: 30 sec per file × 4 = 2 min · **Impact**: Faster perceived load

Replace on every page:
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
```
(append `&display=swap`)

### 8. Add E-E-A-T signals to `about.html`
**Effort**: 30 min · **Impact**: Trust + AI citation eligibility

Add a "Maintainers" or "Built by" section with:
- At least one named maintainer (real or pseudonym + GitHub link)
- Link to public GitHub releases page (sources the download counts)
- Link to security disclosure policy
- Link to license

### 9. Source the statistics or soften them
**Effort**: 15 min · **Impact**: AI citation eligibility

Either:
- **Source them**: link "5M+ downloads" to GitHub releases stats page; link "12,847 ratings" to a real review aggregator
- **Or soften**: "millions of downloads", "thousands of users worldwide", "consistently 4-5 stars across reviewers"

Currently AI Overviews + ChatGPT will not repeat exact numbers without a source.

### 10. Replace emoji icons with SVG
**Effort**: 2-3 hours (~50 emojis) · **Impact**: Cross-platform consistency + UI quality

Use [Lucide](https://lucide.dev) or [Heroicons](https://heroicons.com). Inline each SVG (~1 KB each, only 4-6 unique icons per page). The `ui-ux-pro-max` skill explicitly forbids emoji-as-icons.

### 11. Add product screenshots to `download.html` and `index.html`
**Effort**: 30 min if screenshots exist · **Impact**: Image search SEO + trust

At minimum:
- 1 screenshot of the actual OP Auto Clicker UI on download.html
- Replace the CSS-art "mockup" on index.html with a real screenshot (or keep the mockup AND add a real screenshot below)

Use `loading="lazy"`, explicit `width`/`height`, descriptive `alt` text containing "OP Auto Clicker".

---

## 🟡 Medium Priority (Within 1 month)

### 12. Extract shared CSS to `/styles.css`
**Effort**: 1 hour · **Impact**: 60% smaller subsequent page loads

Currently each page inlines ~9-12 KB of mostly identical CSS. Move common tokens, nav, btn, footer, mockup styles to a single file. Keep page-specific styles inline.

### 13. Reconcile `SoftwareApplication` schema between index + download
**Effort**: 5 min · **Impact**: Schema consistency

Either:
- Make both copies byte-identical (preferred)
- Or remove from index.html and add `Product` or `WebPage` schema instead

### 14. Add `HowTo` schema to download.html install steps
**Effort**: 10 min · **Impact**: Rich result eligibility

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to install OP Auto Clicker",
  "step": [
    {"@type": "HowToStep", "position": 1, "name": "Download", "text": "..."},
    ...
  ]
}
```

### 15. Add `ItemList` schema to use-cases on index.html
**Effort**: 10 min · **Impact**: Rich result eligibility

### 16. Reword H2s as questions for AI search alignment
**Effort**: 15 min · **Impact**: AI Overviews citation rate

Examples:
- "What People Say" → "What do people say about OP Auto Clicker?"
- "Our Story" → "How was OP Auto Clicker built?"
- "Why OP" → "Why choose OP Auto Clicker over manual clicking?"

### 17. Add `dateModified` to all pages
**Effort**: 10 min · **Impact**: Freshness signal

In schemas + visible "Last updated" footer line.

### 18. Add 2-3 outbound authority links per page
**Effort**: 20 min · **Impact**: Topical authority

Examples:
- Microsoft .NET docs from Requirements section on download.html
- Wikipedia "Auto clicker" article from index hero
- GitHub repo from about.html

---

## 🟢 Low Priority (Backlog)

### 19. Add `prefers-reduced-motion` media query
Disable hero cursor animation + reveal animations when set.

### 20. Add `Review` schema to testimonials on index.html
Currently visual-only. Could be structured.

### 21. Add web app manifest (`/manifest.webmanifest`)
For Add-to-Homescreen on Android (low priority for a download site).

### 22. Add `prerender` / `prefetch` hints
e.g., `<link rel="prefetch" href="/download">` on index.html (highest-CTR target).

### 23. Self-host Inter font instead of Google Fonts
Eliminates third-party request, saves ~50-150ms LCP. Use `font-display: swap`, WOFF2 only.

### 24. Add breadcrumbs visual UI on subpages
Schema present, but no visual breadcrumb navigation. Aids UX + visual breadcrumb may show in SERP.

### 25. Dark/light mode toggle
Site is dark-only. Adding light mode signals UX care + reduces bounce on bright environments.

---

## Quick-Win Bundle (60 minutes total)

If you only have an hour, do these in order:

1. **(2 min)** Add `&display=swap` to fonts URL × 4 pages
2. **(2 min)** Add `<lastmod>` to sitemap × 4 entries
3. **(5 min)** Fix faq.html heading levels — `div` → `h2`
4. **(10 min)** Create `llms.txt`
5. **(15 min)** Add OG/Twitter meta + favicon links to all 4 pages
6. **(20 min)** Generate + add OG image and favicon SVG
7. **(5 min)** Soften stats: replace "5M+ downloads / 4.8★ from 12,847 ratings" with sourced or softened versions

These take the score from **78** to roughly **86-88** with minimal risk.
