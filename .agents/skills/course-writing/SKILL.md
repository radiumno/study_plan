---
name: course-writing
description: Write or continue a daily lesson for this study-plan repo — locate the current day, verify 细脉络 alignment, load project rules, dependency-check, write the lesson, update progress, and commit scoped lesson changes. Use when the user says "start learning" / "continue" / "开始今天的学习" / "开始写课".
license: MIT
---

# Course Writing Workflow

当用户说“开始今天的学习”“开始写课”“继续”时，使用这个流程。

## Workflow

### Step 1: 定位进度

先读取：

- `resources/主脉络.md`
- 当前阶段对应的 `docs/plans/阶段X_分脉络大纲.md`
- `vault/会话交接.md`
- 根 `AGENTS.md`

确定当前阶段、当前 day、下一课目标，以及上次会话停在哪里。

### Step 2: 核对细脉络

检查 `docs/plans/阶段X_分脉络大纲.md`：

- 不存在：停止，先走 `roadmap-writing`
- 与主脉络不一致：先修细脉络
- 一致：继续

### Step 3: 加载项目规则

优先使用仓库内当前有效规则：

- 根 `AGENTS.md`
- `docs/workflows/写课程流程.md`
- `.claude/memory/` 中与写课直接相关的记忆

如果历史记忆与当前仓库文件冲突，以根 `AGENTS.md` 和 workflow 文档为准。

### Step 4: 准备参考源

写课前至少准备 2 个参考源，优先顺序：

1. `resources/lib/资源库.md` 中的对应资源
2. 官方文档或原始教程
3. 与当前 day 高度相关的 GitHub / 视频 / 社区资料

如果需要联网搜索，先读 `search-mastery`，再用当前 Codex 可用工具执行。

### Step 5: 依赖检查

列出当天会出现的：

- Python 语法
- 标准库或第三方库 API
- 数据结构
- 新概念

确认它们是否在之前 days 已教，或会在当天先教后用。

如果前置缺失，先修计划，不要直接硬写。

### Step 6: 写教程

目标文件通常是：

- `projects/python/stage1_python基础/dayXX_名称.py`
- `projects/python/stage2_数据处理/dayXX_名称.py`
- `projects/python/stage3_项目实战/dayXX_名称.py`

执行规则：

- 复习题数量按前一天知识块数量设置
- 保持“知识点1.1 -> 练习1.1.x -> 知识点1.2 -> 练习1.2.x -> 总练习1.x”的知识块结构
- 练习数量按知识点难度、重要程度和用户薄弱程度动态调整
- 简单知识点可 1 道题；核心或易错知识点可 2-3 道题；知识块总练习通常 1 道，复杂块可 2 道
- 知识点和练习必须紧挨
- 练习只说 what，不说 how
- `# ↓ 你的代码 ↓` 下方默认留空
- 每个知识点都解释量化场景用途
- 文件顶部标注参考源

### Step 7: 反向检查

写完后至少检查：

| 检查项 | 标准 |
|--------|------|
| 练习区留空 | `# ↓ 你的代码 ↓` 下方没有残留答案 |
| 练习不泄漏答案 | 题目只说做什么，不说做法 |
| 依赖完整 | 没有未讲先用 |
| 量化语境 | 每块内容与量化场景有清晰连接 |
| 格式一致 | 与已有 day 文件风格一致 |
| 知识点→练习紧挨 | 每个知识点后紧跟对应练习 |
| 练习数量合理 | 按难度和重要程度动态调整，不机械固定 |
| 知识块总练习 | 每个知识块结束有总练习，复杂块可多一道 |

### Step 8: 更新进度与交接

通常要同步：

- `resources/主脉络.md`
- 对应 `docs/plans/阶段X_分脉络大纲.md`
- `vault/会话交接.md`

如果这次写课形成了长期稳定规则，再更新根 `AGENTS.md` 或 workflow 文档。

### Step 9: 提交

当课程内容完整、检查通过、改动范围清晰时，再提交本次任务相关文件。
不要为了 checkpoint 制造额外 commit。

## Skills Reference

- 深入解释概念：`learning-explain`
- 增补练习：`learning-practice`
- 技术或方案对比：`learning-compare`
- 生成速查表：`learning-cheatsheet`
- 当前阶段规划失配：`roadmap-writing`

## Full Workflow File

完整细节见 `docs/workflows/写课程流程.md`
