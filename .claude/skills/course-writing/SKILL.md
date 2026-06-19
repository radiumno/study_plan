---
name: course-writing
description: Write a daily lesson tutorial following the course-writing workflow — check progress, verify 细脉络 alignment, load memory rules, dependency-check, write tutorial, update progress, auto-commit. Use when the user says "start learning" / "continue" / "开始今天的学习" / "开始写课".
license: MIT
---

# Course Writing Workflow

每次用户说"开始今天的学习" / "开始写课" / "继续" 时, 走此流程.

## Workflow

### Step 0: 课前 commit
Before writing anything new, commit current working state:
```bash
git add -A && git commit -m "dayXX: 课前 checkpoint"
```
**不询问用户**, 直接执行 (per CLAUDE.md: "不再问要不要 commit").

### Step 1: 定位进度
Read `resources/主脉络.md` and `.claude/CLAUDE.md#当前状态` to determine current stage and day.

### Step 2: 核对细脉络
Check `docs/plans/阶段X_分脉络大纲.md`:
- **不存在?** -> Stop. Run `roadmap-writing` skill first.
- **对不上主脉络?** -> Stop. Update 细脉络 first.
- **吻合?** -> Proceed with the day's arrangement.

### Step 3: 加载记忆规则
Scan `.claude/memory/` directory. Mandatory rules:

| Memory | Constraint |
|--------|------------|
| teaching-explain-every-step | Break down every line and parameter. **No C++ comparison needed** |
| exercises-must-be-empty | Every `# ↓ 你的代码 ↓` must be blank below |
| exercise-hierarchy | 4-level structure: sub-topic → Part → Day → Week review |
| exercise-design-pattern | Adjust exercise count by difficulty (core = more exercises) |
| curriculum-prerequisite-check | Diff today's dependencies vs already-taught |
| daily-progress-display | Show progress bar at lesson start |
| english-punctuation | Code files: ASCII punctuation only |
| never-fabricate | Don't fake what wasn't done |
| sub-threads-research-based | Base teaching on 2-3 researched sources |

Also check `day09-review-lessons.md` for yfinance-specific notes.

### Step 4: 依赖检查
List all types/syntax used today. Confirm each was taught before or is taught today:
1. Scan today's tutorial and list every Python type/syntax/function used
2. Check against previous days (scan `day*.py` headers or `git log`)
3. If a dependency is missing, stop and add it to an earlier day first
4. Exception: "附加题" can use untaught syntax, but **must** have a `# 提示:` comment

### Step 5: 复习机制
Per CLAUDE.md 教学模式, every lesson starts with:
1. **上day核心复习** — 抽1-2道小题
2. **抽题回练** — 从3-7天前的练习抽1道

### Step 6: 写教程
Write `projects/python/tutorials/dayXX_名称.py`.

**常规课结构:**
```
### 复习环节 (每天必有)
练习1: 上day核心概念小题
练习2: 3-7天前知识回练

### 知识块1: [主题]
- 知识点1 → 练习1 (填空/补全)
- 知识点2 → 练习2 (填空/补全)
- ▸ 知识块1总练习 (跨该块所有知识点)

### 知识块2: [主题]
- 知识点2.1 → 练习2.1
- ...
- ▸ 知识块2总练习

### Day 综合练习 (跨所有块)
```
单个知识块 = 2~4个知识点 + 对应的填空/补全练习 + 末尾块总练习

**复习综合课结构 (每3-5天一次, 不教新内容):**
```
### 知识点回顾
- 过去N天的核心概念速查表

### 综合测试 (闭卷风格)
- 练习1-3: 单知识点加深
- 练习4-5: 跨天综合
- 练习6(选做): 附加挑战

### 自评
- 做完对答案, 标记薄弱环节
```

Rules:
- **No C++ comparison** (Phase 1 Python doesn't need it)
- **练习区必须留空** — 写完要反向检查
- **知识块内练习难度递进**: 填空→补全→完整实现
- **综合练习只用当天教过的知识点**, 超前的标为"选做"

### Step 7: 反向检查清单
After writing, verify ALL:

| Check | Standard |
|-------|----------|
| 1. 练习区留空 | Every `# ↓ 你的代码 ↓` below has no executable code |
| 2. 练习不泄漏答案 | Description says "what" not "how" |
| 3. 依赖完整 | All syntax used was taught before or today |
| 4. 每参数拆解 | Every function parameter explained |
| 5. 量化场景 | Every concept linked to a quant dev use case |
| 6. 提示克制 | Hints ≤ 2 sentences, not step-by-step |
| 7. 格式一致 | Separator style matches previous days |
| 8. yfinance安全(如有) | 美股非A股, 有NaN注释, 有多级索引说明 |

### Step 8: 更新进度
Update status in:
- `resources/主脉络.md (7.2 进度追踪 & 7.3 当前状态)`
- `docs/plans/阶段X_分脉络大纲.md (Day 标记)`
- `.claude/CLAUDE.md#当前状态`

### Step 9: 课后 auto-commit
```bash
git add -A && git commit -m "dayXX: 描述" && git push
```
**不询问用户**, 直接执行.

## Skills Reference
- 需要深入解释概念时 → 调用 `learning-explain` skill
- 需要生成额外练习时 → 调用 `learning-practice` skill
- 需要对比技术选项时 → 调用 `learning-compare` skill
- 需要创建速查表时 → 调用 `learning-cheatsheet` skill
- 需要创建/更新阶段规划时 → 调用 `roadmap-writing` skill

## Full Workflow File
For the complete detailed reference including examples, see `docs/workflows/写课程流程.md`.
