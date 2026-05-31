# 阶段1: Python 基础 — 分脉络大纲

> 编写依据：调研 CS50P、Python 官方教程、Real Python、Exercism、QuantInsti 等课程后综合裁剪
> 调研日期：2026-05-27（资源库更新：2026-05-28）
> 学习者：孙溢镭，地大（武汉）数据科学，大一升大二，目标量化开发

---

## 1. 定位与目标

**在主脉络中的位置：** 阶段1（共6阶段），预计 7 周，对应岗位要求中 **Python 数据处理能力（出现频率 90%+）**

**目标：**
- 能独立写 Python 脚本处理数据
- 掌握 NumPy/Pandas，能处理股票行情数据
- GitHub 上有 3+ 项目
- 为阶段2（C++/数据结构）打好编程基础

**教学模式：** Claude Code（我）备课 → 讲解 → 出练习 → Code Review。依赖清单见 `COLLEAGUES.md`

**与其他课程对比：**

| 维度 | CS50P | Real Python | 本计划 |
|------|-------|-------------|--------|
| 异常处理 | Week 4（较早） | 模块化 | Day 04（适中） |
| 测试 | Week 6 单独讲 | 无 | 综合练习体现 |
| Lambda | Week 10 收尾 | 模块化 | Day 03 随函数教 |
| NumPy/Pandas | 无 | 无 | **Day 08-10 重点** |
| 量化场景 | 无 | 无 | **贯穿全部练习** |

> 本计划与其他课程最大的不同：练习全部围绕**量化场景**（股票、持仓、行情、回测），而非通用练习题。

---

## 2. 总体结构

```
阶段1 Python基础（7周）
├── Part 1: Python 核心（Days 01-07，2周）
│   ├── Day 01: 变量、类型、字符串、输入输出  ✅
│   ├── Day 02: 列表、字典、元组、set、遍历  ✅（set 移到 Day 04）
│   ├── Day 03: 函数、作用域、lambda  ✅
│   ├── Day 04: set + 文件I/O + 异常处理
│   ├── Day 05: 模块与包、pip、datetime
│   ├── Day 06: 综合项目（股票数据管理器）
│   └── Day 07: 复习 + 查漏补缺
│
├── Part 2: 数据处理（Days 08-14，2周）
│   ├── Day 08: NumPy 数组运算
│   ├── Day 09: Pandas 入门
│   ├── Day 10: Pandas 进阶
│   ├── Day 11: Matplotlib 可视化
│   ├── Day 12: 数据采集（API/yfinance）
│   ├── Day 13: 数据清洗实战
│   └── Day 14: 综合练习
│
├── Part 3: 项目实战（Days 15-17，1周）
│   ├── Day 15: 股票分析工具 v1（纯Python）
│   ├── Day 16: 股票分析工具 v2（Pandas版）
│   └── Day 17: 复习 + 阶段总结
│
└── 弹性周（1周）
    └── 补进度 / 刷题 / 深入薄弱环节
```

---

## 3. Part 1: Python 核心（Days 01-07）

### 设计思路

参考 **CS50P** 的"先函数后数据结构"和 **Real Python** 的"函数+循环紧密绑定"模式，但做了调整：

- 把 **列表/字典提前到 Day 02**，因为量化场景第一天就需要处理数据容器
- 把 **lambda 随函数教**（Day 03），而不是像 CS50P 拖到最后
- **set 和异常处理放在 Day 04**，因为 set 是四大基础类型的最后一块拼图
- 每一节末尾的综合练习都模拟**真实量化场景**

### 四大基础类型覆盖进度

| 类型 | Day | 状态 |
|------|-----|------|
| list | Day 02 | ✅ |
| dict | Day 02 | ✅ |
| tuple | Day 02 | ✅（随 zip/unpacking 一起教） |
| set  | Day 04 | ✅（已加入，和异常+文件结合） |

### 依赖检查机制

每次 Claude Code 接到新 day 的任务时，会拉依赖清单确认：
- 本 day 用到的所有类型/语法，是否在之前的 day 教过
- 四大基础类型是否有遗漏
- 发现缺失 → 暂停 → 补充前置教学 → 重新检查

详见 `COLLEAGUES.md`

### Day 01 ✅ 已完成

| 知识点 | 来源参考 |
|--------|---------|
| 变量与赋值 | CS50P Week 1, Python Tutorial Ch 3 |
| 基本类型（int/float/str/bool） | CS50P Week 1, Real Python |
| 字符串操作（拼接、切片、格式化） | Python Tutorial Ch 3, Real Python |
| f-string 格式化 | Python 3.6+ 特性 |
| input() 输入 | CS50P Week 1 |
| 注释与编码风格（PEP 8） | Python Tutorial Ch 2, PEP 8 |

**练习内容：** 类型转换、字符串操作、计算器
**综合项目：** 股票信息卡片

### Day 02 ✅ 已完成

| 知识点 | 来源参考 |
|--------|---------|
| list 创建、索引、切片 | Python Tutorial Ch 5, Real Python |
| list 方法（append/pop/remove/sort） | Python Tutorial Ch 5 |
| dict 创建、访问（get/[]）、遍历 | Python Tutorial Ch 5, Exercises |
| tuple 与 unpacking | Python Tutorial Ch 5, Exercism |
| range / enumerate / zip | CS50P Week 3, Python Tutorial Ch 4 |
| 推导式（list/dict comprehension） | CS50P Week 10, Python Tutorial Ch 5 |

**练习内容：** 列表操作、字典映射、遍历技巧、推导式实战
**综合项目：** 股票持仓市值管理系统（含用户练习代码）

### Day 03 ✅ 已完成

| 知识点 | 来源参考 |
|--------|---------|
| 函数定义（def/return） | CS50P Week 1, Python Tutorial Ch 4 |
| 参数（默认值/关键字/*args/**kwargs） | Python Tutorial Ch 4, Real Python |
| 返回值与多个返回值 | Python Tutorial Ch 4 |
| 作用域（global/nonlocal） | Real Python 单独一章 |
| lambda 匿名函数 | CS50P Week 10, Python Tutorial Ch 4 |
| 函数式编程初步（map/filter） | Python Tutorial Ch 5, Exercism |

**练习方向：** 封装重复逻辑、计算指标函数、lambda 排序
**当前状态：** ✅ 已完成（用户已填充全部练习）

### Day 04 ⚠️ 教学已完成，练习待续

| 知识点 | 来源参考 |
|--------|---------|
| **set 集合**（创建、增删、交并差运算）⭐新增 | Python Tutorial Ch 5, Real Python |
| 异常处理（try/except/finally） | CS50P Week 4, Python Tutorial Ch 8 |
| 文件读写（open/with/close） | Python Tutorial Ch 7 |
| CSV 文件处理 | Python Tutorial Ch 7, 量化场景 |
| with 上下文管理器 | Python Tutorial Ch 7 |

**四大基础类型最后一块拼图：** Day 04 完成了 list/dict/tuple/set 的全部覆盖。

**练习方向：**
- set：数据去重、集合运算找出交集/差集（多个板块股票池的交集）
- 异常：处理文件不存在、格式错误、除零
- 文件：读取股票CSV、写入整理后的数据
- 结合练习：从 CSV 读入股票代码到 set，做集合运算，异常保护

### Day 05 ⏳ 未开始

| 知识点 | 来源参考 |
|--------|---------|
| import 机制 | CS50P Week 5, Python Tutorial Ch 6 |
| 自定义模块 | Python Tutorial Ch 6 |
| pip 与第三方库 | Python Tutorial Ch 12, CS50P Week 5 |
| datetime 模块 | Python Tutorial Ch 10 |
| os/pathlib 路径操作 | Python Tutorial Ch 10 |

**练习方向：** 组织多文件项目、时间处理、文件路径操作

### Day 06 ⏳ 未开始

综合项目：**股票数据管理器**
- 结合 Days 01-05 所有知识点
- 读写 CSV 文件
- 数据计算与筛选
- 函数封装

### Day 07 ⏳ 未开始

复习 + 查漏补缺

---

## 4. Part 2: 数据处理（Days 08-14）

参考 **QuantInsti** 和 **Coursera Python for Finance** 的组织方式，加入数据采集环节以保证技能完整性。

| Day | 内容 | 参考来源 |
|-----|------|---------|
| 08 | NumPy 数组运算、广播、线性代数 | QuantInsti, NumPy 官方文档 |
| 09 | Pandas 入门（Series/DataFrame） | Pandas 官方教程, QuantInsti |
| 10 | Pandas 进阶（时间序列/groupby/merge） | Coursera Python for Finance |
| 11 | Matplotlib 可视化（K线/折线/柱状） | Matplotlib 官方教程 |
| 12 | 数据采集（yfinance API/requests） | 招聘需求:数据采集60%+ |
| 13 | 数据清洗实战 | 招聘需求:ETL 60%+ |
| 14 | 综合练习 | — |

---

## 5. Part 3: 项目实战（Days 15-17）

| Day | 内容 | 对应岗位能力 |
|-----|------|-------------|
| 15 | 股票分析工具 v1（纯Python） | 数据处理、文件I/O |
| 16 | 股票分析工具 v2（Pandas版） | 数据分析、时间序列 |
| 17 | 复习 + 阶段总结 | — |

---

## 6. 知识点覆盖检查

### 6.1 岗位要求覆盖

对照招聘数据中的技能要求（来自 `招聘市场调研报告.md`）：

| 岗位要求 | 覆盖情况 | 所在位置 |
|----------|---------|---------|
| Python 数据处理 | ✅ 核心 | Part 1-2 |
| Git 版本控制 | ✅ 初期 | 日常使用 |
| 数据采集/API | ✅ | Day 12 |
| 文件 I/O | ✅ | Day 04 |
| 数据分析能力 | ✅ | Part 2 |
| 可视化能力 | ✅ | Day 11 |
| SQL（阶段1外） | ⬜ 阶段4 | — |
| Linux（阶段1外） | ⬜ 阶段3 | — |

### 6.2 四大基础类型覆盖

| 类型 | 状态 | Day |
|------|------|-----|
| list | ✅ | Day 02 |
| dict | ✅ | Day 02 |
| tuple | ✅ | Day 02 |
| set  | ✅ | Day 04 |

### 6.3 依赖链完整性

每次新 day 交付 Claude Code 前，自动检查该 day 的所有依赖项在之前 days 的教学覆盖率。见 `COLLEAGUES.md`。

---

## 7. 推荐资源映射

| 资源 | 用途 | 对应阶段 |
|------|------|---------|
| ⭐ **资源库（完整版）** `resources/lib/资源库.md` | **各阶段资源总索引** | **全阶段** |
| [廖雪峰Python教程](https://www.liaoxuefeng.com/wiki/1016959663602400) | 主线教材，25章免费中文 | Part 1-2 |
| [Python-100-Days](https://github.com/jackfrued/Python-100-Days) (182k⭐) | 课后练手，Day01-20对应Part1 | Part 1-3 |
| [林粒粒呀3h入门](https://b23.tv/BV1Jgf6YvE8e) (613万播放) | 预热，快速建立认知 | Day 01-02前 |
| [CS50P](https://cs50.harvard.edu/python/) | 课后扩展，查漏补缺 | Part 1 |
| [Python 官方教程](https://docs.python.org/3/tutorial/) | 权威参考，语法查证 | Part 1 |
| [Real Python](https://realpython.com/) | 深入理解概念 | Part 1 |
| [Exercism Python Track](https://exercism.org/tracks/python) | 课后刷题，巩固语法 | Part 1 |
| [菜鸟教程Python](https://www.runoob.com/python3/python3-tutorial.html) | 快速查阅，带在线运行 | Part 1 |
| [NumPy 官方教程](https://numpy.org/doc/stable/user/quickstart.html) | 入门到实践 | Part 2 |
| [Pandas 官方教程](https://pandas.pydata.org/docs/getting_started/) | 入门到实践 | Part 2 |
| [QuantInsti](https://www.quantinsti.com/) | 量化方向参考 | Part 2-3 |
| [尚硅谷Python数据分析](https://b23.tv/BV1D9GLzyEL6) (168万播放) | NumPy/Pandas/Matplotlib视频 | Part 2 |
| [鱼皮AI Guide](https://github.com/liyupi/ai-guide) (14.7k⭐) | AI工具链参考（Claude Code/Cursor等） | 全阶段备查 |

---

## 8. 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-05-27 | 初始创建 |
| 2026-05-28 | Day 03 状态改为⚠️部分完成 |
| 2026-05-28 | Day 04 新增 set 集合（完成四大类型覆盖） |
| 2026-05-28 | 新增依赖检查机制说明（关联 COLLEAGUES.md） |
| 2026-05-28 | 推荐资源映射更新：加入廖雪峰/Python-100-Days/资源库/菜鸟/鱼皮AI Guide |
| 2026-05-28 | 新增四大基础类型覆盖进度表 |
