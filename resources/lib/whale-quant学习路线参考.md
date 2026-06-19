# Whale-Quant 量化开源课程参考

> Datawhale 出品 | 8章量化入门课程 | Python 3.9+ | CC BY-NC-SA 4.0
> GitHub: https://github.com/datawhalechina/whale-quant
> 在线文档: https://datawhalechina.github.io/whale-quant/

---

## 适用阶段

**阶段1 Python基础学完（Day 07+）后开始看，边学边练。**
前三章基础，后五章需要 NumPy/Pandas 基础。

---

## 课程全览

| 章 | 标题 | ⏱ 建议时机 | 核心内容 |
|----|------|-----------|---------|
| 1 | 投资与量化投资 | 随时 | 投资概念、股票分析流派、量化流程、平台介绍 |
| 2 | 金融市场基础概念 | 随时 | 宏观经济学/货币金融学/投资学/数理统计基础 |
| 3 | 股票数据获取 | Day 07-08 | baostock/tushare 数据源、pandas 清洗 |
| 4 | 量化选股策略 | **Day 09+** | MPT/CAPM/APT 模型、多因子、因子有效性检验、市值中性化 |
| 5 | 量化择时策略 | **Day 09+** | 双均线、MACD、技术指标择时 |
| 6 | 量化调仓策略 | **Day 10+** | 组合收益率/风险、有效前沿、最佳仓位 |
| 7 | 量化回测 | **Day 10+** | pandas 评估指标、聚宽/Backtrader/BigQuant 回测平台 |
| 8 | 机器学习与量化策略 | **阶段2-3** | 小波去噪、分类选股、时序预测、非结构化数据、深度学习 |

---

## 依赖栈

```txt
tushare==1.3.7      # A股数据接口
pandas==2.1.4        # 数据处理核心
numpy==1.26.3        # 数值计算
matplotlib==3.8.2    # 可视化
```

> ⚠️ tushare 需要 token，注册地址: https://tushare.pro
> 国内直连推荐: baostock（免费稳定，无需 token，Day 09+ 教学用）

---

## 各章详细大纲

### ch01 投资与量化投资
- 投资 vs 投机
- 个人投资品种（股票/基金/债券/房地产）
- 股票投资流程
- 基本面派 vs 技术派 vs 量化派
- 量化投资发展史
- 量化一般流程：数据→策略→回测→实盘
- 常见平台：聚宽、优矿、BigQuant、Backtrader

### ch02 金融市场的基础概念
- 宏观经济学基础
- 货币金融学基础
- 投资学基础概念
- 数理统计基本概念

### ch03 股票数据获取
- 技术面 vs 基本面数据
- baostock 数据获取
- pandas 数据清洗
- tushare / akshare 等其他数据源

### ch04 量化选股策略 🔑
- 有效市场理论（无效→弱式→半强式→强式）
- 单/多因子选股模型
- **MPT 现代资产配置理论**
  - 均值-方差分析、有效前沿
  - 夏普比率、资本市场线
- **CAPM 资本资产定价模型**
  - β系数、系统性风险
  - CAPM 在 A 股的应用
- **APT 套利定价理论** → 多因子模型
- 常见因子分类（技术/宏观/基本面）
- 因子有效性检验（P值）
- 行业与市值中性化（含 statsmodels 代码）

### ch05 量化择时策略
- 量化择时概念
- 双均线策略（金叉/死叉）
- MACD 择时策略

### ch06 量化调仓策略
- 组合收益率计算
- 组合风险度量
- 最优仓位控制（最优化方法）
- Python 实现
- 有效前沿与资本市场线（选修）
- CAPM（选修）

### ch07 量化回测 🔑
- 净值曲线、年化收益率、最大回撤
- pandas 计算评估指标（含代码）
- 聚宽平台回测实践
- Backtrader 框架实践
- BigQuant 框架实战
- 手写回测代码

### ch08 机器学习与量化策略
- 小波分析去噪与股价预测
- 机器学习分类与选股
- 时间序列预测与择时
- 非结构化数据与策略（新闻/舆情）
- 机器学习策略实战（scikit-learn）
- 深度学习策略实战（LSTM/CNN）

---

## 与本学习路线的关系

```
Day 01-06 Python基础 → ch03 数据获取（需基础）
Day 07-08 NumPy/Pandas → ch03/ch07 回测计算
Day 09+ 综合项目 → ch04/ch05/ch06 策略练手
阶段2-3 C++/算法 → ch08 ML策略
```

- **ch01 ch02**：通识阅读，任何时候都能翻，不费劲
- **ch03**：学完 Day 06（文件I/O）就能跟着跑数据
- **ch04 ch05 ch06**：需要 Day 07-08 的数据分析基础
- **ch07**：阶段1后期或阶段2初期的重点
- **ch08**：建议等阶段2-3再碰，需要 ML 基础

---

## 上手方式

```bash
# 克隆
git clone https://github.com/datawhalechina/whale-quant.git
cd whale-quant

# 安装依赖
pip install -r requirements.txt

# 从 notebook/ 目录打开 Jupyter Notebook
jupyter notebook notebook/
```

---

*参考日期: 2026-06-03*
