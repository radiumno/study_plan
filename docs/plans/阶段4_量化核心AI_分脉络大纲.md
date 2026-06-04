# 阶段4: 量化核心(60%) + AI应用(40%) — 分脉络大纲

> 编写依据: 主脉络岗位能力模型 + BOSS直聘真实JD + Datawhale LLM Cookbook + whale-quant
> 调研日期: 2026-06-05
> 学习者: 孙溢镭, 地大(武汉) 数据科学, 大二下
> 时间: 2027年2月 - 2027年7月 (大二下学期, ~6个月/24周)

---

## 1. 定位与目标

**在主脉络中的位置:** 阶段4（共6阶段），**最关键的一学期** — 双线并行, 产出决定实习竞争力

**双线分配:**
- 量化主线 (60%): Linux/多线程/网络/SQL/金融基础/回测引擎
- AI辅线 (40%): LangChain/RAG/Agent/PyTorch因子
- 考研重叠 (额外): 408 OS/网络/计组 + 数一基础

**目标:**
- **量化:** 完成C++回测引擎项目, LeetCode 250题, 可投大二实习
- **AI:** 完成RAG+Agent两个可展示项目
- **考研:** 408(OS/网络/计组)过一轮, 数一基础过完

---

## 2. 总体结构

```
阶段4: 量化核心 + AI应用 (大二下, 2027.2-2027.7, 24周)
├── Part 1: Linux + Git深入 (4周)
│   ├── Week 1-2: Linux环境/命令/Shell脚本
│   └── Week 3-4: Git工作流 + 开源项目协作
│
├── Part 2: 多线程 + 网络编程 (6周)
│   ├── Week 5-6: C++多线程(thread/mutex/condition_variable)
│   ├── Week 7-8: 网络编程(socket TCP/UDP)
│   ├── Week 9: 多线程+网络结合 (实战)
│   └── Week 10: LeetCode专题 + 八股
│
├── Part 3: SQL + 金融基础 (4周)
│   ├── Week 11-12: SQL (CRUD/联表/聚合/窗口函数)
│   ├── Week 13-14: 金融基础 (股票/期货/订单簿/撮合)
│
├── Part 4: 项目实战 (6周)
│   ├── Week 15-17: 回测引擎 v1 (C++)
│   ├── Week 18-20: 因子计算器 (C++/Python混合)
│
├── Part 5: 实习准备 + 投递 (4周)
│   ├── Week 21-22: 简历+八股+模拟面试
│   ├── Week 23-24: 海投 + 面试
│
└── AI辅线 (并行, 贯穿Part 1-3 + 暑假)
    ├── Stage 1: LangChain入门 (Week 5-8)
    ├── Stage 2: RAG实战 (Week 9-14)
    ├── Stage 3: Agent开发 (Week 15-20)
    └── Stage 4: LLM微调入門 → 移至暑假(阶段5期间)
```

---

## 3. 量化主线 (60%)

### Part 1: Linux + Git (Week 1-4)

#### Week 1-2: Linux开发环境

| 知识点 | 参考 | 练习 |
|--------|------|------|
| 文件系统 (/, /home, /tmp) | 黑马Linux教程 | 找文件, 权限管理 |
| 常用命令 (ls/cd/grep/find/ps) | 鸟哥Linux | 处理CSV文件 |
| vim/nvim | 30分钟教程 | 写C++代码 |
| Shell脚本基础 | 黑马 | 批量处理数据文件 |
| Makefile/CMake | Cherno C++ | 编译C++项目 |

#### Week 3-4: Git深入 + 开源协作

| 知识点 | 参考 | 练习 |
|--------|------|------|
| 分支管理 (branch/merge/rebase) | Git官方文档 | 用分支做实验 |
| 冲突解决 | - | 模拟冲突场景 |
| PR/Code Review流程 | GitHub | 给开源项目提PR |
| GitHub Actions CI | 官方文档 | 自动跑测试 |

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

**练习:** 多线程股票数据更新器

#### Week 7-8: 网络编程

| 知识点 | 参考 | 量化场景 |
|--------|------|---------|
| socket 基础 | 陈硕Linux网络编程 | TCP行情接入 |
| TCP状态转换 | 黑马网络编程 | 连接管理 |
| 非阻塞IO/select/poll | muduo | 多路复用 |
| HTTP协议基础 | - | REST API调用 |

**练习:** 用socket从模拟服务器获取行情数据

#### Week 9: 多线程+网络结合
**练习:** 实现一个简易的行情接收器 (TCP + 多线程处理)

#### Week 10: LeetCode + 八股
- 多线程/网络相关 LeetCode 15题
- C++八股: 多线程/同步/锁

---

### Part 3: SQL + 金融基础 (Week 11-14)

#### Week 11-12: SQL

| 知识点 | 参考 | 量化场景 |
|--------|------|---------|
| SELECT/FROM/WHERE | SQLBolt | 查询行情数据 |
| JOIN (INNER/LEFT) | SQLBolt | 多表关联(股票+财务) |
| GROUP BY/HAVING | SQLBolt | 聚合统计 |
| 窗口函数 (ROW_NUMBER/RANK) | LeetCode SQL | 因子排名 |
| 索引/执行计划 | - | 查询优化 |

**练习:** 用SQLite存股票数据, 写5个分析查询

#### Week 13-14: 金融基础

| 知识点 | 参考 | 对应 |
|--------|------|------|
| 股票交易规则 (T+1/涨跌停) | whale-quant ch02 | 面试必问 |
| 期货/期权基础概念 | 衍生产品(Hull) | 期权岗 |
| 订单簿/限价单/市价单 | 量化投资黑箱 | 订单系统 |
| 撮合机制/滑点 | 交易与交易所 | 回测精度 |
| 因子:价值/动量/质量 | whale-quant ch04 | 因子计算 |

---

### Part 4: 项目实战 (Week 15-20)

#### Week 15-17: 回测引擎 v1 (C++)

**功能:**
- 读取行情CSV
- 支持简单策略 (均线交叉/动量)
- 计算绩效指标 (收益率/夏普/最大回撤)
- 输出绩效报告

**架构:**
```
DataLoader → Strategy → Portfolio → Metrics → Report
```

**要求:**
- C++17, 智能指针, STL容器
- 支持多线程并行回测 (不同参数)
- GitHub项目, 写README

#### Week 18-20: 因子计算器 (C++/Python混合)

**功能:**
- C++核心: 因子计算 (动量/波动/反转等)
- Python绑定: 用pybind11封装C++因子
- Jupyter Notebook: 因子分析 (IC/IR/分层回测)

**参考:** whale-quant ch04 (因子选股), Qlib (AI因子)

---

### Part 5: 实习准备 (Week 21-24)

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

## 4. AI辅线 (40%, 并行)

### Stage 1: LangChain入门 (Week 5-8)

| 知识点 | 参考 | 产出 |
|--------|------|------|
| Chain (LLMChain/SimpleSequentialChain) | LLM Cookbook | 简单问答链 |
| Prompt Template | LangChain官方文档 | 模板化提示 |
| Memory (ConversationBufferMemory) | LLM Cookbook | 多轮对话 |
| Tool/Agent概念 | LLM Cookbook | Agent初探 |

### Stage 2: RAG实战 (Week 9-14)

| 知识点 | 参考 | 产出 |
|------|------|------|
| 文档切分 (RecursiveCharacterTextSplitter) | LLM Cookbook | PDF/文本切分 |
| 向量化嵌入 (OpenAI/HuggingFace) | LLM Cookbook | 向量数据库 |
| Chroma/FAISS 向量存储 | LLM Cookbook | 文档检索 |
| RAG完整链路 (检索+生成) | LLM-Universe | **RAG知识库系统** |

### Stage 3: Agent开发 (Week 15-20)

| 知识点 | 参考 | 产出 |
|------|------|------|
| ReAct框架 | LLM Cookbook | 思考-行动-观察循环 |
| Function Calling | LangChain文档 | 工具调用 |
| 多工具编排 | LLM Cookbook | 组合工具 |
| **项目:** 量化数据查询Agent | 自编 | Agent+量化数据 |

### Stage 4: LLM微调入門 → 移至暑假

> ⚠️ 阶段4内容量过高, 微调部分移到暑假(阶段5期间)进行.
> 阶段4 Week 21-24 专注: 实习准备 + 项目收尾 + 刷题.

暑假微调安排:

| 知识点 | 参考 | 时间估计 |
|------|------|---------|
| LoRA/QLoRA原理 | Happy-LLM | 2天 |
| LLaMA-Factory实战 | LLaMA-Factory | 3天 |
| 数据集准备+微调 | Self-LLM | 3天 |
| **产出:** 微调后的模型 + 使用文档 | — | 1周 |

---

## 5. 对齐检查

| 检查项 | 状态 |
|--------|------|
| 1. 岗位要求覆盖 (多线程80%+/网络60%+/SQL50%+/金融50%) | ✅ 全部覆盖 |
| 2. AI辅线完整 (LangChain/RAG/Agent/微调) | ✅ 4个Stage (微调移至暑假减压) |
| 3. AI+量化交叉 (PyTorch因子+LLM另类数据) | ⏳ 可选 |
| 4. 考研重叠 (OS/网络/计组+数一) | ✅ 贯穿 |
| 5. 产出 (回测引擎+因子+GitHub) | ✅ 2个大项目 |
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
