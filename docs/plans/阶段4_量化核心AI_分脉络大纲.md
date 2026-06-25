# 阶段4: 量化系统主线(75%) + AI工具化辅线(25%) — 分脉络大纲

> 编写依据: 主脉络岗位能力模型 + 2026-06-26多平台JD补充调研 + whale-quant + C++低延迟/交易系统JD
> 调研日期: 2026-06-26
> 学习者: 孙溢镭, 地大(武汉) 数据科学, 大二下
> 时间: 2027年2月 - 2027年7月 (大二下学期, ~6个月/24周)

---

## 1. 定位与目标

**在主脉络中的位置:** 阶段4（共6阶段），**最关键的一学期** — 交易系统项目产出决定实习竞争力

**时间分配:**
- 量化系统主线 (75%): Linux/性能排障/多线程/网络/SQL/金融基础/回测引擎/交易链路模拟器
- AI工具化辅线 (25%): AI编码工具/PyTorch简单因子/RAG资料助手/Agent工具调用
- 考研重叠 (额外): 408 OS/网络/计组 + 数一基础

**目标:**
- **量化:** 完成C++回测引擎 + 简易交易链路模拟器, LeetCode 250题, 可投大二实习
- **AI:** 完成一个轻量RAG/Agent工具化项目, 服务量化资料检索或回测运行
- **考研:** 408(OS/网络/计组)过一轮, 数一基础过完

---

## 2. 总体结构

```
阶段4: 量化系统主线 + AI工具化辅线 (大二下, 2027.2-2027.7, 24周)
├── Part 1: Linux + Git深入 + 性能排障 (4周)
│   ├── Week 1-2: Linux环境/命令/Shell脚本
│   └── Week 3-4: Git工作流 + GDB/perf/日志/简单压测
│
├── Part 2: 多线程 + 网络编程 (6周)
│   ├── Week 5-6: C++多线程(thread/mutex/condition_variable)
│   ├── Week 7-8: 网络编程(socket TCP/UDP)
│   ├── Week 9: 行情接收器(多线程+网络)
│   └── Week 10: LeetCode专题 + 八股
│
├── Part 3: SQL + 金融基础 + 交易链路认知 (4周)
│   ├── Week 11-12: SQL (CRUD/联表/聚合/窗口函数)
│   ├── Week 13-14: 金融基础 (股票/期货/订单簿/撮合/风控/对账)
│
├── Part 4: 项目实战 (6周)
│   ├── Week 15-17: 事件驱动回测引擎 v1 (C++)
│   ├── Week 18-20: 简易交易链路模拟器 (C++)
│
├── Part 5: 实习准备 + 投递 (4周)
│   ├── Week 21-22: 简历+八股+模拟面试
│   ├── Week 23-24: 海投 + 面试
│
└── AI工具化辅线 (并行, 严格不挤占主线)
    ├── Stage 1: AI编码工作流 + PyTorch基础 (Week 5-8)
    ├── Stage 2: 轻量RAG资料助手 (Week 9-14)
    └── Stage 3: Agent工具调用(行情查询/回测运行/报告生成) (Week 15-20)
```

---

## 3. 量化主线 (60%)

### Part 1: Linux + Git + 性能排障 (Week 1-4)

#### Week 1-2: Linux开发环境

| 知识点 | 参考 | 练习 |
|--------|------|------|
| 文件系统 (/, /home, /tmp) | 黑马Linux教程 | 找文件, 权限管理 |
| 常用命令 (ls/cd/grep/find/ps) | 鸟哥Linux | 处理CSV文件 |
| vim/nvim | 30分钟教程 | 写C++代码 |
| Shell脚本基础 | 黑马 | 批量处理数据文件 |
| Makefile/CMake | Cherno C++ | 编译C++项目 |

#### Week 3-4: Git深入 + 性能排障入门

| 知识点 | 参考 | 练习 |
|--------|------|------|
| 分支管理 (branch/merge/rebase) | Git官方文档 | 用分支做实验 |
| 冲突解决 | - | 模拟冲突场景 |
| PR/Code Review流程 | GitHub | 给开源项目提PR |
| GitHub Actions CI | 官方文档 | 自动跑测试 |
| GDB基础 | 官方文档/教程 | 定位段错误和变量变化 |
| perf/time/top | Linux工具 | 对比不同容器/算法耗时 |
| 日志与压测 | 自编 | 给行情处理脚本打日志并做简单压测 |

---

### Part 2: 多线程 + 网络 (Week 5-10)

#### Week 5-6: C++多线程

| 知识点 | 参考 | 量化场景 |
|--------|------|---------|
| thread创建/join/detach | 爱编程的大丙 | 多线程行情处理 |
| mutex/lock_guard/unique_lock | Cherno C++ | 线程安全订单簿 |
| condition_variable | cppreference | 生产者-消费者(行情队列) |
| atomic | cppreference | 无锁计数器 |
| async/future/promise | cppreference | 异步任务(回测) |

**练习:** 多线程股票数据更新器; 生产者-消费者行情队列

#### Week 7-8: 网络编程

| 知识点 | 参考 | 量化场景 |
|--------|------|---------|
| socket 基础 | 陈硕Linux网络编程 | TCP行情接入 |
| TCP状态转换 | 黑马网络编程 | 连接管理 |
| 非阻塞IO/select/poll | muduo | 多路复用 |
| HTTP协议基础 | - | REST API调用 |

**练习:** 用socket从模拟服务器获取行情数据

#### Week 9: 行情接收器
**练习:** 实现一个简易行情接收器 (TCP模拟行情源 + 多线程处理 + 日志 + 简单延迟统计)

#### Week 10: LeetCode + 八股
- 多线程/网络相关 LeetCode 15题
- C++八股: 多线程/同步/锁

---

### Part 3: SQL + 金融基础 + 交易链路认知 (Week 11-14)

#### Week 11-12: SQL

| 知识点 | 参考 | 量化场景 |
|--------|------|---------|
| SELECT/FROM/WHERE | SQLBolt | 查询行情数据 |
| JOIN (INNER/LEFT) | SQLBolt | 多表关联(股票+财务) |
| GROUP BY/HAVING | SQLBolt | 聚合统计 |
| 窗口函数 (ROW_NUMBER/RANK) | LeetCode SQL | 因子排名 |
| 索引/执行计划 | - | 查询优化 |

**练习:** 用SQLite存股票数据, 写5个分析查询; 为行情数据设计数据质量检查表

#### Week 13-14: 金融基础 + 交易链路

| 知识点 | 参考 | 对应 |
|--------|------|------|
| 股票交易规则 (T+1/涨跌停) | whale-quant ch02 | 面试必问 |
| 期货/期权基础概念 | 衍生产品(Hull) | 期权岗 |
| 订单簿/限价单/市价单 | 量化投资黑箱 | 订单系统 |
| 撮合机制/滑点 | 交易与交易所 | 回测精度 |
| 订单生命周期 | 自编 + JD样本 | 下单/撤单/成交回报/持仓资金更新 |
| 风控与对账 | 券商/私募JD | 拒单、部分成交、回报异常、对账差异 |
| 因子:价值/动量/质量 | whale-quant ch04 | 因子计算 |

---

### Part 4: 项目实战 (Week 15-20)

#### Week 15-17: 事件驱动回测引擎 v1 (C++)

**功能:**
- 读取行情CSV
- 支持简单策略 (均线交叉/动量)
- 计算绩效指标 (收益率/夏普/最大回撤)
- 输出绩效报告
- 支持事件流: MarketDataEvent → SignalEvent → OrderEvent → FillEvent

**架构:**
```
DataLoader → EventQueue → Strategy → Portfolio → Metrics → Report
```

**要求:**
- C++17, 智能指针, STL容器
- 支持多线程并行回测 (不同参数)
- 有单元测试/样例数据/性能对比
- GitHub项目, 写README

#### Week 18-20: 简易交易链路模拟器 (C++)

**功能:**
- 模拟行情源: 本地TCP服务推送盘口/成交数据
- 信号模块: 读取行情并生成下单请求
- 订单状态机: New/Submitted/PartiallyFilled/Filled/Cancelled/Rejected
- 风控模块: 仓位上限、单笔金额、涨跌停/停牌模拟检查
- 成交回报: 模拟撮合与成交回报,更新持仓和资金
- 监控日志: 输出延迟、拒单、成交、持仓变化

**架构:**
```
MarketDataServer → Gateway → Strategy → Risk → OrderManager → FillSimulator → Monitor
```

**要求:**
- C++17, socket, thread, condition_variable, queue
- 每个模块有清晰接口, README能画出端到端链路
- 能讲清一次异常: 拒单/部分成交/连接断开/回报异常如何处理

**可选扩展:** C++/Python混合因子计算器(pybind11), IC/IR/分层回测放入Notebook展示。

---

### Part 5: 实习准备 (Week 21-24)

### 投实习触发条件

满足以下 4 条再正式海投,否则先补项目:

| 条件 | 验收标准 |
|------|----------|
| LeetCode | 200题以上,数组/链表/树/哈希/DP基础题能独立写 |
| C++项目 | 回测引擎v1可运行,README有架构图和样例输出 |
| 交易链路 | 能讲清行情→信号→下单→风控→成交回报→持仓资金更新 |
| 简历 | 一页纸,项目能讲30分钟,GitHub链接可打开 |

投递顺序: 小私募/FinTech/券商IT → 实习友好量化私募 → 头部量化试投。

#### Week 21-22: 简历+八股

| 任务 | 产出 |
|------|------|
| 整理GitHub (README/文档) | 3+活跃仓库 |
| 写一页纸简历 | PDF |
| C++八股系统复习 | 脑图 |
| 模拟面试 (录音+复盘) | 录音文件 |

#### Week 23-24: 海投

| 动作 | 目标 |
|------|------|
| BOSS直聘每天投3-5家 | 每周15-25家 |
| 猎聘同步投递 | 每周5-10家 |
| 做题保持手感 | 每天1-2道LeetCode |

---

## 4. AI工具化辅线 (25%, 并行)

### Stage 1: AI编码工作流 + PyTorch基础 (Week 5-8)

| 知识点 | 参考 | 产出 |
|--------|------|------|
| AI辅助读代码 | Claude Code/Cursor | 为C++项目生成模块说明 |
| AI辅助测试 | Claude Code/Cursor | 给回测/订单模块生成测试用例 |
| PyTorch Tensor/Autograd | 土堆PyTorch/d2l | 简单收益率预测实验 |
| 简单ML因子 | d2l + 自编 | 用动量/波动特征做toy模型 |

### Stage 2: 轻量RAG资料助手 (Week 9-14)

| 知识点 | 参考 | 产出 |
|------|------|------|
| 文档切分 | LLM Cookbook | JD/研报/项目README切分 |
| 向量化嵌入 | LLM Cookbook | 本地资料索引 |
| Chroma/FAISS | LLM Cookbook | 检索问答 |
| RAG完整链路 | LLM-Universe | **量化资料问答助手** |

### Stage 3: Agent工具调用 (Week 15-20)

| 知识点 | 参考 | 产出 |
|------|------|------|
| ReAct框架 | LLM Cookbook | 思考-行动-观察循环 |
| Function Calling | LangChain文档 | 工具调用 |
| 工具封装 | 自编 | 行情查询/回测运行/报告生成 |
| **项目:** 量化项目助手 | 自编 | 能调用回测脚本并解释结果 |

> 暂缓: LLM微调、复杂Agent、多模型部署。它们对当前量化开发JD不是硬门槛,阶段5-6有余力再补。

---

## 5. 对齐检查

| 检查项 | 状态 |
|--------|------|
| 1. 岗位要求覆盖 (C++/Linux/多线程/网络/SQL/交易链路/性能排障) | ✅ 全部覆盖 |
| 2. AI辅线降噪 (工具化25%, 不挤占主线) | ✅ |
| 3. AI+量化交叉 (PyTorch因子+LLM另类数据) | ⏳ 可选 |
| 4. 考研重叠 (OS/网络/计组+数一) | ✅ 贯穿 |
| 5. 产出 (回测引擎+交易链路模拟器+GitHub) | ✅ 2个大项目 |
| 6. 实习准备 (简历/八股/投递) | ✅ 最后4周 |

---

## 6. 参考资源

| 资源 | 链接 | 用途 |
|------|------|------|
| 黑马Linux教程 | b23.tv/BV1iJ411S7UA | Linux入门 |
| 爱编程的大丙多线程 | b23.tv/BV1sv41177e4 | C++多线程 |
| 陈硕Linux网络编程 | b23.tv/BV1mm42177mk | 网络编程 |
| SQLBolt | sqlbolt.com | SQL交互式 |
| 邢不行量化投资 | b23.tv/BV1EhkwYUEyt | 量化认知 |
| whale-quant ch04-ch07 | github.com/datawhalechina/whale-quant | 因子+回测 |
| LLM Cookbook | github.com/datawhalechina/llm-cookbook | RAG+Agent主力 |
| LLaMA-Factory | github.com/hiyouga/LLaMA-Factory | 微调框架 |
| Qlib | github.com/microsoft/qlib | AI量化参考 |
