---
name: teaching-check-exercises
description: 给提示前必须核对已教知识点，确保不跳步
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

给提示前必须核对当天及之前教过的知识点，不要用未教的内容提示。如果最佳解法涉及未教内容（如 lambda），必须提供纯已教方案。

**Why:** 用户发现提示用到了未教知识点（如 lambda/sorted key），导致不自信，认为教学不严谨。

**How to apply:** 每次给提示前，先在脑子里过一遍这个知识点教了吗。如果没教，换纯已教方案提示；如果没教且没替代方案，直接说"这个知识点还没讲，需要现在讲吗"。
