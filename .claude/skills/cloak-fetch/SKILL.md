---
name: cloak-fetch
description: >
  Fetch a rendered web page using CloakBrowser stealth browser, bypassing
  anti-bot detection (Cloudflare, reCAPTCHA) and GFW. Use when WebFetch
  fails on Cloudflare-protected, JS-heavy, or blocked sites.
---

# Cloak Fetch

Fetch the rendered text content of a web page using CloakBrowser (stealth Chromium with 49+ C++ fingerprint patches). This bypasses Cloudflare Turnstile, reCAPTCHA, JS rendering requirements, and GFW blocking.

## Usage

```
/cloak-fetch <url> [--no-proxy] [--wait <ms>]
```

## When to use this skill

- WebFetch timed out or returned empty/truncated content
- The target site uses Cloudflare, reCAPTCHA, or other anti-bot systems
- The site requires JavaScript rendering (SPA, React, Vue)
- The site is blocked by GFW and needs a proxy

## Process

### 1. Determine if proxy is needed

- **Default: use proxy** — if the target is overseas or likely blocked (github.com, google.com, stackoverflow.com, npm, pypi, etc.)
- **`--no-proxy`** — if the target is a domestic Chinese site (baidu.com, zhihu.com, etc.)

### 2. Start proxy (if needed and not already running)

```powershell
cd D:\Dev\AiProject\CloakAgent
.venv\Scripts\python scripts/start_proxy.py --bg
```

Wait 2 seconds for initialization.

### 3. Fetch the page

```powershell
cd D:\Dev\AiProject\CloakAgent
.venv\Scripts\python fetch_page.py <url> --headless [--proxy] --wait <wait_ms> --text
```

- Add `--proxy` if using VPN
- `--wait 3000` for normal sites, `--wait 8000` for heavy SPA

### 4. Present the result

Show the user the page title and content. Note any truncation.

### 5. Cleanup

If the user is done with overseas access, stop the proxy:

```powershell
cd D:\Dev\AiProject\CloakAgent
.venv\Scripts\python scripts/start_proxy.py --stop
```

If the user may need it again soon, leave the proxy running.

## Notes

- CloakBrowser binary cached at `.cloakbrowser_cache/` (~200MB)
- First launch takes 3-5 seconds
- Proxy (Clash.Meta) listens on `127.0.0.1:7890`
