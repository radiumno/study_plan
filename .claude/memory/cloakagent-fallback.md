---
name: cloakagent-fallback
description: "当 WebSearch/WebFetch 不可用时, 使用 CloakAgent 浏览器工具作为替代"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8e81202e-727c-4fbc-9688-56fc1d1ea5a6
---

当标准搜索/抓取工具不可用时的保底方案:

**工具路径:** `D:\Dev\AiProject\CloakAgent\fetch_page.py`

**执行方式:**
```bash
cd D:/Dev/AiProject/CloakAgent
.venv/Scripts/python.exe fetch_page.py <url> --headless --proxy --text --timeout 30
```

**代理:** 需要先启动 ChromeGo 代理
```bash
cd D:/Dev/AiProject/CloakAgent
.venv/Scripts/python.exe scripts/start_proxy.py --bg   # 启动
.venv/Scripts/python.exe scripts/start_proxy.py --stop  # 停止
```

**注意事项:**
- 直连访问国内站不需要 `--proxy`
- 访问外网 (GitHub, 国外网站) 必须加 `--proxy`
- 输出首行有 `Update available: cloakbrowser` banner, 实际内容从第二行开始
- 用 `--output <path>` 保存到文件再读取, 避免 JSON 解析被 banner 干扰
