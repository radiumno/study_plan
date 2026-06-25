# 量化开发学习规划 — 项目指令

这个仓库是学习规划和课程产出仓库，不是通用软件项目。课程文件本身就是产品，所有改动都要优先保证：

- 学习路径连续
- 课程结构稳定
- 量化语境明确
- 进度与规划一致

## 任务类型

先判断当前任务属于哪一类：

- 写课 / 继续今天的学习
- 写脉络 / 调整阶段规划
- Code Review / 批改练习
- 资源调研 / 资源库更新
- 知识库整理 / 会话交接

不同任务先读不同文件，不要直接动手。

## 写课前必读

1. `resources/个人信息.md`
2. `resources/主脉络.md`
3. 当前阶段对应的 `docs/plans/阶段X_分脉络大纲.md`
4. `docs/workflows/写课程流程.md`
5. `vault/会话交接.md`

如果细脉络不存在，或与主脉络不一致，先停下来走写脉络流程。

## 写脉络前必读

1. `resources/个人信息.md`
2. `resources/主脉络.md`
3. `resources/招聘市场调研报告.md`
4. `resources/lib/资源库.md`
5. `docs/workflows/写脉络流程.md`
6. `vault/会话交接.md`

## Code Review 前必读

1. 当前 day 的课程文件
2. 当前阶段细脉络
3. `vault/会话交接.md`

Review 目标是判断用户是否掌握了当前知识点，而不是顺手重写一份“更优代码”。

## 目录约定

- 课程文件：`projects/python/stage1_python基础/`、`projects/python/stage2_数据处理/`、`projects/python/stage3_项目实战/`
- 外部参考仓：`projects/ai-engineering/`（本地克隆的辅线资料，不当作当前课程源文件）
- 阶段规划：`docs/plans/`
- 工作流：`docs/workflows/`
- 参考资料：`docs/references/`
- 文档站镜像：`docs/resources/`、`docs/tutorials/`（由脚本同步生成，不手改）
- 核心规划资料：`resources/`
- 知识库与交接：`vault/`
- vault 系统说明：`vault/00_OS/VAULT_CLAUDE.md`
- 项目级 skills：`.agents/skills/`
- 项目级 Codex 配置：`.codex/config.toml`

## 项目主事实来源

以下文件是当前仓库的主事实来源：

- 根 `AGENTS.md`
- `resources/主脉络.md`
- `docs/plans/阶段X_分脉络大纲.md`
- `docs/workflows/写课程流程.md`
- `docs/workflows/写脉络流程.md`
- `vault/会话交接.md`

`.claude/CLAUDE.md` 和 `.claude/memory/` 是历史资产，可以参考，但不是唯一事实来源。

## 写课硬规则

### 学习量

- 每天课程量不能凭感觉安排,必须依据 `docs/plans/学习量校准规则.md`。
- 写 day 文件前,先确认当天对应的阶段目标、前置依赖、时间预算、练习数量和验收产出。
- 默认普通 day 控制在 2.5-3 小时; 项目/综合测试 day 可到 3-4 小时,但必须在阶段细脉络里写明原因。
- 如果当天出现新概念超过 3 个、练习超过 10 道且还有大综合、或同时引入新库+新数据源+项目结构,必须拆天或降为选做。
- 用户上一天练习未稳定完成时,优先减量、复习、补薄弱点,不能机械进入下一天。

### 结构

每节课保持这个骨架：

1. 复习环节
2. 知识块 1：知识点1.1 -> 练习1.1.x -> 知识点1.2 -> 练习1.2.x -> 总练习1.x
3. 知识块 2：知识点2.1 -> 练习2.1.x -> 知识点2.2 -> 练习2.2.x -> 总练习2.x
4. Day 综合练习

复习题数量按前一天知识块数量设置。知识点和练习必须紧挨，不能先教很多，再统一出题。练习数量按知识点难度、重要程度和用户薄弱程度动态调整。

### 练习

- 练习描述只说“做什么”，不说“怎么做”
- 默认不泄漏答案
- `# ↓ 你的代码 ↓` 下方默认留空
- 每道练习写出前必须做依赖校准,依据 `docs/plans/练习依赖校准规则.md`
- 必做练习只能依赖已教内容、当天前面已讲内容,或该练习正上方刚讲完的知识点
- 如果练习必须用到未教技术,只能前移教学、降级题目、改成选做或删除,不能硬塞成必做
- 复习题只用过去 day 已教内容; 知识块总练习只用本块已讲内容; Day 综合只用当天已讲内容 + 历史已学内容
- 简单知识点可 1 道题；核心或易错知识点可 2-3 道题；知识块总练习通常 1 道，复杂块可 2 道
- 超前内容只允许出现在“选做”题
- 如果课程文件已被练习答案污染，先运行 `python3 scripts/archive_and_clear_filled_exercises.py stage1|stage2` 归档后再清理

### 教学

- 代码注释用中文，变量名保持英文
- 每个知识点都说明量化场景用途
- 不超前使用当天未讲过的语法和库
- NumPy / Pandas / Matplotlib 阶段优先使用真实或合理的股票数据语境

### 来源

- 写课前至少参考 2 个来源
- 优先顺序：官方文档 / 原始教程 > 资源库已有高质量资料 > 社区文章或视频
- 在课程文件顶部标注参考源

## 写脉络硬规则

- `resources/主脉络.md` 是长期总规划
- `docs/plans/阶段X_分脉络大纲.md` 是阶段内 day-by-day 安排
- 两者不一致时，先修规划，再写课
- 做阶段规划时,必须先做学习量/容量预算: 阶段终点、总可用时间、主线比例、缓冲比例、每日上限、验收方式
- 阶段2以后即使先按 week 写,进入每个 week 前也必须拆成 day-by-day 微计划
- 做阶段规划时，必须显式检查：
  - 是否符合量化开发主线
  - 是否对应岗位需求
  - 是否存在前置依赖断裂
  - 是否设置复习日和综合练习
  - 是否符合学习量校准规则

## 学习流程路由

- 用户说“开始今天的学习”“继续”“开始写课”：
  走 `course-writing`
- 用户说“新阶段开始”“细脉络没了”“脉络对不上”：
  走 `roadmap-writing`
- 用户发练习代码：
  先 review，再决定是否进入下一天
- 用户说“练 XX”“解释 XX”“对比 XX”：
  优先复用 `learning-*` skills

## 搜索与资源更新

- 所有搜索/调研任务先读本地 `search-mastery`
- 每轮调研结束列出“还有哪些方向没考虑到”
- 搜索范围优先收敛到当前 day / 当前阶段，不做无边界泛搜

如果发现高价值资源：

1. 判断是否与当前学习计划相关
2. 相关则更新 `resources/lib/资源库.md`
3. 如果能立刻影响写课或规划，再同步更新 workflow 或阶段计划

## 记忆与交接

- `vault/会话交接.md` 是新会话第一入口，也是结束时必须更新的文件
- `vault/00_OS/VAULT_CLAUDE.md` 只负责说明 vault 用法，不承载课程进度真相
- 长期保留的知识点、薄弱环节、坑，写入 `vault/20_WIKI/`
- 历史项目记忆在 `.claude/memory/`，可作为补充约束使用
- 如果形成稳定新规则，优先写回 `AGENTS.md` 或 workflow 文档，不要只留在临时对话里

## 常见更新面

### 写完一节课后，通常同步这些文件

- 当天课程文件
- `resources/主脉络.md`
- 对应 `docs/plans/阶段X_分脉络大纲.md`
- `vault/会话交接.md`
- 优先运行 `python3 scripts/checks.py docs`
- 再运行 `python3 scripts/checks.py course`
- 新环境初始化优先用 `python3 scripts/checks.py bootstrap`
- 开工前想快速看仓库状态时，先跑 `python3 scripts/checks.py status`
- 需要快速回归时，优先用 `python3 scripts/checks.py tests`
- 推荐最终跑一次 `python3 scripts/checks.py health`
- 如果希望把最小检查接入 git 流程，用 `python3 scripts/checks.py install-hooks`

### 写完脉络后，通常同步这些文件

- `resources/主脉络.md`
- 对应 `docs/plans/阶段X_分脉络大纲.md`
- 必要时更新 `resources/lib/资源库.md`
- `vault/会话交接.md`

## Git 规则

- 完整完成一节课或一次完整规划调整后再提交
- 不为了 checkpoint 制造无意义 commit
- 只提交本次任务相关文件
- 如果工作树里有无关改动，缩小提交范围

## 项目目标提醒

- 主目标：量化开发学习路线
- AI 是辅线，不压过量化主线
- 考研内容与技能学习尽量重叠设计
- 课程不是面向大众，而是面向当前这位学习者
