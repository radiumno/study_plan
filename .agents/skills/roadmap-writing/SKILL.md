---
name: roadmap-writing
description: Create or update a stage roadmap with 细脉络 for this study-plan repo — research relevant curricula and job signals, read the resource library, update 主脉络, break the stage into daily plans, run alignment checks, and finalize the planning docs. Use when a new stage begins, 细脉络 is missing, or 细脉络 doesn't match 主脉络.
license: MIT
---

# Roadmap / 脉络 Writing Workflow

当需要创建新阶段大纲或更新现有大纲时，按此流程执行。
触发条件：新阶段开始 | 细脉络不存在 | 细脉络与主脉络不匹配

## Workflow

### Step 1: 读取当前规划上下文

先读：

- `resources/个人信息.md`
- `resources/主脉络.md`
- `resources/招聘市场调研报告.md`
- `docs/plans/技能需求-权重矩阵.md`
- `resources/核心学习资源清单.md`
- `resources/lib/资源库.md`
- 根 `AGENTS.md`
- `docs/plans/规划层级与滚动执行规则.md`
- `docs/workflows/写脉络流程.md`
- `vault/会话交接.md`

### Step 2: 做有边界的调研

只研究和当前阶段直接相关的资料，重点回答：

- 主流课程如何组织这个阶段
- 这个阶段对应哪个岗位族、哪些核心要求
- 练习和项目应该如何递进

优先级：官方文档 / 原始教程 > 高质量课程 > 社区实践。
没有逐条样本表时，不生成岗位出现率或典型薪资。

### Step 3: 产出前先回答四个问题

1. 为什么这个阶段要这样排序？
2. 每个 day 对应什么岗位需求？
3. 学完这个阶段，用户会新增什么能力？
4. 节奏是否适合用户背景和时间预算？

答不上来，就不要动笔。

### Step 4: 更新主脉络

必要时更新 `resources/主脉络.md`：

- 阶段定位
- 能力目标
- 与岗位需求的映射
- 当前状态和里程碑

### Step 5: 拆细脉络

更新或创建 `docs/plans/阶段X_分脉络大纲.md`：

- 当前阶段：所有剩余 day 给出教学、练习、依赖、时间和验收
- 下一阶段：周级完整，只细化未来 1-2 周
- 更远阶段：保留能力块、项目和闸门，不制造伪精确

### Step 6: 对齐检查

至少检查这 5 项：

| 检查项 | 标准 | 失败时怎么做 |
|--------|------|-------------|
| 主脉络 vs 岗位需求 | 知识点能映射到真实需求 | 增删内容 |
| 细脉络 vs 主脉络 | 阶段内容覆盖完整 | 调整 day 结构 |
| 前置依赖 | Day N 依赖已在更早阶段出现 | 重排顺序 |
| 练习覆盖 | 每个主题有对应练习 | 补练习 |
| 用户适配 | 节奏、目标、量化主线合理 | 收缩或重定范围 |
| 状态语义 | 课程已写不等于 Review 通过 | 修正状态 |
| AI边界 | 主线未过闸时不占固定比例 | 暂停辅线 |

### Step 7: 定稿与交接

通常同步：

- `resources/主脉络.md`
- 对应 `docs/plans/阶段X_分脉络大纲.md`
- 必要时招聘报告、技能矩阵、核心资源清单或候选资源库
- `vault/会话交接.md`

如果这次规划暴露出稳定规则缺口，再更新根 `AGENTS.md` 或 workflow 文档。

## Full Workflow File

完整细节见 `docs/workflows/写脉络流程.md`
