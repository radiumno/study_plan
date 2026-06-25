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
- `resources/lib/资源库.md`
- 根 `AGENTS.md`
- `docs/workflows/写脉络流程.md`
- `vault/会话交接.md`

### Step 2: 做有边界的调研

只研究和当前阶段直接相关的资料，重点回答：

- 主流课程如何组织这个阶段
- 这个阶段对应哪些岗位要求
- 练习和项目应该如何递进

优先级：官方文档 / 原始教程 > 高质量课程 > 社区实践。

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

更新或创建 `docs/plans/阶段X_分脉络大纲.md`，按 day 给出：

- 教学内容
- 练习安排
- 前置依赖
- 复习日 / 综合课安排
- 与量化主线的连接

### Step 6: 对齐检查

至少检查这 5 项：

| 检查项 | 标准 | 失败时怎么做 |
|--------|------|-------------|
| 主脉络 vs 岗位需求 | 知识点能映射到真实需求 | 增删内容 |
| 细脉络 vs 主脉络 | 阶段内容覆盖完整 | 调整 day 结构 |
| 前置依赖 | Day N 依赖已在更早阶段出现 | 重排顺序 |
| 练习覆盖 | 每个主题有对应练习 | 补练习 |
| 用户适配 | 节奏、目标、量化主线合理 | 收缩或重定范围 |

### Step 7: 定稿与交接

通常同步：

- `resources/主脉络.md`
- 对应 `docs/plans/阶段X_分脉络大纲.md`
- 必要时 `resources/lib/资源库.md`
- `vault/会话交接.md`

如果这次规划暴露出稳定规则缺口，再更新根 `AGENTS.md` 或 workflow 文档。

## Full Workflow File

完整细节见 `docs/workflows/写脉络流程.md`
