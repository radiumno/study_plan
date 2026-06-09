---
name: search-mastery-lessons
description: 搜索能力最大化的操作原则和工具选择框架
metadata: 
  node_type: memory
  type: reference
  originSessionId: fdc89efa-5618-4e1d-9874-c9218d38b745
---

## 核心原则

1. **启动搜索前先确认用户背景** — 专业、约束条件、偏好。不然会默认假设错误。
2. **搜索范围要覆盖全国** — 不只限1~2个城市，不只限1种专业方向。
3. **每个数据标来源等级** — 🔵一手官方 / 🟢二手权威 / 🟡辅导机构 / 🔴论坛推测(不可用)。
4. **数据缺口不放弃** — 先用 cloak-fetch 抓官网，实在没有才承认。
5. **确认 Workflow 真正启动** — 调了 deep-research Skill 后还要确认 Workflow 工具被调用。

## 工具选择

- 单个数据 → WebSearch
- 官网打不开/图片数据 → cloak-fetch
- 系统性多角度研究 → deep-research workflow（要确认真正跑了）
- 自我纠偏 → 列出自设框架并反驳

## 薪资数据处理

新闻稿中的行业薪资数据是🟡级，JD上的薪资是🟢级。ROI推算中的年薪曲线必须标注"基于XX数据的推断"。

**Why:** 这次对话中我因为没标来源等级、搜索范围受限、默认用户背景等错误，被用户多次纠正。
**How to apply:** 每次做搜索任务前加载 `search-mastery` skill，按流程走。
