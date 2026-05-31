---
title: AI 侧线 — 独立学习大纲
description: 跟量化开发主线无关的 AI 工程内容，有兴趣时单独学
tags:
  - AI
  - 侧线
  - 兴趣
date: 2026-05-29
---

# AI 侧线 — 独立学习大纲

> **本目录放什么：** 跟 study_plan 量化开发主线不直接重叠的 AI 工程内容。
> 你哪天想换脑子、对 AI 某个方向感兴趣了，过来挑一个 Phase 翻翻。
>
> 所有代码和教案都在 `D:\Dev\AiProject\_ai_ref\phases\` 下，不用额外下载。

---

## 快速入口

| Phase | 节数 | 你会学到 | 值得花时间吗 |
|-------|------|---------|------------|
| [Phase 10 — LLMs from Scratch](./phase-10-llms-from-scratch.md) | 22 | 手撸分词器→训练124M GPT→量化→DeepSeek架构 | ⭐ **推荐** |
| [Phase 13 — Tools & Protocols](./phase-13-tools-and-protocols.md) | 23 | MCP协议→Function Calling→A2A→Agent SDK | ⭐ **推荐** |
| [Phase 14 — Agent Engineering](./phase-14-agent-engineering.md) | 42 | Agent循环→记忆→规划→多Agent框架→Workbench | ⭐ **强烈推荐** |
| [Phase 4 — Computer Vision](./phase-04-computer-vision.md) | 28 | CNN→YOLO→Diffusion→SAM→VLM | 偶尔看看 |
| [Phase 5 — NLP](./phase-05-nlp.md) | 29 | 分词→词嵌入→Seq2Seq→Attention→RAG | 挑着看 |
| [Phase 12 — Multimodal AI](./phase-12-multimodal.md) | 25 | CLIP→LLaVA→Computer Use→Omni模型 | 偶尔看看 |
| [Phase 15 — Autonomous Systems](./phase-15-autonomous.md) | 22 | 自我改进→安全栈→Kill Switch→RSP | 偶尔看看 |
| [Phase 16 — Multi-Agent](./phase-16-multi-agent.md) | 25 | 协调→MARL→Agent经济→生产级扩展 | 偶尔看看 |
| [Phase 17 — Infrastructure](./phase-17-infra.md) | 28 | vLLM→SGLang→TensorRT→GPU→合规 | 偶尔看看 |
| [Phase 18 — Ethics](./phase-18-ethics.md) | 30 | RLHF→Constitutional AI→红队→水印 | 了解即可 |
| [Phase 19 — Capstone](./phase-19-capstone.md) | 55 | 17个完整项目 (Agent/RAG/Voice/Multi-Agent...) | 有基础再回看 |

---

## 怎么学

### 方式一：直接去 _ai_ref 翻 code/

```bash
cd D:\Dev\AiProject\_ai_ref\phases\14-agent-engineering\01-the-agent-loop\code\
python agent_loop.py
```

每个 lesson 的 `docs/en.md` 是教案，`code/` 是可运行代码。

### 方式二：让我带你

跟我说一句：
- "学一下 Phase 14 Agent 工程"
- "看看 Phase 10 的 GPT 训练"
- "跑一下 Phase 13 的 MCP Server"

我会自动去对应目录拿内容，出题或讲解。

### 方式三：在线阅读

https://aiengineeringfromscratch.com

---

## 学习建议

- **不赶进度。** 这是副线，跟量化主线不冲突
- **一次只开一个 Phase。** 不要同时开两三条侧线
- **如果主线进度慢了，优先停侧线。** 量化开发是正事
- **跑 code/ 比读 docs/ 重要。** 动手跑一遍比看十遍管用
