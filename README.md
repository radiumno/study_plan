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

```
study_plan/
├── projects/python/           ← 教程文件
│   ├── stage1_python基础/     Day 01-07: Python 核心语法
│   ├── stage2_数据处理/        Day 08-14: NumPy/Pandas/Matplotlib
│   └── stage3_项目实战/        Day 15-16: 综合项目
├── docs/                      文档站 (mkdocs)
│   ├── plans/                 各阶段分脉络大纲
│   ├── lib/                   教学资源库
│   └── workflows/             写课/周审/写脉络流程
├── resources/                 主脉络、个人信息、教学参考
├── vault/                     AI 知识库 (跨会话记忆系统)
└── .claude/
    ├── skills/                自动化工作流 (写课/周审/搜索)
    └── memory/                项目记忆规则
```

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

# 2. 安装 Python 依赖
pip install numpy pandas matplotlib baostock

# 3. 运行 Day 09 示例
python3 projects/python/stage2_数据处理/day09_Pandas入门.py
```

### 查看文档站

```bash
pip install mkdocs mkdocs-material
mkdocs serve
# 浏览器打开 http://localhost:8000
```

---

## 技术设计

### 写课自动化

每次 "开始写课" 触发完整工作流：
1. 自动重建周审 cron
2. 搜索当日知识点最新资源（5 分钟快速扫描）
3. 按标准结构写课（复习 → 知识块 → 练习紧挨 → 块练习 → Day 综合）
4. 反向检查 + 结构复查
5. 自动 commit + push

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
