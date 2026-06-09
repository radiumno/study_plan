---
name: conversation-history-guide
description: study_plan 项目对话历史索引，按时间线+学习进度组织
metadata: 
  node_type: memory
  type: reference
  date: 2026-06-03
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

# study_plan 对话历史索引

> 时间跨度: 2026-05-25 ~ 2026-06-03

---

## 阶段1 Python基础 进度

| Day | 内容 | 状态 | 关键会话日期 |
|-----|------|------|-------------|
| 01 | 变量、类型、字符串、输入输出 | ✅ | 5/25 |
| 02 | 列表、字典、元组、内置函数 | ✅ | 5/25 |
| 03 | 函数、作用域、lambda | ✅ | 5/26 |
| 04 | set + 文件I/O + 异常处理 | ✅ | 5/26-5/30 |
| 05 | 模块与包、pip、datetime | ✅ | 5/31 |
| 06 | 综合项目-股票数据管理器 | ✅ | 6/01 |
| 07-13 | NumPy/Pandas/可视化/数据采集 | ⏳ | — |

---

## 关键事件索引

### 项目启动与规划 (5/25)
- 职业规划讨论：量化开发 vs 量化研究 vs FinTech vs 数据分析
- 接手 study_plan 项目，分析 git 历史
- 构建学习规划目录结构

### 教学内容迭代 (5/26-5/31)
- Day 01-03: 初始教学，练习区正常
- Day 04-06: 暴露出多处教学问题，逐轮迭代修复
- 关键教训: 练习区预填答案、漏教元组/内置函数、参数讲解不够细 → 创建对应记忆规则

### 教学规则建立 (5/31)
核心规则全部来自用户反馈:
- 练习区留空，不预填答案
- 每个参数逐行拆解说明
- 绝对禁止编造内容
- 写课前先 commit，写完再 commit
- 每次出课前做依赖检查
- C++ 对比保留但降优先级

### 项目结构重组 (6/01)
- `projects/教程/` → `projects/python/tutorials/`
- `resources/job_data/` 清理冗余招聘数据
- `docs/workflows/` 新增
- `docs/ai-side/` 新增

### Whale-Quant 参考整合 (6/03)
- 评估 whale-quant (Datawhale 量化课程) → 保留做出课参考源
- QuantDigger → 跳过 (Python 2.x, 已停更)
- 整合入主脉络和细脉络大纲

---

## 历史错误摘要

| 错误 | 后果 | 修复措施 |
|------|------|---------|
| 练习区预填答案 | 用户靠抄不是自己写 | `exercises-must-be-empty.md` |
| 漏教元组/内置函数 | Day03 写不出来 | `curriculum-prerequisite-check.md` |
| 参数讲解太粗 | 看不懂代码 | `teaching-explain-every-step.md` |
| 编造信息 | 信任受损 | `never-fabricate.md` |
| 教学区写综合练习 | 练习区空了 | 代码移入 `utils.py` |
| 跳步: 教了没用过的语法直接出题 | 卡住 | 每课依赖清单检查 |
| 教程文件未保存就出题 | IndentationError | commit 规则间接解决 |

---

## 关键文件索引

| 文件 | 说明 |
|------|------|
| `projects/python/tutorials/day01_*.py` ~ `day06_*.py` | 6天教程文件 |
| `docs/plans/阶段1_Python_分脉络大纲.md` | 每日教学大纲 |
| `resources/主脉络.md` | 6阶段完整路线图 |
| `resources/lib/资源库.md` | 教学资源总索引 |
| `docs/workflows/写课程流程.md` | 出课标准流程 |
| `docs/workflows/写脉络流程.md` | 编写大纲标准流程 |
| `docs/workflows/周审流程.md` | 周日审查流程 |
| `resources/lib/whale-quant学习路线参考.md` | 出课参考源 |

---

## 更新日志

| 日期 | 内容 |
|------|------|
| 2026-06-03 | 初始创建，仅含 study_plan 相关内容 |
