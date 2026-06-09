---
name: english-punctuation
description: "全程使用英文符号, 不在代码/注释/教学字符串中使用中文全角标点"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8e81202e-727c-4fbc-9688-56fc1d1ea5a6
---

所有代码文件、注释、教学字符串中全程使用英文 ASCII 符号，禁用中文全角标点。

**Why:** 用户视觉偏好，中文全角符号在代码编辑器中与英文符号混排不协调。

**How to apply:**
- `（` → `(`, `）` → `)`
- `、` → `,`  
- `，` → `,`
- `：` → `:`
- `！` → `!`
- `。` → `.`
- `·` → `-`
- `—` → `--`
- 中文字符串内容里的标点也必须用英文，不能偷懒保留全角符号
- 只在纯中文文档文件（如 resources/*.md）里可以酌情保留，但代码文件一律全改
