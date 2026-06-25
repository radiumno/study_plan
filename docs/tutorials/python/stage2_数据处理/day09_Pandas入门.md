---
title: Day 09 | Pandas 入门 — 从 NumPy 到 DataFrame
description: 课程源码镜像页，由 scripts/sync_docs.py 生成
---

# Day 09 | Pandas 入门 — 从 NumPy 到 DataFrame

> 来源文件: `projects/python/stage2_数据处理/day09_Pandas入门.py`
> 说明: 这是文档站镜像页，课程源码仍以项目目录中的 `.py` 文件为准。

```python
"""
====================================================
 Day 09 | Pandas 入门 — 从 NumPy 到 DataFrame
====================================================

 目标: 学会用 Pandas 处理表格数据 (量化开发日常用最多)

 副线: JSON 数据处理

 参考源:
   - Pandas 官方 Getting Started (pandas.pydata.org/docs/getting_started/)
   - 尚硅谷 Python 数据分析 (b23.tv/BV1D9GLzyEL6)
   - whale-quant ch03 股票数据获取 (github.com/datawhalechina/whale-quant)
   - Real Python Pandas 教程 (realpython.com/pandas-python-explore-dataset)

 三线:
   量化主线 (80%): Pandas 数据分析 + 模拟数据/Baostock
   AI辅线 (10%): 简要提及 Pandas 是 ML 预处理的核心
   考研(10%): 本日以实操为主, 与计组/OS 无直接重叠

====================================================
"""

# ═══════════════════════════════════════════════════
# 前情回顾 — Day 08+08R: NumPy 数组运算
# ═══════════════════════════════════════════════════
# NumPy 的问题是: 数组没有"列名", 你只能记住
#   第 0 列是茅台, 第 1 列是招行...
# 而且不能处理缺失值、时间索引.
# Pandas 就是来解决这些问题的.

print("\n" + "=" * 50)
print("Day 09 | Pandas 入门")
print("=" * 50)

# ═══════════════════════════════════════════════════
# 一, Series — 带标签的一维数组
# ═══════════════════════════════════════════════════
# Series = NumPy 数组 + 索引 (标签)
# 你可以通过标签来访问元素, 不再是 arr[0] 而是 s['茅台']

import numpy as np
import pandas as pd

# --- 1.1 创建 Series ---

# 从 list 创建 (默认索引 0,1,2,...)
"s1 = pd.Series([12.5, 12.8, 12.4])"
"print(s1)"
"# 0    12.5"
"# 1    12.8"
"# 2    12.4"
"# dtype: float64"
""
# Series 有两部分: values (NumPy 数组) + index (标签)
# 可以看左列是 index, 右列是 values

# 指定 index 参数:
"s2 = pd.Series([12.5, 12.8, 12.4], index=['周一', '周二', '周三'])"
"print(s2)"
"# 周一    12.5"
"# 周二    12.8"
"# 周三    12.4"
"# dtype: float64"

# 从 dict 创建 (key 自动变成 index):
"prices_dict = {'茅台': 1800.0, '招行': 35.5, '宁德': 225.0}"
"s3 = pd.Series(prices_dict)"
"print(s3)"
"# 茅台    1800.0"
"# 招行      35.5"
"# 宁德     225.0"
"# dtype: float64"

# 从 NumPy 数组创建:
"arr = np.array([12.5, 12.8, 12.4])"
"s4 = pd.Series(arr, index=['a', 'b', 'c'])"

# --- 1.2 Series 的属性和运算 ---

# 查看属性:
"print(s2.values)   # [12.5 12.8 12.4]   (底层 NumPy 数组)"
"print(s2.index)    # Index(['周一', '周二', '周三'], dtype='object')"
"print(s2.dtype)    # float64"
""
# .values 返回 NumPy 数组 — 说明 Series 底层就是 NumPy 加了个标签层

# 按标签访问:
"print(s2['周二'])    # 12.8   (通过 index 标签)"
"print(s2[0])         # 12.5   (通过位置, 和 NumPy 一样)"
"print(s2['周一':'周三'])  # 标签切片: 包含结尾! (和 list 切片不同)"
""
# ⚠️ 标签切片是"包含结尾"的! 因为标签不一定是数字.
#    而位置切片 (0:2) 仍然是左闭右开.

# 向量化运算 (和 NumPy 一样):
"print(s2 + 1)      # 每个元素 +1"
"print(s2.mean())   # 均值 12.566..."
"print(s2.max())    # 最大值 12.8"
""
# 布尔索引 (和 NumPy 一样):
"print(s2[s2 > 12.6])  # 周二, 周三"


print("\n" + "=" * 40 + "\n练习 1: Series 创建与操作")

# ■ 练习 1.1: 从 list 创建 Series
#
# 给定 5 天的收盘价, 创建 Series:
#   - 数值: [12.5, 12.8, 13.0, 12.9, 13.2]
#   - 索引: ['Day1', 'Day2', 'Day3', 'Day4', 'Day5']
# 打印: Series, values, index, dtype

prices_list = [12.5, 12.8, 13.0, 12.9, 13.2]

# ↓ 你的代码 ↓
s1 = pd.Series(prices_list,index = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
print(s1)
print(s1.values)
print(s1.index)
print(s1.dtype)


# ■ 练习 1.2: 从 dict 创建 Series (更常见)
#
# 以下 dict 表示 3 只股票的收盘价:
#   创建 Series, 然后找出价格 > 226 的股票

stock_close = {'茅台': 1800.0, '招行': 35.5, '宁德': 226.5, '平安': 48.0}

# ↓ 你的代码 ↓
s2 = pd.Series(stock_close)
print(s2[s2 > 226])


# ■ 练习 1.3: 向量化运算
#
# 给定 Series, 计算:
#   1. 平均价和标准差
#   2. 最大值的标签 (用 .idxmax())
#   3. 找出所有价格 > 平均值 的标签

closes = pd.Series([12.5, 12.8, 13.0, 12.9, 13.2],
                    index=['周一', '周二', '周三', '周四', '周五'])

# ↓ 你的代码 ↓
avg = closes.mean()
std = closes.std()
max_index = closes.idxmax()
print(avg,std,max_index)
print(closes.index[closes > avg])


# ═══════════════════════════════════════════════════
# 二, DataFrame — 带标签的二维表格
# ═══════════════════════════════════════════════════
# DataFrame = 多个 Series 拼成的表格.
# 每列是一个 Series, 共享同一个 index (行标签).

# --- 2.1 创建 DataFrame ---

# 从 dict of list 创建 (最直观):
"df = pd.DataFrame({"
"    '茅台': [1800, 1810, 1805, 1820],"
"    '招行': [35.5, 35.8, 35.2, 35.9],"
"    '宁德': [225, 226.5, 224, 227.5]"
"})"
"print(df)"
"#     茅台    招行    宁德"
"# 0  1800.0  35.5  225.0"
"# 1  1810.0  35.8  226.5"
"# 2  1805.0  35.2  224.0"
"# 3  1820.0  35.9  227.5"
""
# dict 的 key → 列名
# list 的每个元素 → 一行

# 指定行索引:
"df2 = pd.DataFrame({"
"    'Close': [12.5, 12.8, 13.0],"
"    'Volume': [10000, 12000, 11000]"
"}, index=['周一', '周二', '周三'])"

# 从 NumPy 数组创建 (指定列名和行索引):
"arr = np.array([[1800, 35.5], [1810, 35.8]])"
"df3 = pd.DataFrame(arr, columns=['茅台', '招行'], index=['Day1', 'Day2'])"

# --- 2.2 查看 DataFrame ---

"print(df.shape)      # (4, 3)  (行数, 列数)"
"print(df.columns)    # Index(['茅台', '招行', '宁德'], dtype='object')"
"print(df.index)      # RangeIndex(start=0, stop=4, step=1)"
"print(df.dtypes)     # 每列的数据类型"
"print(df.values)     # 底层 NumPy 数组 (shape: 4x3)"
""
# df.head(n) 看前 n 行
"print(df.head(2))    # 前 2 行"
"print(df.tail(1))    # 最后 1 行"
""
# df.info() 概览
"print(df.info())"
"# <class 'pandas.core.frame.DataFrame'>"
"# RangeIndex: 4 entries, 0 to 3"
"# Data columns (total 3 columns):"
"#  #   Column  Non-Null Count  Dtype"
"# ---  ------  --------------  -----"
"#  0   茅台      4 non-null      float64"
"#  1   招行      4 non-null      float64"
"#  2   宁德      4 non-null      float64"
""
# df.describe() 统计摘要 (均值/标准差/分位数...)
"print(df.describe())"
"#             茅台         招行         宁德"
"# count     4.00000    4.00000    4.00000"
"# mean   1808.75000   35.60000  225.75000"
"# std       8.53913    0.31623    1.50000"
"# min    1800.00000   35.20000  224.00000"
"# 25%    1803.75000   35.42500  224.75000"
"# 50%    1807.50000   35.65000  225.75000"
"# 75%    1812.50000   35.82500  226.87500"
"# max    1820.00000   35.90000  227.50000"


print("\n" + "=" * 40 + "\n练习 2: 创建和查看 DataFrame")

# ■ 练习 2.1: 从 dict 创建 DataFrame
#
# 3 只股票, 5 个交易日的行情:
#   股票: ['平安', '万科', '格力']
#   数据: (5 行 x 3 列)
#     Day1: [48.5, 28.2, 42.0]
#     Day2: [49.0, 28.5, 42.5]
#     Day3: [48.8, 28.0, 41.5]
#     Day4: [49.2, 28.8, 43.0]
#     Day5: [49.5, 29.0, 43.2]
#   行索引: ['Day1', 'Day2', 'Day3', 'Day4', 'Day5']
#
# 创建后打印:
#   - DataFrame
#   - shape, columns, dtypes
#   - 用 .describe() 看统计摘要

# ↓ 你的代码 ↓
data = [[48.5, 28.2, 42.0],[49.0, 28.5, 42.5],[48.8, 28.0, 41.5],[49.2, 28.8, 43.0],[49.5, 29.0, 43.2]]
df1 = pd. DataFrame(data,columns=['平安', '万科', '格力'],index =['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])
print(df1)
print(df1.shape)
print(df1.columns)
print(df1.dtypes)
print(df1.describe())

# ■ 练习 2.2: 从 NumPy 创建
#
# 给定 NumPy 数组 (5 天 x 3 只股票) 和列名,
# 创建 DataFrame.

price_data = np.array([
    [48.5, 28.2, 42.0],
    [49.0, 28.5, 42.5],
    [48.8, 28.0, 41.5],
    [49.2, 28.8, 43.0],
    [49.5, 29.0, 43.2]
])
stock_names = ['平安', '万科', '格力']
trading_days = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5']

# ↓ 你的代码 ↓
df2 = pd.DataFrame(price_data , columns=stock_names,index = trading_days)
print(df2)


# ═══════════════════════════════════════════════════
# 三, DataFrame 的列操作
# ═══════════════════════════════════════════════════

# --- 3.1 选择列 ---

# 选择一列: 返回 Series
"print(df['茅台'])    # 通过列名 (推荐, 和 dict 一致)"
"print(df.茅台)      # 通过属性 (方便但有限制: 列名不能是关键字)"
""
# 选择多列: 返回 DataFrame
"print(df[['茅台', '宁德']])  # 双中括号 -> 外面是 df[], 里面是 list"

# --- 3.2 添加/修改/删除列 ---

# 添加新列 (向量化, 和 NumPy 一样):
"df['成交量'] = [10000, 12000, 11000, 11500]"
"df['涨跌幅'] = df['茅台'] / df['茅台'].shift(1) - 1"
""
# df.shift(1)   → 数据整体下移一行 (昨天)
# df.shift(-1)  → 数据整体上移一行 (明天)
# shift 是 Pandas 实现"昨日数据"的核心方法

# 删除列:
"df = df.drop('涨跌幅', axis=1)   # 返回新 DataFrame (不修改原 df)"
"df.drop('涨跌幅', axis=1, inplace=True)  # 直接修改原 df"

# --- 3.3 选择行 ---

# 通过行标签: df.loc[行标签]
"print(df.loc[0])          # 第 0 行 (Series)"
"print(df.loc[[0, 2]])     # 第 0 和 2 行 (DataFrame)"
"print(df.loc[0:2])        # 标签切片: 包含 2! (左闭右闭)"
""
# 通过行位置: df.iloc[位置]
"print(df.iloc[0])         # 第 0 行"
"print(df.iloc[0:2])       # 位置切片: 左闭右开 (和 list 一样)"
"print(df.iloc[[0, 2]])    # 第 0 和 2 行"
""
# 布尔索引 (和 NumPy 一样):
"print(df[df['茅台'] > 1810])  # 茅台 > 1810 的行"

# 行列同时选: df.loc[行, 列]
"print(df.loc[0:2, ['茅台', '宁德']])      # 前 3 行的茅台和宁德"
"print(df.iloc[0:3, [0, 2]])               # 一样, 但用位置索引"


print("\n" + "=" * 40 + "\n练习 3: 列和行操作")

# ■ 练习 3.1: 列操作
#
# 给定 DataFrame, 完成:
#   1. 用 df['列名'] 选择 '宁德' 列 (Series)
#   2. 用 df[['列名1','列名2']] 选择 '茅台' 和 '招行' (DataFrame)
#   3. 添加新列 '均价': 茅台、招行、宁德 3 列的平均值
#      (用 .mean(axis=1), 向量化)
#   4. 添加新列 '涨跌幅': 茅台每日涨跌幅 (用 shift)

df_stocks = pd.DataFrame({
    '茅台': [1800.0, 1810.5, 1805.0, 1820.0, 1835.0],
    '招行': [35.5, 35.8, 35.2, 35.9, 36.5],
    '宁德': [225.0, 226.5, 224.0, 227.5, 229.0]
}, index=['Day1', 'Day2', 'Day3', 'Day4', 'Day5'])

# ↓ 你的代码 ↓
print(df_stocks['宁德'])
print(df_stocks[['招行','茅台']])
df_stocks['平均值']=df_stocks.mean(axis = 1)
df_stocks['茅台涨跌幅']=df_stocks['茅台']/df_stocks['茅台'].shift(1)-1
print(df_stocks)


# ■ 练习 3.2: 行操作
#
# 用上面创建好的 df_stocks, 用 loc/iloc 完成:
#   1. 用 df.loc 取出 Day3 的全部数据
#   2. 用 df.iloc 取出前 3 行
#   3. 用布尔索引找出茅台 > 1810 的行
#   4. 用 df.loc[行, 列] 取出 Day2~Day4 的 '茅台' 和 '宁德'
#   5. 用 df.iloc 取出第 0, 2, 4 行的第 0, 2 列

# ↓ 你的代码 ↓
print(df_stocks.loc['Day1':'Day3'])
print(df_stocks.iloc[:3])
print(df_stocks[df_stocks['茅台'] >1810])
print(df_stocks.loc['Day2':'Day4',['茅台','宁德']])
print(df_stocks.iloc[[0,2,4],[0,2]])

# ═══════════════════════════════════════════════════
# 四, CSV 文件读写 + JSON 基础
# ═══════════════════════════════════════════════════
# 量化开发每天要处理 CSV (历史数据, 因子数据, 回测结果...)

# ═══════════════════════════════════════════════════
# 四, 数据读写 — CSV / JSON
# ═══════════════════════════════════════════════════
#
# 量化开发日常: CSV 存本地历史数据, JSON 从 API 拉实时数据.
# Pandas 两种都能直接读, 省去手动解析的麻烦.

# --- 4.1 CSV 读写 ---
#
# CSV (Comma-Separated Values) 是表格数据最通用的格式.
# 打开就是 Excel 表格的样子: 第一行列名, 后面每行一条记录.
#
# 举个栗子, 一个 CSV 文件长这样:
#   date,茅台,招行,宁德
#   2024-01-02,1800.5,35.2,225.0
#   2024-01-03,1810.0,35.5,228.5
#
# Pandas 用 pd.read_csv 读, pd.DataFrame.to_csv 写.

# 读取 CSV:
# df_csv = pd.read_csv('data.csv')               # 默认: 第一行当列名
# df_csv = pd.read_csv('data.csv', index_col=0)  # 第 0 列作为行索引 (一般用日期列)
# df_csv = pd.read_csv('data.csv', parse_dates=['date'])  # 把 date 列解析为时间类型

# 写入 CSV:
# df.to_csv('output.csv')               # 默认: 包含行索引 → 会多一列 Unnamed:0
# df.to_csv('output.csv', index=False)  # 不写行索引 (绝大多数场景用这个)
# df.to_csv('output.csv', index=False, encoding='utf-8-sig')  # Excel 打开不乱码

# 关键区别: index=False 是否把行索引也写进文件.
# 读回来时如果写了索引就用 index_col=0 恢复, 没写就不用.


# --- 4.2 JSON 基础 ---
#
# CSV 适合存本地文件, 但量化系统从 API (数据供应商/交易所) 拿到的
# 数据通常是 JSON 格式. 比如拉实时行情, 返回的是一段 JSON 文本.
#
# JSON = JavaScript Object Notation, 和 Python 的 dict/list 长得几乎一样:
#   Python dict:  {"name": "茅台", "price": 1800.0}
#   JSON 文本:    {"name": "茅台", "price": 1800.0}
# 所以转换非常自然, 但注意 JSON 是"文本"(字符串), Python dict 是内存对象.

import json

# --- dumps / loads: 内存中的转换 ---

# dumps = dict → JSON 字符串 ("序列化")
"data = {'name': '茅台', 'price': 1800.0, 'volume': 10000}"
"json_str = json.dumps(data, ensure_ascii=False)"
"print(json_str)  # {'name': '茅台', 'price': 1800.0, 'volume': 10000}"
""
# ensure_ascii=False 才能保留中文! 不加的话中文会变成 茶...
"json_str_ascii = json.dumps(data)"
"print(json_str_ascii)  # {'name': '\\u8336... 根本没法读"
""
# loads = JSON 字符串 → Python dict ("反序列化")
"parsed = json.loads(json_str)"
"print(parsed['name'])    # '茅台'"
"print(type(parsed))      # <class 'dict'>"

# --- dump / load: 直接读写文件 (没有 s) ---

# dump 直接写文件 (不用先 dumps 再 write):
# data = {'name': '茅台', 'price': 1800.0}
# with open('stock.json', 'w') as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# load 直接从文件读:
# with open('stock.json', 'r') as f:
#     data = json.load(f)          # json.load 不是 loads!
#     print(data['name'])

# 记忆口诀: dumps/loads 有 s → 处理字符串 (string)
#           dump/load   无 s → 处理文件 (stream)


# --- pd.read_json: JSON 直接转 DataFrame ---
#
# 量化场景最常见的是 API 返回了一个 JSON 列表:
# [
#   {"name": "茅台", "price": 1800},
#   {"name": "招行", "price": 35.5}
# ]
# 这种结构 = list of dict, 就是 DataFrame 的行列表.
# pd.read_json 可以直接解析, 一步到位:

"json_list = '[{\"name\": \"茅台\", \"price\": 1800}, {\"name\": \"招行\", \"price\": 35.5}]'"
"df_from_json = pd.read_json(json_list)"
"print(df_from_json)"
"#    name   price"
"# 0   茅台  1800.0"
"# 1   招行    35.5"

# 等价的两步走 (先 json.loads 解析, 再 pd.DataFrame 转换):
"data_list = json.loads(json_list)   # JSON 字符串 → list of dict"
"df_alt = pd.DataFrame(data_list)    # list of dict → DataFrame"
"print(df_alt)"
"# 输出和上面一模一样"

# 两步走的好处是可以在中间做数据清洗,
# 比如过滤、修改字段名再转 DataFrame.


print("\n" + "=" * 40 + "\n练习 4: CSV + JSON")

# ■ 练习 4.1: CSV 读写
#
# 1. 把 df_stocks 写入 'stocks.csv', 不写行索引
# 2. 用 pd.read_csv 读回来
# 3. 打印读回来的 DataFrame, 确认和原来一样

# ↓ 你的代码 ↓
df_stocks.to_csv('stocks.csv',index = False)
df_json=pd.read_csv('stocks.csv')
print(df_json)


# ■ 练习 4.2: JSON 解析
#
# 以下是从 API 获取到的 JSON 格式股票数据,
# 解析为 list of dict, 然后转为 DataFrame.
# 最后计算每只股票的 "成交额" (价 × 量)

api_response = '''
[
    {"code": "000001", "name": "平安银行", "price": 12.5, "volume": 50000},
    {"code": "000002", "name": "万科A", "price": 28.2, "volume": 35000},
    {"code": "000651", "name": "格力电器", "price": 42.0, "volume": 28000}
]
'''

# 提示: json.loads() → list of dict → pd.DataFrame()
#       然后添加成交额列

# ↓ 你的代码 ↓
data_list = json.loads(api_response)
df_from_json = pd.DataFrame(data_list)
df_from_json['成交额'] = df_from_json['price']*df_from_json['volume']
print(df_from_json)



# ═══════════════════════════════════════════════════
# 五, 模拟股票数据 -- 无需网络
# ═══════════════════════════════════════════════════
# yfinance 在国内用不了, 我们用 numpy 生成模拟行情数据.
# 一行代码就能拿到真实股票数据, 返回的就是 DataFrame.

# 固定种子, 每次运行结果一样, 不影响练习.

# --- 5.1 生成模拟股票数据 ---

# 国内 yfinance 用不了, 我们用 NumPy 生成模拟数据.
# 固定种子, 每次运行结果一样.

np.random.seed(42)
dates_5 = pd.date_range('2024-01-02', '2024-03-31', freq='B')

# 生成 3 只股票的模拟收盘价:
sim_prices = pd.DataFrame({
    'AAPL':  180 * np.cumprod(1 + np.random.randn(len(dates_5)) * 0.015),
    'MSFT':  380 * np.cumprod(1 + np.random.randn(len(dates_5)) * 0.012),
    'GOOGL': 140 * np.cumprod(1 + np.random.randn(len(dates_5)) * 0.018),
}, index=dates_5)

print(sim_prices.head())
print(sim_prices.describe())

# 参数说明:
#   180/380/140:   起始股价 (模拟 AAPL/MSFT/GOOGL 的价位)
#   0.015/0.012/0.018: 日波动率 (标准差), 值越大股价越波动
#   np.cumprod(1 + rets): 累乘涨跌幅, 生成价格序列
#   freq='B': 仅交易日 (Business day, 周一到周五)

# Baostock 也能拉股票基本信息:
"# rs = bs.query_stock_basic(code='sz.000001')"
""
# .info 返回股票基本面字段


print("\n" + "=" * 40 + "\n练习 5: 模拟股票数据分析")

# ■ 练习 5.1: 查看股票数据
#
# 用上面生成的 sim_prices:
#   1. 打印前 5 行和后 5 行
#   2. 用 describe() 看统计摘要
#   3. 找出 3 只股票中, 哪只均价最高

# ↓ 你的代码 ↓
print(sim_prices.head())
print(sim_prices.tail())
print(sim_prices.describe())
print(sim_prices.mean())


# ■ 练习 5.2: 多股票分析
#
# 用 sim_prices 计算:
#   1. 每只股票的均价
#   2. 每只股票的最高价和最低价
#   3. 三只股票中, 哪只波动最大 (标准差)
#
# ⚠️ 这里的列名就是 'AAPL'/'MSFT'/'GOOGL', 不是 MultiIndex,
#    直接用 df['AAPL'] 取值即可.

# ↓ 你的代码 ↓
avg = sim_prices.mean(axis=0)
max_ = sim_prices.max(axis=0)
min_ = sim_prices.min(axis=0)
std_ = sim_prices.std(axis=0)
std_max = std_.argmax()



# ═══════════════════════════════════════════════════
# ▸ 综合练习: 多股票数据分析 (离线可用)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 50)
print("综合练习: 多股票数据分析")
print("=" * 50)

# 生成 4 只股票的 6 个月模拟数据 (和 Day 10 的练习类似)
np.random.seed(2024)
dates_comp = pd.date_range('2024-01-02', '2024-06-01', freq='B')

portfolio = pd.DataFrame({
    'AAPL':  180 * np.cumprod(1 + np.random.randn(len(dates_comp)) * 0.015),
    'MSFT':  380 * np.cumprod(1 + np.random.randn(len(dates_comp)) * 0.012),
    'GOOGL': 140 * np.cumprod(1 + np.random.randn(len(dates_comp)) * 0.018),
    'AMZN':  150 * np.cumprod(1 + np.random.randn(len(dates_comp)) * 0.016),
}, index=dates_comp)

# 组合运用今天学过的所有知识点:
#   1. 用 .head() 和 .describe() 查看数据概览
#   2. 找出每只股票的最高收盘价和对应日期
#      (提示: .max() + .idxmax())
#   3. 计算每只股票的累计收益率:
#      累计收益率 = 最后一天 / 第一天 - 1
#      (提示: .iloc[-1] / .iloc[0] - 1)
#   4. 用布尔索引找出 AAPL 收盘价 > 200 的天数
#   5. (附加) 把分析结果保存为 CSV

# ↓ 你的代码 ↓
close_price = portfolio
print(close_price.head(10))
print(close_price.describe())
max_price = close_price.max(axis=0)
max_price_index = close_price.idxmax(axis=0)
ratio = close_price.iloc[-1] / close_price.iloc[0] - 1

apple_stock = close_price['AAPL']
high_apple_days = sum(apple_stock > 200)
result = pd.DataFrame({
    '最高收盘价': max_price,
    '最高日期': max_price_index,
    '累计收益率': ratio
})
result.to_csv('stock_analysis.csv')


# ═══════════════════════════════════════════════════
# ▸ 附: Baostock 真实 A 股数据 (国内直连)
# ═══════════════════════════════════════════════════
#
# 上面的练习用模拟数据, 但你需要学会拉真实数据.
# Baostock 免费直连, 无需注册, 极其稳定.
#
# 拉取平安银行(000001) 2024年日线:

"import baostock as bs"
"import pandas as pd"
""
"# 登录 (免费, 无需注册)"
"bs.login()"
""
"rs = bs.query_history_k_data_plus("
"    'sz.000001',"
"    'date,open,close,high,low,volume',"
"    start_date='2024-01-01', end_date='2024-12-31'"
")"
"df_bs = rs.get_data()"
"bs.logout()"
""
"# 类型转换 (Baostock 返回字符串)"
"for col in ['open', 'close', 'high', 'low', 'volume']:"
"    df_bs[col] = df_bs[col].astype(float)"
""
"# 日期设索引"
"df_bs.index = pd.to_datetime(df_bs['date'])"
"print(df_bs[['open', 'close']].head())"
"print(f'\\n行数: {len(df_bs)}')"
""
# 参数说明:
#   bs.login(): 必须登录, 免费无密码
#   query_history_k_data_plus(代码, 字段列表, 起止日期)
#     代码格式: sh.600000 (上海), sz.000001 (深圳)
#     字段: date,open,close,high,low,volume 等
#   .get_data(): 返回 DataFrame, 但全是字符串
#   bs.logout(): 释放连接
#
# ⚠️ Baostock 数据是 T+1 更新, 今天看不到今天的数据.
```
