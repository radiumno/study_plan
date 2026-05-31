---
title: AI 侧线 — Phase 10. LLMs from Scratch
tags: [AI侧线, LLM, Phase10]
---

# Phase 10 — LLMs from Scratch（22 节）

> **推荐度：** ⭐ 推荐。理解 LLM 内部原理对用好它们非常有帮助。
> **本地路径：** `_ai_ref/phases/10-llms-from-scratch/`
> **预计时间：** 12-15 小时（挑着看）

## 这 Phase 讲什么

从零构建一个 LLM：手写 tokenizer → 构建训练数据集 → 预训练一个 124M 参数的 mini GPT → SFT 微调 → RLHF/DPO → 量化部署 → 推理优化。最后还带你看了 DeepSeek-V3 和 Jamba 的架构。

## 推荐 Lesson

| 序号 | Lesson | 为什么看 |
|------|--------|---------|
| 01 | Tokenizers: BPE, WordPiece, SentencePiece | 所有 LLM 的第一步，理解文字怎么变成数字 |
| 02 | Building a Tokenizer from Scratch | 手撸一个，不再觉得 Tokenizer 是黑盒 |
| 04 | Pre-Training a Mini GPT (124M) | **核心。** 训练一个小 GPT，理解预训练全过程 |
| 06 | Instruction Tuning — SFT | 理解"教模型听话"的原理 |
| 07-08 | RLHF / DPO | 对齐训练的核心技术 |
| 11 | Quantization: INT8, GPTQ, AWQ, GGUF | 模型压缩，跑大模型必备 |
| 12 | Inference Optimization | 推理加速，实用 |
| 20 | DeepSeek-V3 Architecture Walkthrough | 看看国产最强开源模型怎么设计的 |

## 怎么跑

```bash
# 手撸 tokenizer
cd D:\Dev\AiProject\_ai_ref\phases\10-llms-from-scratch\02-building-a-tokenizer-from-scratch\code
python tokenizer.py

# Mini GPT 训练
cd ..\04-pre-training-a-mini-gpt\code
# 可能需要 GPU，先看 doc 理解流程
```

## 跟主线的关系

间接帮助：
- 理解 LLM 能力边界（你以后用 LLM 做自动化就知道什么能做什么不能）
- RAG 用到 Embedding，知道它怎么来的
- 量化（模型量化技术）跟你的量化开发没有关系但名字一样有意思
