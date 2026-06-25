# Quant Developer Study Plan

> **从零到量化开发工程师 —— Python 数据处理 → C++ 系统开发 → AI 量化策略**
>
> 以量化开发为主线，AI 应用开发为保底，考研 408/数一贯穿全程的体系化学习路线。

---

## 概览

本项目是一份完整的量化开发自学路线图，面向数据科学专业本科生，目标是**量化私募 C++/Python 开发实习生**。

### 学习路线（6 阶段）

| 阶段 | 时间 | 核心内容 | 产出 |
|:----:|:----:|---------|:----:|
| 1 | 大一暑假 | Python 数据处理 (NumPy/Pandas/Matplotlib) | 数据分析能力 |
| 2 | 大二上 | C++ 入门 + 数据结构 + 算法刷题 100 题 | 编程基本功 |
| 3 | 寒假 | 现代 C++ (智能指针/移动语义/内存管理) | C++ 深度 |
| 4 | 大二下 | 量化系统 + AI 应用双线并行 (60%/40%) | 回测引擎 + AI 项目 |
| 5 | 暑假 | 第一份实习 (小私募 / FinTech) | 实习经历 |
| 6 | 大三 | 冲刺 (低延迟/系统设计/LeetCode 500 题) | Offer |

### 当前进度

**阶段 1: Python 基础 — 进行中 (Day 10/16)**

| Part | Days | 内容 | 状态 |
|:----|:----:|------|:----:|
| 1 | 01-07 | Python 核心 (变量/控制流/函数/文件/异常) | ✅ 完成 |
| 2 | 08-14 | 数据处理 (NumPy → Pandas → Matplotlib → 数据采集) | ⏳ Day 10 |
| 3 | 15-16 | 综合项目: 股票分析工具 | ⏳ 待开始 |

---

## 项目结构

| 路径 | 角色 | 是否手改 |
|------|------|:--------:|
| `projects/python/` | 课程源码主产物 | ✅ |
| `resources/` | 主脉络、个人信息、资源库等主资料 | ✅ |
| `docs/plans/` | 阶段细脉络与规划文档 | ✅ |
| `docs/workflows/` | 写课、写脉络、周审流程 | ✅ |
| `docs/references/` | AI 辅线、速查表、补充参考 | ✅ |
| `docs/reviews/` / `docs/templates/` | 审计复盘 / 模板 | ✅ |
| `docs/resources/` | `resources/` 的文档站镜像（含 `index.md`） | ❌ |
| `docs/tutorials/` | `projects/python/` 的文档站镜像（含 `index.md`） | ❌ |
| `scripts/` | 同步、校验、健康检查脚本 | ✅ |
| `vault/会话交接.md` | 当前会话状态与下次待办 | ✅ |
| `vault/00_OS/` | vault 说明、模板、系统文件 | ✅ |
| `vault/10_RAW/` | 原始记录与课程快照归档 | 只追加 |
| `vault/20_WIKI/` | 长期知识点 / 薄弱项 / 教训 | ✅ |
| `projects/ai-engineering/` | 本地外部参考仓，供 AI 辅线查阅 | 谨慎 |
| `.claude/` | 历史配置和记忆资产，仅补充参考 | 谨慎 |

### 结构原则

1. 课程真源只放在 `projects/python/`。
2. 规划与教学主资料只放在 `resources/` 和 `docs/plans/`。
3. `docs/resources/`、`docs/tutorials/` 是同步产物，不手工编辑，入口页分别是 `docs/resources/index.md`、`docs/tutorials/index.md`。
4. 用户填写过答案的课程文件，先归档到 `vault/10_RAW/代码片段/filled_course_snapshots/`，再清空源码练习区。
5. 外部克隆仓和历史资产可以参考，但不作为当前课程产出的事实来源。

### 技术栈

| 工具 | 用途 |
|------|------|
| Python 3.13 | 教程语言、数据处理 |
| NumPy / Pandas / Matplotlib | 数据分析核心栈 |
| Baostock | A 股数据源 (国内直连) |
| mkdocs-material | 文档站 |
| Obsidian | AI 知识库 (可选) |

---

## 特色

### 1. 体系化而非碎片化

每节课按固定结构编排：
```
复习 → 知识块(知识点→练习紧挨→块练习) → Day 综合练习
```

每 3-5 天一次综合测试日（闭卷风格，跨知识点），每阶段末一次期末大综合。

### 2. 全部练习量化场景

- 不是"算 1+1"，而是"计算股票日收益率矩阵"
- 不是"排序字符串"，而是"按市值对股票池排序"
- 数据源用 Baostock（国内直连，无需 VPN）

### 3. 数据驱动的内容编排

- 教学内容直接对应 BOSS 直聘/猎聘量化开发 JD 要求
- 每周自动扫描 GitHub/B 站/知乎新资源，动态调整资源库
- 招聘市场变化（如 2026 年头部私募要求 AI Agent 技能）实时反映到学习路线中

### 4. AI 辅助全流程

- Claude Code 自动化写课、审课、更新进度
- 跨会话 AI 知识库记录学习轨迹和薄弱环节
- 多路并行搜索最新教学资源

---

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/radiumno/study_plan.git
cd study_plan

# 2. 一次性初始化环境
python3 scripts/checks.py bootstrap

# 3. 运行 Day 09 示例
python3 projects/python/stage2_数据处理/day09_Pandas入门.py
```

### 查看文档站

```bash
pip install mkdocs mkdocs-material
python3 scripts/checks.py docs
mkdocs serve
# 浏览器打开 http://localhost:8000
```

### 文档站维护

文档站现在只依赖 `docs/` 目录。

- `resources/` 中的主资料通过 `scripts/sync_docs.py` 同步到 `docs/resources/`
- `projects/python/` 中的课程源码通过 `scripts/sync_docs.py` 生成镜像页到 `docs/tutorials/`
- 每次改动文档入口、课程源码、资源资料后，优先跑 `python3 scripts/checks.py docs`

不要手工改 `docs/resources/` 和 `docs/tutorials/` 里的同步产物，源文件分别是 `resources/` 和 `projects/python/`。

### 仓库健康检查

```bash
python3 scripts/checks.py health
```

当前会执行：
- 文档同步 `scripts/sync_docs.py`
- 文档结构校验 `scripts/check_docs_structure.py`
- 课程质量校验 `scripts/check_course_quality.py`

也可以按组运行：

```bash
python3 scripts/checks.py list
python3 scripts/checks.py docs
python3 scripts/checks.py course
python3 scripts/checks.py tests
```

- `list`：查看统一入口可用命令
- `docs`：只跑文档同步与文档结构校验
- `course`：只跑课程质量硬检查
- `tests`：只跑脚本级回归测试

### 统一维护入口

如果不想记多个脚本名，直接用统一入口：

```bash
python3 scripts/checks.py list
python3 scripts/checks.py bootstrap
python3 scripts/checks.py status
python3 scripts/checks.py sync
python3 scripts/checks.py docs
python3 scripts/checks.py course
python3 scripts/checks.py tests
python3 scripts/checks.py health
python3 scripts/checks.py install-hooks
python3 scripts/checks.py reset-stage1
python3 scripts/checks.py reset-stage2
```

### Git hooks

仓库内提供了可追踪的 git hooks：

```bash
python3 scripts/checks.py install-hooks
```

- `pre-commit`：提交前跑 `python3 scripts/checks.py tests`
- `pre-push`：推送前跑 `python3 scripts/checks.py health`

如果是新环境，`python3 scripts/checks.py bootstrap` 会一并创建 `.venv`、安装依赖、安装 hooks，并跑一次全量健康检查。

`python3 scripts/checks.py status` 会快速显示当前环境、hooks、docs 镜像和工作树状态，适合开工前先看一眼。

### 课程练习区重置

当课程文件里的 `# ↓ 你的代码 ↓` 已经被填满，需要恢复成可再次教学的版本时：

```bash
python3 scripts/archive_and_clear_filled_exercises.py stage1
python3 scripts/archive_and_clear_filled_exercises.py stage2
```

原始已填写版本会先归档到 `vault/10_RAW/代码片段/filled_course_snapshots/`，然后再清空课程源文件里的练习区。

---

## 技术设计

### 写课自动化

每次 "开始写课" 触发完整工作流：
1. 读取主脉络、细脉络、会话交接和项目规则
2. 搜索当日知识点最新资源（必要时，5 分钟快速扫描）
3. 按标准结构写课（复习 → 知识块 → 练习紧挨 → 块练习 → Day 综合）
4. 反向检查 + 结构复查
5. 更新进度与交接，完成后提交相关改动

### 知识点→练习紧挨

每个知识点教学后紧跟对应练习，编号对应：

```
知识点1.1 (teaching) → 练习1.1 (填空)
知识点1.2 (teaching) → 练习1.2.1, 练习1.2.2 (补全)
知识点1.3 (teaching) → 练习1.3 (实现)
▸ 知识块1总练习 (跨该块所有知识点)
```

练习描述只说"做什么"，不说"怎么做"。

---

## 参考资源

- [whale-quant](https://github.com/datawhalechina/whale-quant) — Datawhale 量化课程参考
- [QuantInsti](https://www.quantinsti.com/) — 量化金融培训
- [Baostock](http://baostock.com/) — 免费 A 股数据
- [资源库](resources/lib/资源库.md) — 完整教学资源索引

---

## 致谢

- 教学资源引用自 Datawhale、CS50P、Real Python、尚硅谷等开源教程
- 数据源由 Baostock 提供
- 文档站使用 mkdocs-material 构建

---

## 许可证

MIT
