---
title: AI 侧线 — Phase 13. Tools & Protocols
tags: [AI侧线, MCP, 工具, Phase13]
---

# Phase 13 — Tools & Protocols（23 节）

> **推荐度：** ⭐ 推荐。MCP (Model Context Protocol) 是 Agent 时代的基础设施，对你做自动化工具很有用。
> **本地路径：** `_ai_ref/phases/13-tools-and-protocols/`
> **预计时间：** 6-8 小时（核心 8 节）

## 这 Phase 讲什么

AI 和现实世界之间的接口。Function Calling → Structured Output → MCP 协议全家桶（Server/Client/Transport/Security）→ A2A 协议 → OpenTelemetry → 路由层。

## 推荐 Lesson

| 序号 | Lesson | 为什么看 |
|------|--------|---------|
| 01 | The Tool Interface | 理解"工具"的抽象 |
| 02 | Function Calling Deep Dive | 深入理解 LLM 怎么调用函数 |
| 06 | MCP Fundamentals | MCP 是什么，为什么重要 |
| 07 | Building an MCP Server | **手撸一个 MCP Server** |
| 08 | Building an MCP Client | 连接 MCP Server |
| 14 | MCP Apps | 完整 MCP 应用 |
| 19 | A2A Protocol | Agent-to-Agent 通信协议 |
| 22 | Skills and Agent SDKs | 技能系统是什么 |

## 怎么跑

```bash
cd D:\Dev\AiProject\_ai_ref\phases\13-tools-and-protocols\07-building-an-mcp-server\code
python mcp_server.py
```

## 跟主线的关系

中高相关：
- Function Calling 是你以后用 LLM 做量化自动化的基础（比如让 AI 帮你取数据、算指标）
- MCP 是未来 Agent 的标准协议，学会了你就能自己搭 AI 工具链
- 跟量化开发的多线程/网络编程有概念上的互通
