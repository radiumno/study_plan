---
title: AI辅线 — 分脉络大纲
description: 与量化主线并行的AI学习路径，按阶段分解
tags:
  - AI
  - 辅线
  - 规划
date: 2026-06-04
---

# AI辅线 — 分脉络大纲

> 量化:AI = 60:40(时间分配)。辅线学习不单独占白天时段，利用周末/假期/晚间。

---

## 对齐关系：量化主线 ↔ AI辅线

| 量化主线阶段 | 对应AI辅线内容 | 时间安排 | 比例 |
|------------|--------------|---------|------|
| 阶段1 Python基础 | easy-vibe Stage 1(搭原型) | 暑假周末 | 90:10 |
| 阶段2 C++算法 | PyTorch入门(土堆教程) | 周末/晚间 | 80:20 |
| 阶段3 C++深入 | Transformer原理(Happy-LLM前5章) | 寒假 | 70:30 |
| **阶段4 量化核心** | **LangChain/RAG/Agent(LLM Cookbook)** | **正式并行** | **60:40** |
| 阶段5 实习 | AI应用开发实习(保底) | 暑假 | 按需 |
| 阶段6 冲刺 | AI应用面试准备(备选) | 并行 | 60:40 |

---

## 详细安排

### 阶段1(平行): easy-vibe Stage 1

**时机:** Day30+ 开始, 不早于Python基础完成80%
**预计耗时:** 2-3周周末, 每天1-2小时
**学习方式:** 跑easy-vibe代码, 感受AI编程工作流(Claude Code/Cursor)
**产出:** 用自然语言搭建1-2个小原型
**资源:** `resources/lib/资源库.md` → easy-vibe(15.8k⭐)

### 阶段2(平行): PyTorch入门

**时机:** 阶段2中期(数据结构完成后)开始
**预计耗时:** 4周周末, 每天1-2小时
**学习方式:**
1. 土堆PyTorch教程:BV1hE411t7RN(22节,约10h)
2. 配合官方PyTorch教程实践
**产出:** 能写简单神经网络(Python/PyTorch)
**资源:** `resources/lib/资源库.md` → 土堆PyTorch / zh.d2l.ai

### 阶段3(平行): Transformer原理理解

**时机:** 寒假, 与C++深入并行
**预计耗时:** 2~3周,每天1-2小时
**学习方式:**
1. Happy-LLM前5章: Transformer架构→手搭LLaMA2原理
2. The Illustrated Transformer(可视化理解)
3. Tiny-Universe手写TinyTransformer
**产出:** 理解Transformer核心机制(Attention/QKV等)
**资源:** Happy-LLM(10.8k⭐) / The Illustrated Transformer

### 阶段4(正式并行): LangChain/RAG/Agent全链路

**时机:** 大二下, 与量化核心并行
**预计耗时:** 40%学习时间
**学习方式:**
1. LLM Cookbook(15.8k⭐) — RAG+Agent实战
2. LLM-Universe(6.8k⭐) — 知识库项目
3. LangChain B站教程:BV17jhTzCEMV(最全面)
4. Tiny-Universe手写TinyRAG/TinyAgent
**产出:**
- RAG知识库问答系统(核心项目)
- AI Agent(功能型)
**资源:** `resources/lib/资源库.md` 第五章全

### 阶段5-6(就业保底)

**AI应用开发保底方向:**
- 目标岗位: AI应用开发工程师 / AI Agent开发
- 薪资范围: 25~45万(应届)
- 岗位情况: 2025年AI岗位7.2万个,同比+543%
- 准备方式: 用阶段4的项目做简历,投AI应用岗实习

---

## 进度追踪

| 阶段 | 状态 | 位置 |
|------|------|------|
| easy-vibe Stage 1 | ⏳ 待开始 | `projects/ai-engineering` |
| PyTorch入门 | ⏳ 待开始 | — |
| Transformer原理 | ⏳ 待开始 | — |
| LangChain/RAG/Agent | ⏳ 待开始 | — |
| AI实习/就业 | ⏳ 待定 | — |

> 量化主线进度见 `resources/主脉络.md` 进度追踪
