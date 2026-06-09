---
name: course-and-roadmap-workflows
description: "写课程和写脉络两条工作流程, 每次动手前自查"
metadata: 
  node_type: memory
  type: reference
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

有两个工作流程文件, 每次写课或写脉络前必须核对. 已封装为 skills

## 写课程流程
`docs/workflows/写课程流程.md` | skill: `course-writing`
- 触发: 用户说"开始学习" / "继续" / "开始今天的学习"
- 7步: 定位进度 -> 核对细脉络 -> 加载记忆规则 -> 依赖检查 -> 写教程 -> 更新进度 -> 问commit
- 关键: 细脉络不存在或对不上主脉络时, 先走"写脉络流程"再回来

## 写脉络流程
`docs/workflows/写脉络流程.md` | skill: `roadmap-writing`
- 触发: 新阶段开始 / 细脉络不存在 / 细脉络与主脉络不匹配
- 6步: 调研 -> 读招聘数据+资源库 -> 写主脉络 -> 拆细脉络 -> 对齐检查(5项) -> 定稿

**Why:** 之前出现过跳过细脉络直接写课, 导致内容混乱的问题. 两条流程确保每次写课都有依据、有对齐检查.

**How to apply:**
1. 听到"开始学习", 立即加载"写课程流程"
2. 写课前先检查 `docs/plans/` 下对应阶段的细脉络是否存在
3. 如果细脉络不存在 -> 走"写脉络流程"创建
4. 每次写课按 `teaching-explain-every-step` 规则逐行拆解

Related: [[teaching-explain-every-step]], [[daily-progress-display]], [[english-punctuation]]
