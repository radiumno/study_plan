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
   量化主线 (80%): Pandas 数据分析 + yfinance 拉取股票
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


# ■ 练习 1.2: 从 dict 创建 Series (更常见)
#
# 以下 dict 表示 3 只股票的收盘价:
#   创建 Series, 然后找出价格 > 226 的股票

stock_close = {'茅台': 1800.0, '招行': 35.5, '宁德': 226.5, '平安': 48.0}

# ↓ 你的代码 ↓


# ■ 练习 1.3: 向量化运算
#
# 给定 Series, 计算:
#   1. 平均价和标准差
#   2. 最大值的标签 (用 .idxmax())
#   3. 找出所有价格 > 平均值 的标签

closes = pd.Series([12.5, 12.8, 13.0, 12.9, 13.2],
                    index=['周一', '周二', '周三', '周四', '周五'])

# ↓ 你的代码 ↓


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


# ■ 练习 3.2: 行操作
#
# 用上面创建好的 df_stocks, 用 loc/iloc 完成:
#   1. 用 df.loc 取出 Day3 的全部数据
#   2. 用 df.iloc 取出前 3 行
#   3. 用布尔索引找出茅台 > 1810 的行
#   4. 用 df.loc[行, 列] 取出 Day2~Day4 的 '茅台' 和 '宁德'
#   5. 用 df.iloc 取出第 0, 2, 4 行的第 0, 2 列

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 四, CSV 文件读写 + JSON 基础
# ═══════════════════════════════════════════════════
# 量化开发每天要处理 CSV (历史数据, 因子数据, 回测结果...)

# --- 4.1 CSV 读写 ---

# 读取 CSV:
# df_csv = pd.read_csv('data.csv')              # 默认: 第一行是列名
# df_csv = pd.read_csv('data.csv', index_col=0) # 第 0 列作为行索引
# df_csv = pd.read_csv('data.csv', parse_dates=['date'])  # 日期列自动解析

# 写入 CSV:
# df.to_csv('output.csv')              # 默认包含行索引 (会多一列 Unnamed)
# df.to_csv('output.csv', index=False) # 不写行索引

# --- 4.2 JSON 基础 ---
# JSON = JavaScript Object Notation, 是 API 数据交换最常用的格式
# Python 的 json 模块可以轻松处理

import json

# Python dict → JSON 字符串 (序列化)
"data = {'name': '茅台', 'price': 1800.0, 'volume': 10000}"
"json_str = json.dumps(data, ensure_ascii=False)"
"print(json_str)  # '{\"name\": \"茅台\", \"price\": 1800.0, \"volume\": 10000}'"
""
# ensure_ascii=False 才能保留中文!

# JSON 字符串 → Python dict (反序列化)
"parsed = json.loads(json_str)"
"print(parsed['name'])   # '茅台'"
""
# 从文件读 JSON:
# with open('data.json', 'r') as f:
#     data = json.load(f)      # json.load (不是 loads!) -> 从文件读

# 写 JSON 到文件:
# with open('data.json', 'w') as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# JSON 列表 → DataFrame:
"json_list = '[{\"name\": \"茅台\", \"price\": 1800}, {\"name\": \"招行\", \"price\": 35.5}]'"
"df_from_json = pd.read_json(json_list)"
"print(df_from_json)"
"#    name   price"
"# 0   茅台  1800.0"
"# 1   招行    35.5"

# 等价于:
"data_list = json.loads(json_list)  # 先解析为 Python list of dict"
"df_alt = pd.DataFrame(data_list)   # list of dict -> DataFrame"


print("\n" + "=" * 40 + "\n练习 4: CSV + JSON")

# ■ 练习 4.1: CSV 读写
#
# 1. 把 df_stocks 写入 'stocks.csv', 不写行索引
# 2. 用 pd.read_csv 读回来
# 3. 打印读回来的 DataFrame, 确认和原来一样

# ↓ 你的代码 ↓


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


# ═══════════════════════════════════════════════════
# 五, yfinance 引子 — 一行代码拉股票数据
# ═══════════════════════════════════════════════════
# yfinance 是雅虎财经的 Python 客户端.
# 一行代码就能拿到真实股票数据, 返回的就是 DataFrame.

# 安装: pip install yfinance (在终端运行)

# --- 5.1 基本的 yfinance 用法 ---

import yfinance as yf

# 下载单只股票:
"aapl = yf.download('AAPL', start='2024-01-01', end='2024-03-01')"
"print(type(aapl))   # <class 'pandas.core.frame.DataFrame'>"
"print(aapl.head())  # 有 Open/High/Low/Close/Volume 等列"
""
# 参数说明:
#   ticker:   股票代码 (AAPL = Apple, 600519.SS = 茅台上海)
#   start:    开始日期 (字符串 'YYYY-MM-DD')
#   end:      结束日期 (默认到今天)
#   progress: 是否显示进度条 (默认 True, 第一次可以关掉)

# 下载多只股票:
"portfolio = yf.download(['AAPL', 'MSFT', 'GOOGL'], start='2024-01-01')"
"print(portfolio.columns)  # 多级列索引: (Open/Close..., AAPL/MSFT...)"
"print(portfolio['Close'])  # 只看收盘价 (DataFrame)"

# --- 5.2 .info 属性 — 查看股票信息 ---

# 获取单只股票的详细信息:
"aapl_info = yf.Ticker('AAPL').info"
"print(aapl_info['currentPrice'])    # 当前价格"
"print(aapl_info['marketCap'])       # 市值"
"print(aapl_info['trailingPE'])      # 市盈率"
"print(aapl_info['dividendYield'])   # 股息率"
""
# .info 返回一个 dict, 包含几十个字段


print("\n" + "=" * 40 + "\n练习 5: yfinance 入门")

# ■ 练习 5.1: 拉取真实股票数据
#
# 用 yfinance 拉取:
#   1. 茅台 (600519.SS) 2024年全年的数据
#   2. 打印 head() 和 tail()
#   3. 打印 info() 看 describe()

# ↓ 你的代码 ↓


# ■ 练习 5.2: 多股票收盘价
#
# 1. 拉取 ['AAPL', 'MSFT', 'GOOGL'] 2024年1月~3月数据
# 2. 从返回的数据中提取 'Close' 列 (收盘价 DataFrame)
# 3. 计算:
#    - 每只股票的均价
#    - 每只股票的最高价和最低价
#    - 三只股票中, 哪只波动最大 (标准差)

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# ▸ 综合练习: 真实股票数据分析管道
# ═══════════════════════════════════════════════════

print("\n" + "=" * 50)
print("综合练习: 真实股票数据分析管道")
print("=" * 50)

# 综合运用今天的全部知识点
#
# 任务: 分析 2024 年美股科技股的走势
#
# 数据:
#   - 股票: AAPL, MSFT, GOOGL, AMZN
#   - 时间: 2024-01-01 ~ 2024-06-01
#
# 步骤:
# 1. 用 yfinance 下载上述 4 只股票数据
# 2. 提取 'Close' 收盘价 DataFrame
# 3. 用 .head() 和 .describe() 查看数据概览
# 4. 计算每只股票的月均价 (提示: groupby + resample
#    或手动切片, 但 Day 09 还没教 resample, 用切片法)
#    (可选: 按月份分组, 每月算均值 → 4 只股票 x 5 个月)
# 5. 找出每只股票的历史最高收盘价和对应日期
# 6. 计算每只股票的累计收益率:
#    累计收益率 = (最后一天收盘 / 第一天收盘 - 1)
# 7. 用布尔索引找出 AAPL 收盘价 > 200 的天数
# 8. (附加) 把分析结果保存为 CSV
#
# 输出格式参考:
#   === 数据概览 ===
#   AAPL 均价: xxx.xx, 最高: xxx.xx
#   MSFT 均价: xxx.xx, 最高: xxx.xx
#   ...
#   === 月均价 ===
#   2024-01: [AAPL均值, MSFT均值, ...]
#   ...
#   === 累计收益率 ===
#   AAPL: +xx.xx%
#   ...

# ↓ 你的代码 ↓
