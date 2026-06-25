# 阶段1: Python 基础 — 分脉络大纲

> 编写依据：调研 CS50P、Python 官方教程、Real Python、Exercism、QuantInsti 等课程后综合裁剪
> 调研日期：2026-05-27（最后更新：2026-06-26，根据多平台量化开发JD复核压实“够用即收”原则）
> 学习者：孙溢镭，地大（武汉）数据科学，大一升大二，目标量化开发

---

## 1. 定位与目标

**在主脉络中的位置：** 阶段1（共6阶段），预计 5 周（原7周，2026-05-31复核后压缩），对应岗位要求中 **Python 数据处理能力（出现频率 90%+）**

> 压缩原因: 2026年量化开发竞争环境下Python不再是差异化技能, 5周掌握数据处理能力即可进入C++阶段.
> AI编码工具(Claude Code/Cursor)从本阶段起作为日常工具使用.
> 2026-06-26复核: 阶段1不再追加大型AI/全栈内容, 只保留数据清洗、可视化、回测引子和GitHub展示。目标是尽快进入C++/算法主线。

**目标：**
- 能独立写 Python 脚本处理数据
- 掌握 NumPy/Pandas，能处理股票行情数据
- GitHub 上有 1-2 个质量过关的小项目, README清楚, 可复现
- 为阶段2（C++/数据结构）打好编程基础

**教学模式：** Codex / AI 助手备课 → 讲解 → 出练习 → Code Review。依赖与流程见根目录 `AGENTS.md`

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
阶段1 Python基础（5周，2026-05-31复核后压缩）
├── Part 1: Python 核心（Days 01-07，2周+）
│   ├── Day 01: 变量、类型、字符串、输入输出  ✅
│   ├── Day 02: 列表、字典、元组、遍历  ✅（set 移到 Day 04）
│   ├── Day 03: 函数、作用域、lambda  ✅
│   ├── Day 04: set + 文件I/O + 异常处理     ✅
│   ├── Day 05: 模块与包、pip、datetime       ✅
│   ├── Day 06: 综合项目（股票数据管理器）   ✅
│   ├── Day 07: 复习课（查漏补缺）          ✅ (2026-06-05新增)
│
├── Part 2: 数据处理（Days 08-14R，含2个综合测试日）
│   ├── Day 08: NumPy 数组运算 (+ 正则 re) ✅
│   ├── Day 09: Pandas 入门 (+ JSON 处理) ⚡模拟数据练手
│   ├── Day 10: Pandas 进阶 ⚡Baostock 实战：计算均线/波动率
│   ├── Day 11: Matplotlib 可视化
│   ├── Day 12: R2 复习日 (collections + itertools + generators + Git基础)
│   ├── Day 13: 数据采集与清洗 (+ pytest 验证)
│   ├── Day 14: 综合练习
│
├── Part 3: 项目实战（Days 15-16，2天）
│   ├── Day 15: 股票分析工具 v1
│   └── Day 16: 股票分析工具 v2
│
└── 弹性周（1周）
    └── 补进度 / 刷题 / 深入薄弱环节
```

### 学习量校准依据

阶段1不是按“每天想教什么”排,而是按终点倒推:

| 约束 | 阶段1取值 |
|------|-----------|
| 阶段终点 | 能处理行情数据,完成 `stock-analysis-tool`,README清楚,有最小测试 |
| 岗位权重 | Python数据处理/数据采集/API/Git 是阶段1核心; C++/系统/SQL 留到后续阶段 |
| 总容量 | 5周主线 + 1周弹性,普通 day 2.5-3h,项目/综合 day 3-4h |
| 缓冲 | Day 07, Day 11R, Day 14R 和弹性周用于复习/返工/薄弱点 |
| 禁止加量 | 不加 Web UI/数据库/完整AI系统/复杂交易系统 |

阶段1后半段按“回测项目闭环”倒推:

| Day | 类型 | 主目标 | 预估 | 验收产出 | 超量处理 |
|-----|------|--------|------|----------|----------|
| Day 11 | 常规技能课 | Matplotlib 可视化 | 2.5-3h | 一张价量+均线+买卖点图 | K线细节只做选修 |
| Day 11R | 复习综合课 | NumPy/Pandas/可视化串联 | 2-3h | 一道闭卷数据管道题 | 不加新库 |
| Day 12 | 工具补齐课 | collections/itertools/generator/Git | 3-4h | 交易频次统计、流式行情、Git提交 | Git进阶命令后移 |
| Day 13 | 常规技能课 | 数据采集与清洗 | 3h | 3只A股数据CSV + pytest检查 | requests只讲够用 |
| Day 14 | 综合应用课 | 本地回测管道 + 平台验证 | 3h | 平台截图 + 本地Pandas复现 | 聚宽/米筐不展开复杂API |
| Day 14R | 阶段测试 | 阶段1数据处理闭环验收 | 3-4h | 闭卷大题和薄弱点清单 | 失败则补课,不进项目 |
| Day 15 | 项目课 | 股票分析工具 v1 | 3-4h | 可运行CLI/脚本结构 | 不加Web/数据库 |
| Day 16 | 项目课 | 股票分析工具 v2 | 3-4h | Pandas版+可视化+README+最小测试 | 不加AI系统 |

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
- 每道练习的必用技术是否已经教过,或是否在练习正上方刚讲完
- 发现缺失 → 暂停 → 补充前置教学 → 重新检查

详见根目录 `AGENTS.md` 与 `docs/workflows/写课程流程.md`

### 练习依赖校准机制

阶段1写每道练习前必须做依赖矩阵,规则见 `docs/plans/练习依赖校准规则.md`:

| 题型 | 可用技术范围 |
|------|--------------|
| 复习题 | 只用过去 day 已教内容 |
| 知识点后练习 | 过去已学 + 刚讲完的知识点 |
| 知识块总练习 | 过去已学 + 本知识块已讲内容 |
| Day 综合 | 过去已学 + 当天已讲内容 |
| 选做题 | 可少量预告,不作为进度门槛 |

如果题目自然会诱导用户使用未教技术,要么先教,要么改题,不能靠提示临时补课。

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

### Day 04 ✅ 已完成

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

### Day 05 ✅ 已完成

| 知识点 | 来源参考 |
|--------|---------|
| import 机制 | CS50P Week 5, Python Tutorial Ch 6 |
| 自定义模块 | Python Tutorial Ch 6 |
| pip 与第三方库 | Python Tutorial Ch 12, CS50P Week 5 |
| datetime 模块 | Python Tutorial Ch 10 |
| os/pathlib 路径操作 | Python Tutorial Ch 10 |

**练习方向：** 组织多文件项目、时间处理、文件路径操作

### Day 06 ✅ 已完成

综合项目：**股票数据管理器**
- 结合 Days 01-05 所有知识点
- 读写 CSV 文件 (csv.DictReader/DictWriter)
- 数据计算与筛选 (set/推导式/lambda)
- 函数封装 (4个分步实现 + 综合练习)

### Day 07 ✅ 已完成

**复习课:** Python 核心查漏补缺 (2026-06-05 调整: 原Day 07 NumPy顺延至Day 08)
- 目的: 综合运用 Days 01-06 所有知识, 发现薄弱环节
- 练习1: 找 bug (常见错误: 索引/类型/可变性)
- 练习2: 函数 + 数据结构 (portfolio 分析)
- 练习3: set + 文件 + 异常 (板块交叉)
- 练习4: 综合管道 (交易日历生成, csv + datetime)
- 练习5(选做): 多股票区间筛选器 (csv 综合)

---

## 4. Part 2: 数据处理（Days 08-14）

参考 **QuantInsti** 和 **Coursera Python for Finance** 的组织方式，加入数据采集环节以保证技能完整性。依据 2026-06-05 优化调整，新增 R2 复习日补齐 collections / itertools / generators 缺口。

正则表达式（re）教学说明：`re` 模块基础语法在 Day 08 副线覆盖，Day 13 数据采集与清洗会深度复用。

### 数据源说明

国内直连可用方案：**Baostock**（`pip install baostock`，A股日线，国内直连最稳）+ **模拟数据**（NumPy cumprod，种子固定，练习可复现）

- Day 09-10: 模拟数据 (练习可复现) + 末尾附 Baostock 真实数据示例
- Day 11: Baostock / 模拟数据
- Day 13-14: Baostock 主线教学

---
### Day 08 — NumPy 数组运算 (已完成 ✅) [预估 2.5h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | ndarray 创建、形状/轴、广播机制、布尔索引、通用函数 | 50min |
| 练 | 5个子练习 (数组创建→广播→布尔索引→向量化) | 60min |
| 综合 | 用 NumPy 实现一个多股票日收益率矩阵运算 | 40min |

### Day 08R — NumPy 强化 (已完成 ✅) [预估 3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | axis 参数深入、广播 shape 匹配、布尔索引括号陷阱、向量化 vs for 循环 | 40min |
| 练 | 5个子练习 (axis选择→multi-stock归一化→信号生成→滑动窗口→综合) | 90min |
| 综合 | 分钟级多股票交易信号引擎 (向量化实现) | 50min |

### Day 09 — Pandas 入门 (已完成 ✅) [预估 2.5-3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | Series/DataFrame 创建、loc/iloc、shift、CSV/JSON 读写、模拟数据 | 50min |
| 练 | 5组练习 (Series创建→DataFrame查看→列行操作→CSV/JSON→股票分析) | 70min |
| 综合 | 多股票数据分析管道 (模拟数据 + Baostock 附) | 40min |

### Day 10 — Pandas 进阶 (已完成 ✅) [预估 3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 复习R | Series创建回练 + 布尔索引回练 | 15min |
| 块1 | 时间序列(to_datetime/date_range/切片): 练1.1-1.3 + 块练习 | 40min |
| 块2 | 滚动窗口(均线/波动率/金叉死叉): 练2.1-2.3 + 块练习 | 40min |
| 块3 | 重采样: 练3.1-3.2 | 20min |
| 块4 | GroupBy: 练4.1-4.2 + 块练习 | 20min |
| 块5 | 合并(concat/merge): 练5.1-5.2 + 块练习 | 25min |
| 综合 | Day综合: 均线金叉/死叉策略分析 | 50min |

---
### Day 11 — Matplotlib 可视化 [预估 2.5-3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | figure/axes、plot折线、bar柱状、hist分布、subplot多子图、K线自制方法 | 50min |
| 练 | 折线图(股价走势) → 柱状图(成交量) → subplot(价量双图) → 分布直方图 | 60min |
| 综合 | 净值曲线 + 均线叠加 + 买卖点标注 (完整交易可视化报表) | 50min |

练习数: 8~10个，数据用 Baostock/模拟

### Day 11R — 复习综合课 Day 08-11 [预估 2-3h] [资源扫描]

| 环节 | 内容 | 时间 |
|------|------|------|
| 回顾 | NumPy/Pandas/可视化核心速查表 | 20min |
| 测试 | 闭卷综合: 数组运算→DataFrame清洗→均线计算→净值曲线 全流程 | 100min |
| 自评 | 逐题对答案, 标记薄弱环节记入复习本 | 20min |

出题跨 4 天 (08→08R→09→10→11), 混合知识点。

### Day 12 — R2 复习日 [预估 3-4h]

**目的:** 集中补齐量化开发必备但Part 1没覆盖的工具类知识

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | collections(Counter/defaultdict/deque)、itertools(combinations/groupby/chain)、yield生成器、Git init-add-commit-push | 45min |
| 练 | Counter统计交易频次、deque模拟滑动窗口、itertools配对交易组合、生成器流式行情 | 60min |
| 综合1 | **Git实战**: 初始化本项目 → commit → push → README写作 | 40min |
| 综合2 | 找bug题(跨 Day 08-11) + 跨days综合管道题 | 60min |

**参考:** `docs/references/cheatsheets/git基础.md`

### Day 13 — 数据采集与清洗 [预估 3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | Baostock API 完整用法、requests GET请求、JSON解析、缺失值处理、pytest基本断言 | 50min |
| 练 | 拉单只A股 → 拉多只A股 → 日期范围遍历 → 数据清洗(去重/补空/类型修正) | 70min |
| 综合 | 采集3只A股2024全年数据 → 清洗 → 合并 → 保存CSV → pytest验证完整性 | 60min |

**项目参考:** `daily_stock_analysis` 只取多数据源/数据降级设计思路, 不引入 WebUI、Bot、Docker、LLM 配置。

### Day 14 — 数据采集+清洗综合+回测引子 [预估 3h]

| 环节 | 内容 | 时间 |
|------|------|------|
| 学 | 双均线策略回测全流程(数据→信号→持仓→绩效)、收益率曲线/最大回撤/夏普比 | 40min |
| 练 | 用 Day 09-13 知识完整实现: Baostock拉数据 → Pandas清洗 → 策略计算 → Matplotlib可视化 | 80min |
| 综合 | **完整回测管道**: 采集→清洗→策略→回测→绩效报告→可视化 一条龙 | 60min |

**平台触发:** Day 14后允许第一次上聚宽/米筐。
- 聚宽: 跑一个双均线或动量策略,记录回测参数、收益曲线、最大回撤。
- 米筐/RQAlpha: 看快速上手和回测文档,理解事件驱动回测入口。
- 必做对照: 用本地 Pandas 复现平台策略的核心信号和绩效指标。平台只当验证器,不能替代理解。

### Day 14R — 阶段1期末综合测试 [预估 3-4h] [资源扫描] [大审查]

| 环节 | 内容 | 时间 |
|------|------|------|
| 回顾 | Part 1+2 全部核心知识点速查 (Day 01-14) | 30min |
| 测试 | 闭卷大题3~4道, 覆盖: 数据采集/清洗/分析/可视化/策略回测 全链路 | 120min |
| 自评 | 逐题对答案, 薄弱环节记入"阶段2前需补"列表 | 30min |

执行大审查: 全量检查课程质量/结构合规/脉络对齐/岗位要求匹配, 更新资源库。

做完这个再进 Part 3 项目实战。

---

## 5. Part 3: 项目实战（Days 15-16）

| Day | 内容 | 对应岗位能力 | 预估时间 |
|-----|------|-------------|---------|
| 15 | **股票分析工具 v1**（纯Python, csv/txt/模块组织；参考 daily_stock_analysis 的任务入口/报告结构） | 数据处理、文件I/O、模块化 | 3-4h |
| 16 | **股票分析工具 v2**（Pandas版 + 简单可视化 + README + 最小测试；不做完整AI系统） | 数据分析、时间序列、可视化、工程展示 | 3-4h |

> 阶段1项目验收线: 能从原始CSV/接口数据得到清洗后的行情表、指标表和可视化报告; README写明安装、运行、输入输出。不要追加Web UI、数据库、LLM或复杂交易系统。

**阶段1结束后可以做:**
- 做一个可展示项目: `stock-analysis-tool`。
- 开始准备数学建模国赛: 数据清洗、可视化、建模论文模板。
- 可以参加天池/Kaggle金融风控类新人赛,但目标是练数据流程,不是冲名次。
- 不建议投量化开发实习: 这时还缺C++、算法和系统项目,硬投收益很低。

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
| README/最小测试 | ✅ | Day 16 |
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

每次新 day 开始前，自动检查该 day 的所有依赖项在之前 days 的教学覆盖率。见根目录 `AGENTS.md` 与 `docs/workflows/写课程流程.md`。

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
| 🐳 **whale-quant 量化课程** | [GitHub](https://github.com/datawhalechina/whale-quant) / [本地参考](../resources/lib/whale-quant学习路线参考.md) | **出课参考源**, 各章对应 Day 见右侧 | Day 09+ |
| — ch01 投资与量化投资 | 通识阅读，不依赖编程基础 | 随时 |
| — ch02 金融市场基础概念 | 通识阅读，补充金融基础 | 随时 |
| — ch03 股票数据获取 | **数据采集/清洗出课参考** | **Day 09-13** |
| — ch04 量化选股策略(MPT/CAPM/多因子) | 因子选股综合练习参考 | Day 13-14 |
| — ch05 量化择时策略(双均线/MACD) | 择时策略综合练习参考 | Day 14 |
| — ch06 量化调仓策略(仓位/有效前沿) | 组合优化概念参考 | Day 14(选修) |
| — ch07 量化回测(pandas评估/Backtrader) | 回测评估指标出课参考 | **Day 11-14** |
| — ch08 机器学习与量化策略 | 阶段2-3参考 | 阶段2+ |

---

## 8. 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-05-27 | 初始创建 |
| 2026-05-28 | Day 03 状态改为⚠️部分完成 |
| 2026-05-28 | Day 04 新增 set 集合（完成四大类型覆盖） |
| 2026-05-28 | 新增依赖检查机制说明（后续迁移到 AGENTS.md / workflow） |
| 2026-05-28 | 推荐资源映射更新：加入廖雪峰/Python-100-Days/资源库/菜鸟/鱼皮AI Guide |
| 2026-05-28 | 新增四大基础类型覆盖进度表 |
| 2026-06-03 | 新增 whale-quant 出课参考源, Part 2 每日对照章节映射 |
| 2026-06-20 | 数据源替换 yfinance→Baostock, Part 2/3 细化(每课拆学/练/综合+时间预估) |
| 2026-06-20 | 教学模式重构: 复习→知识块1(知识点→练习,块练习)→知识块2(…)→Day综合, 新增 Day 11R/14R 综合测试日 |
| 2026-06-26 | 根据多平台JD复核, 明确阶段1“够用即收”: 不追加Web/AI大项目, 以数据处理小项目+README+最小测试收尾, 尽快进入C++/算法 |
| 2026-06-26 | 新增学习量校准依据: 阶段1每天从阶段终点倒推,标明容量、验收和超量处理 |
| 2026-06-26 | 新增练习依赖校准机制: 每道必做题只能依赖已教内容,未教技术只能选做/预告 |
