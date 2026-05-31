---
title: AI 侧线 — Phase 14. Agent Engineering
tags: [AI侧线, Agent, Phase14]
---

# Phase 14 — Agent Engineering（42 节）

> **推荐度：** ⭐ **强烈推荐。** Agent 是 AI 应用的核心范式，42 节从零到生产，不管对你做量化自动化还是个人效率都极有价值。
> **本地路径：** `_ai_ref/phases/14-agent-engineering/`
> **预计时间：** 15-25 小时（分批看）

## 这 Phase 讲什么

这个 Phase 是这个仓库的明珠。42 节课，分成四段：

**核心 Agent（1-12）：** Agent 循环 → 规划（ReWOO/ToT/LATS）→ 记忆（MemGPT/Mem0）→ 工具调用 → 工作流模式

**框架层（13-18）：** LangGraph → AutoGen → CrewAI → OpenAI Agents SDK → Claude Agent SDK

**评估与观察（19-24）：** SWE-bench → WebArena → 计算机使用 → OpenTelemetry → Langfuse

**Agent Workbench（25-42）：** 一个完整的 Agent 开发工作台，从任务边界到验证门到多会话交接

## 推荐 Lesson

| 序号 | Lesson | 为什么看 |
|------|--------|---------|
| 01 | The Agent Loop | 120 行 Python 实现 Agent 核心循环。**必看** |
| 02 | ReWOO and Plan-and-Execute | 先规划再执行的模式 |
| 07 | Memory — Virtual Context and MemGPT | Agent 怎么记住东西 |
| 12 | Anthropic's Workflow Patterns | 实战工作流模式 |
| 13 | LangGraph — Stateful Graphs | 状态机驱动的 Agent |
| 16 | OpenAI Agents SDK | 手把手的 Agent 框架 |
| 21 | Computer Use | AI 操控电脑，最科幻的一节 |
| 25-42 | Agent Workbench 系列（12节） | 完整的 Agent 开发方法论 |

## 怎么跑

```bash
# 先跑 Agent 核心循环
cd D:\Dev\AiProject\_ai_ref\phases\14-agent-engineering\01-the-agent-loop\code
python agent_loop.py

# 再跑记忆系统
cd ..\07-memory\code
python memgpt_demo.py
```

## 跟主线的关系

中高相关：
- 学会搭 Agent，以后可以自己做量化研究助手（自动取数据 → 算因子 → 跑回测）
- Hermes 本身就是 Agent 系统，学了这个你也更理解我怎么工作的
- Agent Workbench 的方法论可以直接用到你的学习管理上
