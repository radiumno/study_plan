---
name: roadmap-writing
description: Create or update a stage roadmap with 细脉络 — research online tutorials, read job data + resource library, write 主脉络, break into 细脉络 daily plans, run 5-point alignment check, finalize. Use when a new stage begins, 细脉络 is missing, or 细脉络 doesn't match 主脉络.
license: MIT
---

# Roadmap / 脉络 Writing Workflow

当需要创建新阶段大纲或更新现有大纲时, 按此流程执行.
触发条件: 新阶段开始 | 细脉络不存在 | 细脉络与主脉络不匹配

## Workflow

### Step 1: 调研
Search quality Python/C++/quant-dev tutorials. Understand:
- How mainstream courses organize topics
- What each stage covers
- Exercise/project design patterns

Reference sources:
- Python: CS50P, Real Python, Python Official Tutorial, Exercism
- C++: learncpp.com, cppreference
- Quant dev: job market data for required skills

### Step 2: 读招聘数据 + 资源库
Confirm market demand and existing resources:
- `resources/lib/资源库.md` — available books/tutorials
- Job market research — which skills are required
- User background (`个人信息.md`) — time budget, target city, priorities

### Step 3: 写主脉络
Write `resources/主脉络.md` with:
1. **Stage breakdown** — 6 stages: Python -> C++ -> Data Structures -> Data Processing -> Database -> Quant入门
2. **Skill-to-job mapping table** — each skill maps to job requirements
3. **Milestones** — what user can do at end of each stage

### Step 4: 拆细脉络
Create `docs/plans/阶段X_分脉络大纲.md` day-by-day:

```
## Day Y - Title

### Teaching Content
- Knowledge points list (with prerequisite markers)
- C++ comparison points
- Quant scenario

### Exercise Plan
- Basic exercises: count, what they test
- Comprehensive exercise: description

### Dependency Checklist
All Python types/syntax used this day, annotated with source day
```

### Step 5: 自我审查 (写脉络前先回答这几个问题)

动笔前想清楚, 回答不上来就别写:

```
1. 这个脉络为什么这样安排? 教学顺序有科学依据吗?
   → 参考了哪些课程/教程? 学了A对学B有什么帮助?

2. 和岗位要求对得上吗?
   → 每个Day的内容直接对应(招聘市场调研报告.md)里的哪条JD要求?
   → 如果对不上, 删掉还是再加?

3. 和用户目标对得上吗?
   → 量化开发主目标? AI辅线? 考研重叠?
   → 这个阶段学完用户能做什么原来不能做的?

4. 节奏合理吗?
   → 知识点太多?(一个知识块≤4个) 练习够?(每知识点≥1个)
   → 有复习日/综合测试日吗?(每3-5天一次)
```

### Step 6: 对齐检查 (5项)

| Check | Standard | If fails |
|-------|----------|---------|
| 1. 主脉络 vs job needs | Every knowledge point maps to a job requirement? | Add/remove skills |
| 2. 细脉络 vs 主脉络 | 细脉络 covers all of 主脉络's stage content? | Adjust 细脉络 |
| 3. Internal deps | Day N's prerequisites taught in Day < N? | Reorder |
| 4. Exercises vs topics | Every topic has corresponding exercises? | Add exercises |
| 5. Memory rules | Step-by-step breakdown? ASCII punctuation? Difficulty progression? | Fix teaching style |

### Step 6: 定稿
- Update `resources/主脉络.md`
- Create/update `docs/plans/阶段X_分脉络大纲.md`
- If new teaching constraints emerged, write to memory/
- Update `.claude/CLAUDE.md#当前状态`

## Full Workflow File
For the complete detailed reference including examples, see `docs/workflows/写脉络流程.md`.
