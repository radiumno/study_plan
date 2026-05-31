---
title: AI Engineering 整合索引
description: ai-engineering-from-scratch 与 study_plan 的对照融合
tags:
  - AI
  - 整合
  - 参考
date: 2026-05-29
---

# AI Engineering 整合索引

> 本文件是 `D:\Dev\AiProject\_ai_ref\` (ai-engineering-from-scratch, 23.7k stars)
> 与 study_plan 的桥梁。每条目标注：🟢融入主线 | 🟡AI侧线 | ⬜跳过

---

## 快速导航

| 分类 | 数量 | 说明 |
|------|------|------|
| 🟢 融入主线 | 6 Phase | 直接写进 study_plan 教案 |
| 🟡 AI 侧线 | 11 Phase | 单独放 `docs/ai-side/`，有空再学 |
| ⬜ 跳过 | 3 Phase | 跟你的方向完全不重叠 |

**本地路径：** `D:\Dev\AiProject\_ai_ref\phases\<NN>-<name>\`
**在线阅读：** https://aiengineeringfromscratch.com

---

## 🟢 融入 study_plan 主线

这些 Phase 的内容直接写进你的量化开发教案，遇到对应 Day/Phase 时翻过来跑一遍 code/。

### Phase 1 — Math Foundations（22 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段1 Day 08 (NumPy) | 02 Vectors, Matrices & Operations | 配合 NumPy 跑向量/矩阵运算 |
| 阶段1 Day 08 (NumPy) | 12 Tensor Operations | 高维数组理解 |
| 阶段4 量化核心·数学准备周 | 01 Linear Algebra Intuition | 线性代数直觉 |
| 阶段4 量化核心·数学准备周 | 04 Calculus for ML | 导数/梯度 |
| 阶段4 量化核心·数学准备周 | 06 Probability & Distributions | 概率基础 |
| 阶段4 量化核心·数学准备周 | 08 Optimization: Gradient Descent | 梯度下降 |
| 阶段4 量化核心·数学准备周 | 10 Dimensionality Reduction: PCA | 降维（因子模型前置） |

**code/ 路径：** `_ai_ref/phases/01-math-foundations/<NN>-<lesson>/code/`

---

### Phase 2 — ML Fundamentals（18 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段4 量化核心·ML基础周 | 01 What Is ML | 认知 |
| 阶段4 量化核心·ML基础周 | 02 Linear Regression from Scratch | **手撸线性回归** |
| 阶段4 量化核心·ML基础周 | 03 Logistic Regression | 分类 |
| 阶段4 量化核心·因子模型 | 08 Feature Engineering & Selection | 因子构建前置 |
| 阶段4 量化核心·因子模型 | 09 Model Evaluation | 回测评估方法 |
| 阶段4 量化核心·集成方法 | 11 Ensemble Methods | 随机森林/Boosting |

**code/ 路径：** `_ai_ref/phases/02-ml-fundamentals/<NN>-<lesson>/code/`

---

### Phase 3 — Deep Learning Core（13 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段4 量化核心·DL入门周 | 01 The Perceptron | 神经元基础 |
| 阶段4 量化核心·DL入门周 | 02 Multi-Layer Networks | 前向传播 |
| 阶段4 量化核心·DL入门周 | **03 Backpropagation from Scratch** | **手写反向传播** |
| 阶段4 量化核心·DL入门周 | 04 Activation Functions | ReLU/Sigmoid/GELU |
| 阶段4 量化核心·DL入门周 | 05 Loss Functions | MSE/Cross-Entropy |
| 阶段4 量化核心·DL入门周 | 06 Optimizers | SGD/Momentum/Adam |
| 阶段4 量化核心·DL入门周 | 11 Introduction to PyTorch | 框架入门 |

**code/ 路径：** `_ai_ref/phases/03-deep-learning-core/<NN>-<lesson>/code/`

---

### Phase 7 — Transformers Deep Dive（14 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段4 ML进阶·Transformer周 | 01 Why Transformers | 动机理解 |
| 阶段4 ML进阶·Transformer周 | **02 Self-Attention from Scratch** | **手撸注意力机制** |
| 阶段4 ML进阶·Transformer周 | 03 Multi-Head Attention | 多头注意力 |
| 阶段4 ML进阶·Transformer周 | 04 Positional Encoding | RoPE (当代LLM标配) |
| 阶段4 ML进阶·Transformer周 | 05 The Full Transformer | Encoder-Decoder |
| 阶段4 ML进阶·Transformer周 | 12 KV Cache & Flash Attention | 推理优化 |
| 阶段6 量化系统 | 13 Scaling Laws | 理解大模型规律 |

**code/ 路径：** `_ai_ref/phases/07-transformers-deep-dive/<NN>-<lesson>/code/`

---

### Phase 9 — Reinforcement Learning（12 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段4 RL入门周 | 01 MDPs, States, Actions & Rewards | 强化学习框架 |
| 阶段4 RL入门周 | 04 Q-Learning, SARSA | 基础算法 |
| 阶段4 RL入门周 | **05 Deep Q-Networks (DQN)** | **DL+RL 结合** |
| 阶段4 RL入门周 | 06 Policy Gradients — REINFORCE | 策略梯度 |
| 阶段4 RL入门周 | **07 Actor-Critic (A2C/A3C)** | **交易策略常用框架** |
| 阶段4 RL入门周 | **08 PPO** | **最流行的策略优化** |
| 阶段4 RL入门周 | 10 Multi-Agent RL | 多资产/多agent场景 |
| 阶段6 进阶 | 09 Reward Modeling & RLHF | 理解大模型训练 |

**code/ 路径：** `_ai_ref/phases/09-reinforcement-learning/<NN>-<lesson>/code/`

---

### Phase 11 — LLM Engineering（17 节课）

| 映射到 study_plan | 重点 Lesson | 怎么用 |
|------------------|------------|--------|
| 阶段4 数据工程 | 04 Embeddings & Vector Representations | 文本特征 |
| 阶段4 数据工程 | **06 RAG: Retrieval-Augmented Generation** | **研报分析/知识库** |
| 阶段4 数据工程 | 07 Advanced RAG | Chunking/Reranking |
| 阶段6 自动化工具 | 09 Function Calling & Tool Use | Agent 工具调用 |
| 阶段6 自动化工具 | 14 Model Context Protocol (MCP) | Agent 协议 |
| 阶段6 自动化工具 | 16 LangGraph | 状态机/AI工作流 |

**code/ 路径：** `_ai_ref/phases/11-llm-engineering/<NN>-<lesson>/code/`

---

## 🟡 AI 侧线（独立学习）

这些放 `docs/ai-side/`，不强制。你哪天想换脑子了走过来翻翻。每个 Phase 都包含完整的 doc narrative (en.md) + 可运行代码。

### Phase 4 — Computer Vision（28 节）

跟量化几乎无关，但这是理解现代 AI 视觉能力的必由之路。

**值得看的：**
- 02 Convolutions from Scratch — 卷积操作本质
- 03 CNNs: LeNet to ResNet — CV 进化史
- 18 Open-Vocabulary Vision — CLIP（多模态基础）
- 23 Diffusion Transformers — 最新图像生成架构

**路径：** `_ai_ref/phases/04-computer-vision/`

---

### Phase 5 — NLP Foundations to Advanced（29 节）

量化里偶尔用到（情感分析、研报分类），但不是核心。

**值得看的：**
- 01 Tokenization — NLP 的第一步
- 03 Word2Vec from Scratch — 词向量手撸
- 10 Attention Mechanism — 注意力机制（Transformer 前身）
- 19 Subword Tokenization — BPE/WordPiece（LLM基础）
- 23 Chunking Strategies for RAG — 检索相关

**路径：** `_ai_ref/phases/05-nlp-foundations-to-advanced/`

---

### Phase 6 — Speech & Audio（17 节）

兴趣方向，跟量化无关。

**路径：** `_ai_ref/phases/06-speech-and-audio/`

---

### Phase 8 — Generative AI（14 节）

图像/音频/3D 生成，纯兴趣。

**路径：** `_ai_ref/phases/08-generative-ai/`

---

### Phase 10 — LLMs from Scratch（22 节）

**推荐抽空看。** 理解 LLM 内部原理对你用好它们很有帮助。

**值得看的：**
- 01 Tokenizers — BPE/SentencePiece 原理
- 02 Building a Tokenizer from Scratch — 手撸分词器
- 04 Pre-Training a Mini GPT (124M) — 训练小GPT
- 06 Instruction Tuning — SFT 微调
- 11 Quantization — INT8/GPTQ/GGUF
- 20 DeepSeek-V3 Architecture — 最新架构

**路径：** `_ai_ref/phases/10-llms-from-scratch/`

---

### Phase 12 — Multimodal AI（25 节）

多模态（图文音视频），前沿方向但跟你现阶段距离远。

**路径：** `_ai_ref/phases/12-multimodal-ai/`

---

### Phase 13 — Tools & Protocols（23 节）

**推荐抽空看。** MCP (Model Context Protocol) 是 Agent 时代的基础设施。

**值得看的：**
- 02 Function Calling Deep Dive
- 06-14 MCP 系列（8节）— 构建 MCP Server/Client
- 19 A2A Protocol — Agent-to-Agent
- 22 Skills and Agent SDKs

**路径：** `_ai_ref/phases/13-tools-and-protocols/`

---

### Phase 14 — Agent Engineering（42 节）

**推荐。** Agent 是 AI 应用的核心范式，学会了对量化自动化和个人效率都有帮助。

**值得看的：**
- 01 The Agent Loop — 核心循环（120行Python）
- 07 Memory — Virtual Context & MemGPT
- 13 LangGraph — 状态图
- 14 AutoGen v0.4 — 多Agent框架
- 21 Computer Use — AI操控电脑
- 42 节完整看完可以做自己的 Agent

**路径：** `_ai_ref/phases/14-agent-engineering/`

---

### Phase 15 — Autonomous Systems（22 节）

自我改进 AI 系统 + 安全栈。前沿但远。

**路径：** `_ai_ref/phases/15-autonomous-systems/`

---

### Phase 16 — Multi-Agent & Swarms（25 节）

多智能体协作。有一定自动化价值。

**路径：** `_ai_ref/phases/16-multi-agent-and-swarms/`

---

### Phase 17 — Infrastructure & Production（28 节）

AI 模型部署/推理优化。跟量化的低延迟优化有交集，有空可以看。

**路径：** `_ai_ref/phases/17-infrastructure-and-production/`

---

### Phase 18 — Ethics, Safety & Alignment（30 节）

安全/对齐/红队。认知层面了解即可。

**路径：** `_ai_ref/phases/18-ethics-safety-alignment/`

---

### Phase 19 — Capstone Projects（55 节）

17 个完整项目 + 4 个深度构建轨道。等你有基础了再回来看。

**路径：** `_ai_ref/phases/19-capstone-projects/`

---

## ⬜ 跳过

| Phase | 原因 |
|-------|------|
| Phase 0 — Setup & Tooling | 你环境已经搭好了 |
| Phase 6 — Speech & Audio | 跟量化无关 |
| Phase 8 — Generative AI | 跟量化无关 |

---

## 使用方式

### 日常学主线时

遇到某个概念不熟（比如"反向传播到底怎么推导的"）：

```bash
# 打开对应 Lesson 的 code/ 目录
cd D:\Dev\AiProject\_ai_ref\phases\03-deep-learning-core\03-backpropagation-from-scratch\code\
# 跑一遍手撸代码
python backprop.py
```

### 想换脑子时

```bash
# 直接打开 AI 侧线目录
cd D:\Dev\AiProject\study_plan\docs\ai-side\
# 或者直接进 _ai_ref 翻
cd D:\Dev\AiProject\_ai_ref\phases\14-agent-engineering\01-the-agent-loop\code\
python agent_loop.py
```

### 我（Hermes）怎么帮你

- 学主线时遇到不懂的 → 跟我说"翻一下 _ai_ref Phase X Lesson Y 的 code/"
- 想开一个新 AI 侧线 Phase → 跟我说"学一下 Phase 14 Agent 工程"
- 我会自动去 _ai_ref 对应目录拿代码/doc 给你
