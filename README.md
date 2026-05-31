<div align="center">
  <h1>Quant Developer Roadmap</h1>
  <p><strong>量化开发学习与就业规划</strong></p>
  <p>从零到量化开发工程师 · 完整6阶段路线图</p>

  <p>
    <img src="https://img.shields.io/badge/阶段-1%20of%206-blue?style=flat-square" alt="阶段">
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python" alt="Python">
    <img src="https://img.shields.io/badge/C%2B%2B-20-00599C?style=flat-square&logo=c%2B%2B" alt="C++">
    <img src="https://img.shields.io/badge/进度-5%20/%2017%20天-green?style=flat-square" alt="进度">
    <img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square" alt="MIT">
  </p>
</div>

---

## 这是什么

一份**岗位需求驱动**的量化开发学习路线图。

从 BOSS直聘 / 猎聘真实招聘数据出发，倒推出6阶段学习计划，逐日推进。适合**数据科学专业本科生**以量化开发为职业目标的学习路径。

### 学习者档案

- **学校：** 中国地质大学（武汉）· 数据科学与大数据技术 · 2025级
- **目标：** 量化开发工程师（C++/Python）
- **保底：** 互联网后端开发

---

## 项目结构

```
study_plan/
├── .claude/
│   ├── CLAUDE.md               # 项目指令
│   ├── settings.json           # Claude 配置
│   └── skills/                 # 自定义技能
├── .vscode/                    # VS Code 工作区配置
├── docs/
│   ├── plans/                  # 阶段详细计划
│   ├── workflows/              # 写课/写脉络工作流
│   ├── archive/                # 历史存档
│   └── ai-side/                # AI 侧线学习大纲
├── data/                       # 练习用数据文件
├── projects/
│   ├── python/
│   │   ├── tutorials/          # 每日Python教程
│   │   ├── projects/           # 项目实战
│   │   └── setup_day04_data.py # 数据生成脚本
│   └── cpp/                    # C++摸底+练习
├── resources/
│   ├── 个人信息.md
│   ├── 主脉络.md               # 全6阶段路线图
│   ├── 教学资源参考.md
│   ├── 招聘市场调研报告.md
│   ├── 课程匹配度与AI量化分析.md
│   └── lib/资源库.md           # 完整资源索引
├── scripts/                    # 工具脚本
├── COLLEAGUES.md               # 教学契约（Hermes 交换信息）
└── README.md
```

---

## 路线图

| 阶段 | 时间 | 内容 | 状态 |
|------|------|------|------|
| **阶段1** Python基础 | 2026.5 - 7月 | 语法 → NumPy/Pandas → 项目 | 🏃 进行中 |
| **阶段2** 算法+C++ | 大二上 | 数据结构 + 算法刷题 + C++入门 | ⏳ |
| **阶段3** C++深入 | 寒假 | 现代C++、内存管理、STL | ⏳ |
| 阶段4 | 量化核心 | 大二下 | 回测系统、Linux、多线程、ML入门 | ⏳ |
| 阶段5 | 实习 | 大二暑假 | 第一份量化实习 | ⏳ |
| 阶段6 | 冲刺 | 大三 | 交易系统、面试准备、秋招 | ⏳ |

---

## AI 工程整合

study_plan 引入了 [ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (23.7k ⭐) 作为补充资源。

| 资源 | 路径 | 说明 |
|------|------|------|
| **AI 工程整合索引** | [`resources/ai-engineering.md`](resources/ai-engineering.md) | 所有 20 Phase 的映射: 🟢融入主线 / 🟡AI侧线 / ⬜跳过 |
| **AI 侧线学习大纲** | [`docs/ai-side/README.md`](docs/ai-side/README.md) | 跟量化主线不重叠的 AI 内容, 有空再学 |
| **本地代码仓库** | `D:\Dev\AiProject\_ai_ref\` | 完整克隆, 473 节课的 code/ + docs/ |

### 怎么用

- 🟢 **融入主线** — 学习对应 Day/Phase 时, 翻 `_ai_ref` 的 code/ 跑一遍, 配合理解
- 🟡 **AI 侧线** — 想换脑子时打开 `docs/ai-side/` 选一个 Phase, 跟我说"学一下 Phase 14"就行

---

## 当前进度

### 阶段1 — Python基础（17天 / 7周）

| Day | 内容 | 状态 |
|-----|------|------|
| 01 | 变量、类型、字符串、输入输出 | ✅ |
| 02 | 列表、字典、元组、内置函数 | ✅ |
| 03 | 函数、作用域、lambda | ✅ |
| 04 | set + 文件I/O + 异常处理 | ✅ |
| 05-17 | 模块与包 → 综合项目 | ⏳ |

### 学习管理

```
Claude Code（备课 → 讲解 → 出练习 → Code Review）
     │
     └── 依赖清单检查 → 发现缺项立即喊停
```

---

## 核心原则

- **岗位驱动** — 所有内容从招聘JD倒推，不学用不上的
- **量化场景** — 练习全部围绕股票数据、交易逻辑
- **依赖严谨** — 每个Day的依赖项必须在之前教过
- **先调研再动** — 不做拍脑门的决定

---

## 资源索引

| 类别 | 位置 |
|------|------|
| B站视频 / GitHub项目 / 书籍 | [`resources/lib/资源库.md`](resources/lib/资源库.md) |
| 完整路线图 | [`resources/主脉络.md`](resources/主脉络.md) |
| AI+量化分析 | [`resources/课程匹配度与AI量化分析.md`](resources/课程匹配度与AI量化分析.md) |
| 招聘数据 | [`resources/招聘市场调研报告.md`](resources/招聘市场调研报告.md) |

---

<div align="center">
  <sub>从运城到武汉 · 从零到量化开发</sub>
</div>
