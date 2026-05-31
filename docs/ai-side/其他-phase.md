---
title: AI 侧线 — 其他 Phase (CV/NLP/多模态/安全...)
tags: [AI侧线, 其他]
---

# 其他 AI 侧线 Phase

## Phase 4 — Computer Vision（28 节）

**路径：** `_ai_ref/phases/04-computer-vision/`

跟量化几乎无关，但如果你对"AI 怎么看世界"感兴趣：

| Lesson | 内容 | 推荐理由 |
|--------|------|---------|
| 02 | Convolutions from Scratch | 理解卷积操作本质 |
| 03 | CNNs: LeNet to ResNet | 15 年 CV 进化史 |
| 06 | Object Detection — YOLO from Scratch | 手撸目标检测 |
| 11 | Stable Diffusion — Architecture | 文生图原理 |
| 18 | Open-Vocabulary Vision — CLIP | 多模态基础 |
| 25 | Vision-Language Models | VLM 是什么 |

**跑一个：**
```bash
cd D:\Dev\AiProject\_ai_ref\phases\04-computer-vision\02-convolutions-from-scratch\code
python conv_from_scratch.py
```

---

## Phase 5 — NLP Foundations to Advanced（29 节）

**路径：** `_ai_ref/phases/05-nlp-foundations-to-advanced/`

跟量化的交叉点是情感分析（用于舆情因子）。但其他部分更大是语言模型基础。

| Lesson | 内容 | 推荐理由 |
|--------|------|---------|
| 01 | Text Processing: Tokenization | NLP 第一步 |
| 03 | Word2Vec from Scratch | 词向量手撸 |
| 10 | Attention Mechanism — The Breakthrough | 注意力本质 |
| 14 | Information Retrieval & Search | 搜索/检索 |
| 19 | Subword Tokenization: BPE, WordPiece | LLM 基础 |
| 23 | Chunking Strategies for RAG | 检索增强 |
| 27 | LLM Evaluation: RAGAS | 评估方法 |

---

## Phase 12 — Multimodal AI（25 节）

**路径：** `_ai_ref/phases/12-multimodal-ai/`

多模态模型（图文音视频统一理解），前沿方向，现阶段看看概念就好。

**核心概念：**
- CLIP — 图文对齐
- LLaVA — 视觉指令微调
- Computer Use — AI 操控电脑
- Omni Models — 统一输入输出

---

## Phase 15 — Autonomous Systems（22 节）

**路径：** `_ai_ref/phases/15-autonomous-systems/`

自我改进 AI + 安全栈。AI Scientists、Recursive Self-Improvement、Kill Switches、安全策略。

**值得看的：**
- 01 From Chatbots to Long-Horizon Agents
- 05 AI Scientist v2
- 13 Action Budgets & Cost Governors
- 14 Kill Switches & Circuit Breakers
- 19 Anthropic Responsible Scaling Policy

---

## Phase 16 — Multi-Agent & Swarms（25 节）

**路径：** `_ai_ref/phases/16-multi-agent-and-swarms/`

多智能体协作。涉及通信协议、协调模式、Agent 经济学。

**值得看的：**
- 05 Supervisor/Orchestrator-Worker Pattern
- 07 Society of Mind
- 12 A2A Protocol
- 17 Generative Agents
- 22 Production Scaling

---

## Phase 17 — Infrastructure & Production（28 节）

**路径：** `_ai_ref/phases/17-infrastructure-and-production/`

AI 模型部署、推理优化、GPU 扩缩容。

**值得看的（跟量化有交集的部分）：**
- 04 vLLM Serving Internals — 推理引擎
- 08 Inference Metrics — TTFT/TPOT
- 09 Production Quantization
- 25 Security — PII Scrubbing
- 27 FinOps for LLMs

---

## Phase 18 — Ethics, Safety & Alignment（30 节）

**路径：** `_ai_ref/phases/18-ethics-safety-alignment/`

安全和对齐。认知层面了解即可。

**值得看的：**
- 02 Reward Hacking
- 07 Sleeper Agents
- 12 Red-Teaming
- 20 Bias & Representational Harm
- 23 Watermarking

---

## Phase 19 — Capstone Projects（55 节）

**路径：** `_ai_ref/phases/19-capstone-projects/`

等你有了足够基础再回来看。17 个完整项目的设计思路值得学习。

**推荐项目（以后）：**
- 01 Terminal-Native Coding Agent — 跟 Hermes 同类
- 02 RAG over Codebase — 代码知识库
- 03 Real-Time Voice Assistant — 语音助手
- 06 DevOps Troubleshooting Agent — K8s排障
- 09 Code Migration Agent — 代码迁移
- 10 Multi-Agent Software Engineering Team — 多Agent开发团队
