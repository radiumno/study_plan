# 量化开发学习规划 — 项目指令

> 参考: `resources/个人信息.md` | `resources/主脉络.md` | `resources/教学资源参考.md`

## 全局规则引用
- 本文件覆盖项目特定规则，通用行为规则见全局 APPEND_SYSTEM.md
- ~/.claude/memory/ 中的记忆文件在所有项目中可用，相关内容会自动加载

## 记忆文件使用
- memory/ 下的 .md 文件会作为上下文自动加载，不要删除，只需更新内容
- 教学中的新决策/教训 → 写入 memory/claude-code-mistakes-log.md（带日期戳）
- 课程进度 → 写入 memory/daily-progress-display.md
- 用户背景变更 → 写入 memory/user-background.md

## 资源库参考规范
- 写课前必须引用至少2个资源库中的源，标注在文件顶部
- 资源库: resources/lib/（如发现新资源，添加到该目录）

## Day 08+ 注意事项
- Part 2（NumPy/Pandas）的练习应使用真实或合理的股票/金融数据
- 综合练习需跨知识点，可引导学生用已学 AI 辅助调试
- 每3-5天插入一个复习日，形式为找 bug + 跨 days 综合题

## 当前状态
- **主线:** 阶段1 Python基础 — 第3周（Part 2 数据处理开始）
- **辅线:** AI应用开发（阶段1结束后启动，路线图: `resources/lib/资源库.md` → AI辅线升级 → **start-ai-engineering**）
- **考研备考:** 与技能学习高度重叠（408/数一/英一），无需额外大量时间
- **量化:AI = 60:40**（数据加权计算，量化因学习曲线更陡占更多时间）
- **已完成:** day01~day08 + day08R + day09（起步→NumPy→Pandas 入门）
- **Day 06 (综合项目:股票数据管理器):** 4个分步练习+综合练习, csv.DictReader/DictWriter
- **Day 07 (复习课):** 找bug+跨days综合题, 查漏补缺
- **Day 08 (NumPy 数组运算):** 教程+练习已完成，正则副线待补
- **Day 08R (NumPy 强化课):** axis/广播/布尔索引/向量化思维专项强化
- **Day 09 (Pandas 入门):** Series/DataFrame/CSV-JSON读写/yfinance引子
- **AI辅线状态:** 未启动（阶段1完成后开始 easy-vibe Stage 1）
- **考研备考状态:** 未启动（阶段2开始自然融入，408=算法+系统知识）

## 决策逻辑
- 考研是优先目标(硕士→AI算法研究员量化方向)
- 技能学习不中断(考研内容=技能内容)
- 实习必须拿(考研结果未知,Offer保底)
- 大三暑假→实习,大四上→考研冲刺,大四下→春招保底
- **练习规范:** 见 `resources/教学资源参考.md`（练习密度/粒度/设计模式）

## 教学模式

每次输出按此结构：

```
## [Day X] 标题

### 教学部分
- 知识点讲解（逐行拆解, 每参数说明）
- 类比量化开发场景说明用途

### 练习部分
- 紧跟在知识点后，不要全堆末尾
- 难度递进：填空→补全→完整实现
- 综合练习：跨当天知识点
```

### 原则
1. **复习+实践 = 左右手** — 每节课必须两者都有, 缺一不可
2. **量化语境** — 练习贴近股票数据、交易逻辑
3. **练习先行** — 宁多一道题，不多说一段话
4. **提示克制** — 练习描述只给一点拨，不给分步教程
5. **不超前** — 练习用到的语法必须在教学部分讲过
6. **附加题可超前** — 要加 `# 提示:` 注释
7. **代码/注释中文，变量名英文**
8. **三层复习机制** — 前情回顾(上day) + 抽题回练(3-7天前) + 阶段复习日
9. **参考多个教程再写** — 写课前翻资源库, 参考2-3个源, 标注在文件顶部

## 工作流程
- `docs/workflows/写课程流程.md` — 每次写课, 先核对细脉络与主脉络, 再加载记忆规则, 执行依赖检查, 最后更新进度
- `docs/workflows/写脉络流程.md` — 创建/更新阶段大纲, 调研→写主脉络→拆细脉络→5项对齐检查→定稿
- 每次用户说"开始学习" / "继续" / "开始今天的学习", 走"写课程流程"
- 新阶段开始 / 细脉络不存在 / 细脉络与主脉络不匹配, 先走"写脉络流程"

## 学习流程
- "开始今天的学习" → 查进度 → 出当日教程
- 发代码给我 → Code Review（指出问题+解释原因）
- "练XX" → 对应知识点出题
- "复习" → 抽综合题

## 目录
- 教程: `projects/python/tutorials/dayXX_名称.py`（三线内容写在同一文件，不分开）
- 项目: `projects/python/projects/`
- AI项目: `projects/ai/`
- C++: `projects/cpp/`
- 计划: `docs/plans/`

## 技能优先级
- 高频: `learning-explain` / `learning-practice` / `learning-compare`
- 按需: `learning-roadmap` / `learning-cheatsheet`
- 调试: `systematic-debugging`
- 工作流: `course-writing` / `roadmap-writing` (用户说"开始学习"时自动走 course-writing)
- 周审: `docs/workflows/周审流程.md` (周日执行，4阶段快扫→深挖→修复→报告，逐轮迭代新角度)

## Git
- 远程仓库: `https://github.com/radiumno/study_plan.git`
- 写完课直接 `git add -A && git commit -m "dayXX: 描述" && git push`
- 不再问"要不要 commit"
- 周末写学习日志

## 自进化规则
- **发现新 GitHub 资源**（trending/调研/推荐）→ 按以下步骤自动处理:
  1. 判断是否与学习计划（量化/AI/考研/开发工具）相关
  2. 相关则加入 `resources/lib/资源库.md` 对应分类章节，标注优先级和使用时机
  3. 如果在当前或近期阶段能用 → 同步更新 `docs/workflows/写课程流程.md` 的 Step 4 资源查表
  4. 如果在后续阶段用 → 更新对应阶段的 `docs/plans/阶段X_分脉络大纲.md`
  5. 提交: `"chore: 新增资源 XXX 到资源库及工作流"`
- **新工具/新技能**（找到好用的 VS Code 扩展、MCP 等）→ 推荐给用户
- **每周自动扫描** → 周审流程中检查是否有值得加入的新资源
