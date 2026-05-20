# SEO Playbook — opauto-clicker.com

The exact sequence that took this site from zero to **Bing position 4 + 885 AI citations in 10 days** (May 4 → May 20, 2026).

This document exists so we can replicate the result on any new site. The full skill version with templates lives at `~/.claude/skills/seo-launch-blueprint/`.

## The headline result

| Metric | Day 0 (May 4) | Day 16 (May 20) |
|---|---|---|
| Pages on site | 17 | **42** |
| Bing homepage rank | Not indexed | **Position 4** |
| Bing impressions (3M) | 0 | **14,100** |
| AI Performance citations (3M) | 0 | **885** |
| AI grounding queries triggering us | 0 | **20+ distinct** |
| Average word count | ~700 | **1,186** |
| Pages with FAQPage schema | 11 | **37** |
| Pages with author byline | 0 | **35** |
| Schema types in use | 9 | **23** |

## The 17 commits (in order)

This is the actual chronological sequence — what we did, when, why each one mattered.

### Foundation (commits 1-4)
1. **`60759fa` — CSS fix for broken subpage hero images.** Subpages were missing the `.hero-img` class style. Visible-symptom fix; revealed the CSS cache TTL was 24h (too long).
2. **`0feb257` — keyword density trim on over-optimized pages.** Three pages had "OP Auto Clicker" repeated to the point of looking spammy.
3. **`72971f3` — inline image width constraints on all hero images.** Defensive against the CSS cache issue: `style="width:100%;max-width:1100px;height:auto..."` directly on `<img>` tags. CSS-cache-proof.
4. **`fd61b66` — image cleanup.** Removed a broken YouTube facade (placeholder `data-yt="YOUTUBE_VIDEO_ID"` was lying to users). Compressed `og-image.png` from 137KB → 55KB via PIL palette quantization.

### Image + branding (commit 5)
5. **`1cfb919` — per-page OG images + brand fix.** Generated 6 unique 1200×630 OG cards (Minecraft, Roblox, Windows 11, Fastest, Safe, homepage) with PIL. Critical fix: old OG image still said `opauto.app` (the previous domain) — regenerated with `opauto-clicker.com`.

### Content + schema (commits 6-7)
6. **`dcb7fbc` — FAQPage schema on homepage + Person schema on About + 2025→2026 date update.** Homepage had `<h2>` questions in the body but no FAQPage schema. Added it with 5 Q&As. About page needed `Person` entity for E-E-A-T.
7. **`bc00fc0` — testimonials + dates + ordered lists + tips sections.** Removed fake `AggregateRating` (claimed 12,847 ratings — unverifiable, manual penalty risk). Removed 6 fake `Review` schemas. Anonymized 6 visible testimonials to source-attributed roles ("Minecraft player · Discord" instead of made-up names). Converted `/how-to-use` steps from `<div>` grid to semantic `<ol>` with `HowToStep` itemprops. Added "tips from community" sections to windows-11, cps-test, safe pages.

### New pages (commit 8)
8. **`fa24a92` — 3 new pages + maintainer bio on About + footers wired.** Added `/auto-clicker-for-mac` (captures macOS search intent we 100% missed), `/cookie-clicker-auto-clicker`, `/auto-clicker-not-working`. Added "Who maintains it" section to About with `@op-auto-clicker` handle + contact channels. Updated footer nav across all 14 existing pages to surface new pages.

### The critical technical fix (commit 9)
9. **`1766dff` — canonical → www + 301 redirect, shorten titles/descs, sitemap refresh.** THE highest-impact commit. Was: canonicals pointed to non-www but server 307'd non-www → www (signal conflict). Now: all canonical URLs + og:url + JSON-LD URLs use `https://www.opauto-clicker.com`, plus 301 redirect in `vercel.json` for apex → www. Shortened 13 titles from 60-73c down to 40-53c (no more SERP truncation). Dropped landing.css cache TTL from 24h to `max-age=300, stale-while-revalidate=86400`.

### GEO / AI visibility (commit 10)
10. **`2a8cefb` — definition sections + bylines + SearchAction + semantic FAQ h3.** Added "What is X?" definition sections (~115-126 words each, optimal AI passage range) to 13 use-case pages. Added visible author byline below H1 on 13 article pages with `<time datetime="">` semantics. Wrapped 20 FAQ question texts in `<h3>` for semantic heading + better AI passage extraction. Added `SearchAction` to WebSite schema on index.

### SXO (commit 11)
11. **`d18a7a6` — cookie-clicker bookmarklet + roblox/minecraft safety + fastest comparison.** Page-type pivots based on SERP analysis: `/cookie-clicker-auto-clicker` was wrong intent — added browser-bookmarklet section with copyable JS snippet (the SERP wanted browser-first, not desktop-app). `/roblox-auto-clicker` title rewritten with "Safe for Clicker Sims" framing (winning competitor pattern). `/minecraft-auto-clicker` added `SoftwareApplication` schema with `about: VideoGame/Minecraft`. `/fastest-auto-clicker` pivoted from single-product defense to comparison page (Speed AutoClicker, TinyTask, GS, AutoHotkey, OP).

### Cluster expansion (commit 12)
12. **`8020c86` — 7 new SEO-targeted pages.** Top picks from cluster audit: `/auto-clicker-for-chromebook` (dedicated SERP, weak competitors), `/minecraft-auto-clicker-afk` (extends strongest cluster), `/kohi-click-test` (interactive 5s CPS tool), `/auto-clicker-not-detected` (honest detection guide), `/op-auto-clicker-vs-tinytask` (fills only major comparison gap), `/hypixel-auto-clicker`, `/auto-clicker-for-idle-games`. Each: ~1100-1300 words, FAQPage schema, Article schema with staggered datePublished, ordered-list step guides, comparison tables, related links.

### llms.txt + minor cleanup (commit 13)
13. **`b8395c0` — tighten 2 descriptions + expand llms.txt.** Added 10 newly-published pages to `llms.txt` so AI crawlers can discover them via the structured guidance file.

### Homepage expansion (commits 14-15)
14. **`cab23a3` + `da49a7f` — Bing canonicalization + homepage 1,451 → 2,419 words.** Added `@id` self-references to WebSite + SoftwareApplication schemas (Bing uses this for entity canonicalization). Added `rel="home"` link. Expanded homepage content: "What is OP Auto Clicker?" section (~330 words), "60-second setup" `<ol>`, "When to use vs when not to" two-column honesty section (~360 words), "How OP Auto Clicker actually works" technical detail (~340 words).

### Long-form article import (commit 16)
15. **`7d57988` — import 15 long-form articles, themed to match site.** Imported white-bg default styled articles, re-themed to site's dark navy/purple. Pages: best-auto-clicker, auto-clicker-pc, auto-clicker-laptop, auto-clicker-for-macos, auto-clicker-for-roblox, roblox-autoclicker, super-fast-auto-clicker, good-auto-clicker, automatic-clicker, free-autoclickers, download-autoclicker, free-auto-clicker-download, op-auto-clicker, op-auto-clicker-download, op-auto-clicker-4-0. Added 40+ lines of `.article-body` CSS so imported markup renders properly in dark theme.

### Post-audit cleanup (commit 17)
16. **`020a66a` — breadcrumb on homepage, description tighten, canonicalization for clusters.** Added `BreadcrumbList` to homepage (was missing — every other page had it). Tightened 8 meta descriptions from 160-181c to 120-141c. Canonicalization fixes: `/auto-clicker-for-roblox` and `/roblox-autoclicker` → `rel="canonical"` to `/roblox-auto-clicker`; `/op-auto-clicker-download`, `/download-autoclicker`, `/free-auto-clicker-download` → `rel="canonical"` to `/download`. Pruned sitemap from 41 → 36 URLs (only canonicals).

## What Bing tells us worked (post-launch data)

**AI grounding queries** (the queries that triggered AI to cite our content):
- "how to use op auto clicker" — 20 citations → our `/how-to-use-auto-clicker` page
- "op auto clicker" — 10 citations → homepage
- "fastest op auto clicker settings" — 8 citations → `/fastest-auto-clicker`

Pattern: pages with answer-first H2s, FAQ schema, ordered-list steps, and comparison tables get cited disproportionately.

**Bing search positions** (homepage `https://www.opauto-clicker.com/`, 3-month window):
- Position 3: 2.6K impressions, 28 clicks, 1.09% CTR
- Position 4: 4.6K impressions, 23 clicks, 0.50% CTR
- Position 5: 1.8K impressions, 5 clicks, 0.27% CTR
- Positions 6-10: ~973 impressions, 0 clicks

Pattern: getting indexed and ranking was solved by the canonical/www fix + Bing schema signals (commits 9 + 14). Low CTR remaining is a snippet copy issue (next iteration).

## External signals that helped (user-reported)

- Published 10 Claude artifacts (each linking back to the site)
- Listed on tech sites in the GitHub orbit + Stack Overflow / Stack Exchange answers
- Bing Webmaster Tools verification + IndexNow protocol

## Replicating this on a new site

Use the skill: `/seo-launch-blueprint` — it contains the full templates (vercel.json, robots.txt, sitemap, llms.txt, page template, schema snippets) and the 8-phase execution playbook.

OR: clone this repo at `https://github.com/reggieog01-cpu/opauto` as a structural reference, replacing brand-specific content.
