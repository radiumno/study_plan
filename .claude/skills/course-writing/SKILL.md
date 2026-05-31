---
name: course-writing
description: Write a daily lesson tutorial following the course-writing workflow — check progress, verify 细脉络 alignment, load memory rules, dependency-check, write tutorial, update progress, ask for commit. Use when the user says "start learning" / "continue" / "开始今天的学习" / "开始写课".
license: MIT
---

# Course Writing Workflow

每次用户说"开始今天的学习" / "开始写课" / "继续" 时, 走此流程.

## Workflow

### Step 1: 定位进度
Read `resources/主脉络.md` and `.claude/CLAUDE.md#当前状态` to determine current stage and day.

### Step 2: 核对细脉络
Check `docs/plans/阶段X_分脉络大纲.md`:
- **不存在?** -> Stop. Run `roadmap-writing` skill first.
- **对不上主脉络?** -> Stop. Update 细脉络 first.
- **吻合?** -> Proceed with the day's arrangement.

### Step 3: 加载记忆规则
Scan MEMORY.md. Confirm these rules are loaded:

| Memory | Constraint |
|--------|------------|
| english-punctuation | Code files: ASCII punctuation only, no Chinese full-width |
| teaching-explain-every-step | Break down every line and parameter |
| teaching-check-exercises | Check taught content before giving hints |
| curriculum-prerequisite-check | Diff today's dependencies vs already-taught |
| exercise-design-pattern | Adjust exercise count by difficulty |
| never-fabricate | Don't fake what wasn't done |
| daily-progress-display | Show progress bar at lesson start |
| sub-threads-research-based | Base teaching on researched sources |

### Step 4: 依赖检查
List all types/syntax used today. Confirm each was taught before or is taught today.

### Step 5: 写教程
Write `projects/python/tutorials/dayXX_名称.py` per 细脉络 + memory rules.

Structure:
```
## [Day X] 标题

### 教学部分
- Parameter-by-parameter breakdown
- Python vs C++ comparison
- Quant development context

### 练习部分
- After each knowledge point (not all at end)
- Difficulty progression: fill-in -> complete -> full implementation
- Comprehensive exercise crossing today's topics
```

### Step 6: 更新进度
Update status in:
- `resources/主脉络.md`
- `docs/plans/阶段X_分脉络大纲.md`
- `.claude/CLAUDE.md#当前状态`

### Step 7: 问 commit
After lesson, ask user whether to commit. Format: `dayXX: brief description`

## Full Workflow File
For the complete detailed reference including examples, see `docs/workflows/写课程流程.md`.
