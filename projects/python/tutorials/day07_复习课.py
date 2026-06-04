"""
====================================================
 Day 7 | 复习: Python 核心查漏补缺
====================================================

 目标: 综合运用 Days 01-06 的知识,
      找出薄弱环节, 巩固基础

 无 C++ 对比

====================================================
"""

# ═══════════════════════════════════════════════════
# 阶段1: Python 基础 (5周)
# Part 1: Python 核心 (Days 01-07, 2周+)
#
# Day 01 ✅ 变量, 类型, 字符串, I/O
# Day 02 ✅ 列表, 字典, 元组, 推导式
# Day 03 ✅ 函数, 作用域, lambda
# Day 04 ✅ set, 文件 I/O, 异常处理, CSV 读写
# Day 05 ✅ 模块与包, pip, datetime, 路径操作
# Day 06 ✅ 综合项目: 股票数据管理器
# Day 07 ▶ 复习课 (今天!) -- 查漏补缺
#
# Part 2 预告 (Days 08-13):
# Day 08 NumPy 数组运算
# Day 09 Pandas 入门
# Day 10 Pandas 进阶
# Day 11 Matplotlib 可视化
# Day 12 数据采集与清洗
# Day 13 综合练习
# ═══════════════════════════════════════════════════

# 本课全部知识点已在 Days 01-06 教过, 没有新语法.
# 每道题都是跨 days 的综合题, 自己试试能独立完成多少.

# 需要用到的模块
import csv
from datetime import datetime, timedelta


# ═══════════════════════════════════════════════════
# 练习 1: 找 bug (热身)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n练习 1: 找 bug")

# 下面 4 段代码各有 1 个 bug.
# 找出 bug 并修复, 让代码正确运行.
#
# 提示: 类型、索引、可变性、边界条件

# --- 1.1 ---
stock_prices = ["12.5", "12.8", "13.0", "12.9"]
avg = sum(stock_prices) / len(stock_prices)
print(f"均价: {avg}")
above_avg = [p for p in stock_prices if p > avg]

# ↓ 你的代码 ↓


# --- 1.2 ---
codes = ["000001", "000002", "000651"]
prices = [12.5, 8.3, 225.0]
for i in range(len(codes)):
    print(f"{codes[1]}: {prices[i]}")
# 这代码能跑, 但结果不对. 哪错了?

# ↓ 你的代码 ↓


# --- 1.3 ---
def add_stock(portfolio, code, shares):
    portfolio = portfolio.copy()
    portfolio[code] = shares
    return portfolio

my_portfolio = {"000001": 100, "000002": 500}
add_stock(my_portfolio, "000651", 200)
print(my_portfolio)

# 这段代码有 2 个设计问题. 找出来.

# ↓ 你的代码 ↓


# --- 1.4 ---
date_str = "2026-01-05"
dt = datetime.strptime(date_str, "%Y-%m-%d")
next_day = dt + timedelta(days=1)
print(f"下一天: {next_day}")

# 这代码没问题. 但如果 date_str 是 "2026/01/05" 呢?
# 不改 datetime.strptime 的前提下, 先处理字符串.

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 练习 2: 函数 + 数据结构 (Days 02-03)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n练习 2: 组合分析")

# 你手上有 3 个列表: 股票代码, 收盘价, 持仓量.
# 写一个函数 analyze_portfolio, 接受这 3 个列表,
# 返回一个字典, 包含:
#   - "total_value": 总市值 (收盘价 * 持仓量 之和)
#   - "max_stock": 市值最大的股票代码
#   - "min_stock": 市值最小的股票代码
#   - "sorted_by_value": 按市值降序排列的 [(代码, 市值), ...]
#   - "avg_price": 平均收盘价
#
# 提示: 先 zip 再处理. sorted + lambda 能排序.

codes = ["000001", "000002", "000651", "600519", "300750"]
close_prices = [12.5, 8.3, 225.0, 1800.0, 226.5]
holdings = [100, 500, 200, 50, 100]

def analyze_portfolio(codes, prices, shares):
    pass  # 替换为你的实现

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 练习 3: set + 文件 + 异常 (Days 04-05)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n练习 3: 板块交叉分析")

# 有两个板块的股票列表文件:
# data/tech.csv   (科技板块)
# data/finance.csv (金融板块)
#
# 每个文件格式: code,name (无表头, UTF-8)
#
# 写一个函数 analyze_sectors, 完成:
# 1. 安全地读取两个文件 (文件不存在 -> 友好提示)
# 2. 把每只股票代码加入对应板块的 set
# 3. 返回一个 dict:
#    - "tech_only": 科技独有股票 (不在金融的)
#    - "finance_only": 金融独有股票
#    - "common": 交集 (同时在两个板块的)
#    - "total": 并集 (所有股票数)
#
# 提示: set 是去重利器. 文件操作别忘了 try/except.

def analyze_sectors():
    pass  # 替换为你的实现

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 练习 4: 综合管道 (Days 01-06 全覆盖)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n练习 4: 交易日历生成器")

# 给定起始日期和交易日数, 生成一个交易日历 CSV 文件.
# 规则: 周一 ~ 周五为交易日, 周六周日跳过.
#
# 写一个函数 generate_trading_calendar(start_date, days, output_file):
#   start_date: str ("2026-01-05")
#   days: int (要生成的交易日数量)
#   output_file: str (输出的 CSV 路径)
#
# 输出 CSV 格式 (含表头):
#   date,weekday,week_num
#   2026-01-05,星期一,1
#   2026-01-06,星期二,2
#   ...
#
# 提示:
#   - weekday() 返回 0=周一 ... 6=周日
#   - 需要一个中文星期几的映射表
#   - timedelta(days=1) 一天天加, 跳过周末
#   - csv.DictWriter 写 CSV
#   - datetime 运算: 加一天, 判断 weekday
#
# 附加: 如果 output_file 所在目录不存在, 自动创建.

WEEKDAY_NAMES = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]

def generate_trading_calendar(start_date, days, output_file):
    pass  # 替换为你的实现

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 练习 5: 免费题 -- 上强度 (选做)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n练习 5: 多股票区间筛选器 (选做)")

# 文件 stock_data.csv 包含多只股票的多日行情数据.
# 格式: code,date,open,high,low,close,volume
#
# 写一个函数 filter_stocks_by_date(data_path, start, end, codes):
#   data_path: CSV 文件路径
#   start: str "2026-01-06"
#   end: str "2026-01-09"   (含两端)
#   codes: list[str] 要筛选的股票, 比如 ["000001", "000002"]
#
# 返回: dict[str, list[dict]]
#   key = 股票代码, value = 该股票在时间范围内的所有行
#
# 要求:
#   1. 用 csv.DictReader 读文件
#   2. 用推导式筛选日期范围 (字符串可以直接比大小)
#   3. 只返回指定股票的行情, 按股票代码分组
#   4. 如果某股票没有数据, value 为空列表
#   5. 如果文件不存在 -> print("文件未找到") 返回空字典
#
# 提示: 日期字符串 "2026-01-06" 可以直接用 >= <= 比较.

def filter_stocks_by_date(data_path, start, end, codes):
    pass  # 替换为你的实现

# ↓ 你的代码 ↓
