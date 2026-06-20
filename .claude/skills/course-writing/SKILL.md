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

### Step 1: 定位进度 + 重建周审 cron
Read `resources/主脉络.md` and `.claude/CLAUDE.md#当前状态` to determine current stage and day.
同时检查周审 cron 是否还在 (用 CronList), 不在就重建: 周日 9:08, durable:true.

### Step 2: 核对细脉络
Check `docs/plans/阶段X_分脉络大纲.md`:
- **不存在?** -> Stop. Run `roadmap-writing` skill first.
- **对不上主脉络?** -> Stop. Update 细脉络 first.
- **吻合?** -> Proceed with the day's arrangement.
- **注意细脉络是否有 `[资源扫描]` 或 `[大审查]` 标记** -> 按标记执行

### Step 2.5: 课前快速资源扫描 (每次写课前必做)
Quick WebSearch for new resources relevant to today's topic:
- 搜今日知识点的最新教程/工具 (eg: 写 Matplotlib 就搜 "Matplotlib 2026 教程 最新")
- 搜 GitHub Trending 该方向有没有新项目
- 有合适的直接更新到 `resources/lib/资源库.md`，本次写课就用上
- ⏱ 5分钟，别拖太久

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
Write `projects/python/stageN_阶段名/dayXX_名称.py` (根据当前阶段选 stage1_python基础 / stage2_数据处理 / stage3_项目实战).

**常规课结构:**
```
### 复习环节 (每天必有, 约10-15min)
练习R1: 上day核心概念小题
练习R2: 3-7天前知识回练

### 知识块1: [主题]
知识点1.1 ──→ 练习1.1 (填空)
知识点1.2 ──→ 练习1.2.1, 练习1.2.2, 练习1.2.3 (补全, 难就多练)
知识点1.3 ──→ 练习1.3 (完整实现)
▸ 知识块1总练习 (跨该块所有知识点)

### 知识块2: [主题]
知识点2.1 ──→ 练习2.1
...
▸ 知识块2总练习

### Day 综合练习 (跨所有块)
```

编号规则:
- `练习R1/R2` = 复习环节
- `练习1.1` = 知识块1, 知识点1
- `练习1.2.1` = 知识块1, 知识点2, 子练习1 (知识点难就分多个子练习)
- `练习2.1` = 知识块2, 知识点1
- `块总练习` = 不带编号, 标 `▸` 符号

**铁律: 知识块内必须是"知识点→练习紧挨", 禁止先教一堆再练一堆.**
- 每写完一个知识点的 teaching 代码, 立即紧跟该知识点的练习
- 格式: `知识点X.X (teaching) → 练习X.X (填空/补全) → 下一知识点`
- 知识点难可以拆多个子练习: `练习1.2.1, 练习1.2.2, 练习1.2.3`
- 且不能出现 `# 提示:` 或任何等同于提示的步骤指引
- 练习描述只说"做什么"(what), 不说"怎么做"(how)
- 变量名、数据结构、函数名都不能在描述里给
- 超出当天知识点的附加题可以有提示, 但必须标注 `(选做)`

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
| 6. 禁止提示 | Exercise descriptions say "what" not "how", no `# 提示:` lines |
| 7. 格式一致 | Separator style matches previous days |
| 8. 知识点→练习紧挨 | Teaching→exercise 是紧挨的, 不是先教一堆再练一堆 |

### Step 7.5: 结构复查
Before updating progress, do a quick second-pass check:
- [ ] 本课所有 `知识点X.X` 的 teaching 代码后面, 是不是立即跟着对应的 `练习X.X`?
- [ ] 练习区有没有泄漏答案的注释或 `# 提示:`?
- [ ] 脉络里对这个 Day 的描述能对上吗?(读一遍细脉络)
- [ ] 用户目标(量化开发/考研/AI)和岗位要求(数据处理是面试必考)覆盖了吗?

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
