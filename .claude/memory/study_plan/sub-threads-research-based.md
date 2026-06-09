---
name: sub-threads-research-based
description: 分脉络（阶段大纲）基于网络教程调研 + 用户目标背景编写
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

每个学习阶段（如阶段1 Python、阶段2 C++等）需要撰写分脉络文档，详细说明该阶段的大纲、每日安排、知识点覆盖、对应岗位要求。

分脉络的编写要求：
1. 必须通过网络搜索调研现有的优质教程（如 CS50P、Real Python、Exercism、Python官方文档等），了解这些课程是怎么组织知识点的
2. 结合用户的目标（量化开发工程师）和背景（地大数据科学专业，大一升大二，有一定Python基础）做裁剪
3. 与招聘数据（主脉络中的技能-岗位映射表）对齐——确保教的是岗位要求的
4. 不能照搬任何单一课程，要综合多来源后自己组织

**Why:** 用户要求教学要有依据，不能只凭模型训练知识来教。结合真实网络教程和真实招聘数据，用户才知道为什么学这个、为什么这个顺序。

**How to apply:** 每进入一个新阶段前，先做网络调研，把调研结果和分脉络文档一起给出。分脉络文档存放在 `docs/superpowers/plans/` 目录下，命名格式 `阶段X_名称_依据.md`。
