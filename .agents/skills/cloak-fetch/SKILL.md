---
name: cloak-fetch
description: >
  Fetch a rendered web page using CloakBrowser stealth browser, bypassing
  anti-bot detection (Cloudflare, reCAPTCHA) and GFW. Use when WebFetch
  fails on Cloudflare-protected, JS-heavy, or blocked sites.
---

# Cloak Fetch

Fetch the rendered text content of a web page using CloakBrowser (stealth Chromium with 58+ C++ fingerprint patches). This bypasses Cloudflare Turnstile, reCAPTCHA, JS rendering requirements, and GFW blocking.

## Usage

```
/cloak-fetch <url> [--wait <ms>] [--no-proxy]
```

## When to use this skill

- WebFetch timed out or returned empty/truncated content
- The target site uses Cloudflare, reCAPTCHA, or other anti-bot systems
- The site requires JavaScript rendering (SPA, React, Vue)
- The site is blocked by GFW and needs a proxy

## Install

```bash
pip install cloakbrowser
```

CloakBrowser auto-downloads the stealth Chromium binary on first launch.

Optional extras:
```bash
pip install cloakbrowser[geoip]    # match timezone/locale to proxy IP
pip install cloakbrowser[patchright]  # alternative driver
pip install cloakbrowser[serve]    # web service mode
```

## Process

### 1. Determine if proxy is needed

- **Default: use proxy** — if the target is overseas or likely blocked
- **`--no-proxy`** — if the target is a domestic Chinese site

### 2. Fetch the page

```python
from cloakbrowser import launch

browser = launch(headless=True, humanize=True)
page = browser.new_page()
page.goto("<url>")
content = page.inner_text("body")
browser.close()
print(content)
```

- `--wait <ms>`: add `page.wait_for_timeout(<ms>)` before reading content
- `--proxy`: add `proxy="..."` to `launch()`

### 3. Present the result

Show the user the page title and content. Note any truncation.

## Notes

- CloakBrowser binary auto-downloads and caches on first launch (~200MB)
- First launch takes 3-5 seconds
- Passes Cloudflare Turnstile, reCAPTCHA (v3 score ~0.9), FingerprintJS
- Dodocker run --rm cloakhq/cloakbrowser cloaktest` for a quick test without install
