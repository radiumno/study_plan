"""
====================================================
 Day 10 | Pandas 进阶 -- 时间序列 + 多表操作
====================================================

 目标: 学会处理时间序列数据, 算均线/波动率, 合并多表

 参考源:
   - Coursera Python for Finance (时间序列/rolling)
   - whale-quant ch03 常见指标 (github.com/datawhalechina/whale-quant)
   - whale-quant ch07 pandas 评估指标
   - Pandas 官方 Cookbook (pandas.pydata.org/docs/user_guide/timeseries.html)

 三线:
   量化主线 (90%): 均线/波动率/时间聚合, 量化分析核心技能
   AI辅线 (5%): groupby/merge 也是 ML 特征工程的基础
   考研 (5%): 时间序列概念与数一统计部分有重叠

====================================================

 进度: 阶段1 Python基础 -- Part 2 数据处理 (Day 08~14)
   Day 08 NumPy 数组运算   ✅
   Day 08R NumPy 强化      ✅
   Day 09 Pandas 入门      ✅
   >>> Day 10 Pandas 进阶  <<<  (当前位置)
   Day 11 Matplotlib 可视化  (下一课)
   Day 12 复习日
   Day 13-14 数据采集+综合
"""

# ═══════════════════════════════════════════════════
# 复习环节 -- Day 09 回顾 + 抽题回练
# ═══════════════════════════════════════════════════
# Day 09 核心: Series/DataFrame 创建, loc/iloc, shift,
# CSV/JSON 读写. Day 08R 核心: 布尔索引, 向量化.

print("\n" + "=" * 50)
print("Day 10 | Pandas 进阶 -- 复习环节")
print("=" * 50)

import numpy as np
import pandas as pd

# --- 练习 R1: Day 09 核心复习 ---

# 从 dict 创建 Series, 找出价格 > 180 的股票
stock_dict = {'AAPL': 185.0, 'MSFT': 420.5, 'GOOGL': 175.0}

# ↓ 你的代码 ↓


# --- 练习 R2: Day 08R 布尔索引回练 ---

# 给定 NumPy 数组, 找出所有 > 0 的元素并替换为 1
arr_r2 = np.array([-0.5, 1.2, 0.0, 2.1, -0.3, 1.5])

# 提示: 布尔索引 + 赋值, 一行搞定

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 知识块1: 时间序列基础
# ═══════════════════════════════════════════════════
# 量化数据最核心的维度就是时间.
# 但 Python 默认不认识 "2024-01-02" 是日期 -- 它就是个字符串.
# 需要用 pd.to_datetime() 把它变成 Pandas 能理解的时间类型.

# --- 1.1 pd.to_datetime() -- 字符串转时间 ---

# 单字符串转换:
"t = pd.to_datetime('2024-01-02')"
"print(t)                      # 2024-01-02 00:00:00"
"print(type(t))                # <class 'pandas._libs.tslibs.Timestamp'>"
""
# 参数说明:
#   arg: 可以是字符串, 字符串列表, 或 Series
#   format: 指定格式 (不传则 Pandas 自动推断, 慢但方便)

# 列表转换:
"dates = pd.to_datetime(['2024-01-02', '2024-01-03', '2024-01-04'])"
"print(dates)                  # DatetimeIndex: 一批时间戳"
"print(type(dates))            # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>"
""
# ⚠️ 常见日期格式都能自动识别: '2024-01-02', '2024/01/02', '01-02-2024'
#    但有歧义时 (01-02-2024 是 1月2日 还是 2月1日?) 建议传 format

# Series 转换:
"df = pd.DataFrame({'date': ['2024-01-02', '2024-01-03'], 'price': [100, 101]})"
"df['date'] = pd.to_datetime(df['date'])  # 把 date 列转为时间类型"
"print(df.dtypes)  # date -> datetime64[ns]"

# --- 1.2 DatetimeIndex -- 日期作为行索引 ---

# 把日期列设为行索引:
"df = df.set_index('date')  # 原来的 'date' 列变成了行索引"
"print(df.index)            # DatetimeIndex(['2024-01-02', '2024-01-03'])"
""
# 为什么要把日期设为索引? 三个原因:
#   1. 时间切片: df['2024-01'] 直接取 1 月所有数据
#   2. rolling/resample 都要求索引是时间类型
#   3. 画图时 x 轴自动标日期

# 也可以读 CSV 时直接指定:
# df = pd.read_csv('data.csv', parse_dates=['date'], index_col='date')
#   parse_dates: 告诉 Pandas 哪些列是日期 (自动转 DatetimeIndex)
#   index_col:   指定哪列作为行索引

# --- 1.3 pd.date_range() -- 生成日期序列 ---

# 生成连续的交易日 (但包含周末):
"dates = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')"
"print(dates)"
"# DatetimeIndex(['2024-01-01', '2024-01-02', ..., '2024-01-10'])"
""
# 参数说明:
#   start: 开始日期 (字符串或 Timestamp)
#   end:   结束日期 (含)
#   periods: 生成 N 个日期 (与 end 二选一)
#   freq:  频率 (默认 'D' 按天)
#     'D'  = 每日 (含周末)
#     'B'  = 仅交易日 (Business day, 周一到周五)
#     'W'  = 每周 (默认周日)
#     'ME' = 月末 (Month End)
#     'QE' = 季度末

"biz_days = pd.date_range(start='2024-01-01', periods=10, freq='B')"
"print(biz_days)  # 跳过周末, 只有周一到周五"

# --- 1.4 时间切片 -- 按时间范围取数据 ---

# 当索引是 DatetimeIndex 时, 可以直接切片:
"dates = pd.date_range('2024-01-01', periods=10, freq='D')"
"df = pd.DataFrame({'price': range(10)}, index=dates)"
""
"print(df['2024-01-03':'2024-01-07'])  # 左闭右闭! (和普通标签切片一样)"
"#             price"
"# 2024-01-03      2"
"# 2024-01-04      3"
"# 2024-01-05      4"
"# 2024-01-06      5"
"# 2024-01-07      6"
""
"print(df['2024-01'])  # 取整个 1 月的数据"
"#             price"
"# 2024-01-01      0"
"# 2024-01-02      1"
"# ..."
""
# ⚠️ 时间切片包含结尾 (左闭右闭), 和普通标签切片一致.


print("\n" + "=" * 40 + "\n知识块1 练习: 时间序列")

# ■ 练习 1.1: 创建 DatetimeIndex
#
# 给定一个价格 list, 用 pd.date_range 生成 2024 年 1 月
# (仅交易日, 不包含周末) 的日期索引, 创建 DataFrame.
# 打印 DataFrame 和 index 的信息.

prices = [100, 102, 101, 105, 103, 107, 106, 110, 108, 112,
          111, 115, 113, 118, 116, 120, 119, 122, 121, 125,
          123, 128, 126, 130, 129, 133, 131, 135, 134, 138]

# 提示:
#   1. 1月有 31 天, 周六周日各 4-5 天, 交易日约 23 天
#   2. 用 pd.date_range(start='2024-01-01', periods=len(prices), freq='B')
#   3. 创建 df = pd.DataFrame({'price': prices}, index=dates)

# ↓ 你的代码 ↓


# ■ 练习 1.2: 时间切片
#
# 从上题创建的 DataFrame 中:
#   1. 取出 2024 年 1 月第三周的数据 (1月15日 ~ 1月19日)
#   2. 计算这周的均价
#   3. 取出 1 月下半月 (1月16日之后) 的数据

# 提示: 时间切片用 df['2024-01-15':'2024-01-19']

# ↓ 你的代码 ↓


# ■ 练习 1.3: 字符串转时间
#
# 以下是从 CSV 读取的数据 (日期是字符串),
# 请把 date 列转为时间类型, 再设为索引.

data_str = {
    'date': ['2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-08'],
    'close': [180.0, 182.5, 181.0, 183.5, 185.0],
    'volume': [10000, 12000, 11000, 13000, 14000]
}
df_raw = pd.DataFrame(data_str)

# 提示:
#   1. pd.to_datetime(df_raw['date']) 转类型
#   2. df_raw['date'] = 转好的结果
#   3. df_raw = df_raw.set_index('date')
# 完成后打印 df_raw 和 df_raw.index

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 二, 滚动窗口 -- 算均线和波动率
# ═══════════════════════════════════════════════════
# 移动平均线 (Moving Average) 是量化分析最基础的指标.
# SMA_n = n 日收盘价的平均值, 每天滚动计算.
# 不用 for 循环, Pandas 的 .rolling() 一行搞定.

# --- 2.1 rolling() -- 滑动窗口 ---

# 基本用法:
"dates = pd.date_range('2024-01-01', periods=10, freq='D')"
"df = pd.DataFrame({'price': [100, 102, 101, 105, 103, 107, 106, 110, 108, 112]}, index=dates)"
""
"# 3 日均线: 每个窗口取 3 天, 算均值"
"df['SMA_3'] = df['price'].rolling(window=3).mean()"
"print(df)"
"#            price     SMA_3"
"# 2024-01-01    100      NaN    <- 窗口 < 3, 不够算"
"# 2024-01-02    102      NaN"
"# 2024-01-03    101  101.00    <- (100+102+101)/3"
"# 2024-01-04    105  102.67    <- (102+101+105)/3"
"# ..."
""
# 参数说明:
#   window: 窗口大小 (天数/行数)
#   min_periods: 最少需要多少行才计算 (默认=window)
#     rolling(3, min_periods=1) -> 即使前 2 行也勉强算
#   center: 窗口居中 (默认 False, 用窗口末尾对齐)

# rolling 后可以跟的各种聚合:
"df['SMA_3']    = df['price'].rolling(3).mean()   # 均线"
"df['max_3']    = df['price'].rolling(3).max()     # 3 日最高"
"df['min_3']    = df['price'].rolling(3).min()     # 3 日最低"
"df['std_3']    = df['price'].rolling(3).std()     # 3 日标准差 (波动率)"

# --- 2.2 波动率 (年化) ---

# 日收益率:
"df['daily_ret'] = df['price'].pct_change()  # 每日涨跌幅"
"# pct_change() = 本日/昨日 - 1, 等同于 df['price']/df['price'].shift(1) - 1"

# 波动率 = 标准差 * sqrt(天数)
#   日波动率: rolling(20).std()
#   年化波动率: 日波动率 * sqrt(252)
#   为什么 252? 一年大约 252 个交易日.
"rolling_vol = df['daily_ret'].rolling(20).std() * np.sqrt(252)"
"print(rolling_vol)  # 年化波动率, 单位: decimal (0.2 = 20%)"
""
# ⚠️ rolling(20) 常用作"月度波动率" (约 20 个交易日/月)
#    rolling(60) -> 季度波动率
#    rolling(252) -> 年度波动率

# --- 2.3 均线的量化应用: 金叉/死叉 ---

# 金叉 (Golden Cross): 短期均线上穿长期均线 -> 买入信号
# 死叉 (Death Cross):  短期均线下穿长期均线 -> 卖出信号
""
"df['SMA_5']  = df['price'].rolling(5).mean()"
"df['SMA_20'] = df['price'].rolling(20).mean()"
"# 金叉判断 (不需要 for 循环):"
"df['signal'] = 0            # 0 = 无信号"
"df.loc[df['SMA_5'] > df['SMA_20'], 'signal'] = 1   # 短期 > 长期 -> 持仓"
"df.loc[df['SMA_5'] < df['SMA_20'], 'signal'] = -1  # 短期 < 长期 -> 空仓"
""
# ⚠️ 这个信号是"状态"不是"穿越".
#   穿越 (= 前一天没有持仓, 今天开始持仓) 需要 shift:
#   buy_signal = (df['SMA_5'] > df['SMA_20']) & (df['SMA_5'].shift(1) <= df['SMA_20'].shift(1))


# ▸ 知识块1 总练习: 时间序列全流程
#
# 给定起始日期和价格数组, 完成:
#   1. 创建 DatetimeIndex (仅交易日)
#   2. 计算 5 日均线和 20 日年化波动率
#   3. 用时间切片取出 1 月下半月数据
#   4. 找出价格最高的交易周
# 提示: 把上面 3 个知识点串起来


print("\n" + "=" * 40 + "\n知识块2 练习: 滚动窗口 -- 均线和波动率")

# ■ 练习 2.1: 算均线
#
# 给定收盘价数据, 计算 5 日均线 (SMA_5) 和 20 日均线 (SMA_20).
# 打印 DataFrame 的最后 10 行, 观察均线趋势.

np.random.seed(42)
dates_2 = pd.date_range('2024-01-01', periods=100, freq='D')
price_2 = 100 + np.cumsum(np.random.randn(100) * 0.5)  # 随机游走
df_2 = pd.DataFrame({'close': price_2}, index=dates_2)

# ↓ 你的代码 ↓


# ■ 练习 2.2: 波动率
#
# 从 df_2 计算:
#   1. 日收益率 (用 pct_change)
#   2. 20 日滚动年化波动率
#   3. 找波动率最高的那一天 (用 idxmax)
#   4. 打印波动率 > 0.3 (30%) 的那些行

# 提示:
#   daily_ret = df_2['close'].pct_change()
#   vol = daily_ret.rolling(20).std() * np.sqrt(252)

# ↓ 你的代码 ↓


# ■ 练习 2.3: 金叉/死叉信号
#
# 给 df_2 生成 SMA_5 和 SMA_20 均线,
# 然后生成交易信号:
#   1. signal = 0 (默认)
#   2. SMA_5 > SMA_20 -> signal = 1 (持仓)
#   3. SMA_5 < SMA_20 -> signal = -1 (空仓)
#
# 最后统计: signal=1 的天数占比

# ↓ 你的代码 ↓


# ▸ 知识块2 总练习: 完整均线策略信号
#
# 给定收盘价数据, 一次性完成:
#   1. 5日均线 + 20日均线
#   2. 日收益率 + 20日年化波动率
#   3. 生成买卖信号 (SMA_5 > SMA_20 = 持仓, 否则空仓)
#   4. 统计持仓天数占比


# ═══════════════════════════════════════════════════
# 三, 重采样 -- 日频转周频/月频
# ═══════════════════════════════════════════════════
# 量化分析不同场景需要不同频率:
#   日线: 日常监控, 日内交易
#   周线/月线: 中期趋势判断, 因子计算
#   .resample() 就是做频率转换的.

# --- 3.1 基本 resample ---

"dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')"
"df = pd.DataFrame({'price': np.cumsum(np.random.randn(len(dates))) + 100}, index=dates)"
""
"# 日 -> 月: 每月均值"
"monthly = df.resample('ME').mean()    # ME = Month End"
"print(monthly)"
""
"# 日 -> 周: 每周收盘价 (最后一天的价)"
"weekly = df.resample('W').last()      # W = Week, last = 取周五收盘"
"# .last() 取窗口内最后一个值 (一般是周五)"
"# .first() 取第一个值 (周一开盘)"
"# .mean() 取平均值"
"# .ohlc() 取 Open/High/Low/Close"
""
"# 日 -> 季度: 每季末"
"quarterly = df.resample('QE').last()  # QE = Quarter End"

# 参数说明:
#   ME: Month End (月末)
#   MS: Month Start (月初)
#   W:  Weekly (周日结束, 用 W-MON 指定周一结束)
#   W-FRI: 周五结束的周
#   QE: Quarter End (季末)
#   YE: Year End (年末)

# --- 3.2 多聚合: 用 .agg() ---

# resample 后可以同时算多个值:
"monthly_agg = df.resample('ME').agg({"
"    'price': ['last', 'mean', 'max', 'min']"
"})"
"print(monthly_agg)"
"#             price"
"#             last    mean     max     min"
"# 2024-01-31  xxx    xxx     xxx     xxx"
"# 2024-02-29  xxx    xxx     xxx     xxx"
""

# --- 3.3 OHLC 重采样 (常见: 日线→周线) ---

# 股票交易软件经常把日线数据压缩成周线:
#   Open  = 周一开盘 (窗口内第一个)
#   High  = 窗口内最高
#   Low   = 窗口内最低
#   Close = 周五收盘 (窗口内最后一个)
"weekly_ohlc = df.resample('W').ohlc()  # ohlc() 一次搞定 4 列"
"print(weekly_ohlc.head())"

# ⚠️ 注意: ohlc() 只能用在单列 DataFrame 或 Series 上.
#   如果有多列, 需要分开算再用 agg.


print("\n" + "=" * 40 + "\n知识块3 练习: 重采样 + 分组 + 合并")

# ■ 练习 3.1: 日转周
#
# 用 df_2 (100 天的随机游走数据):
#   1. 重采样为周频, 取每周收盘价 (.last())
#   2. 重采样为月频, 取每月均价 (.mean())
#   3. 打印两种结果, 对比数据量

# 提示: df_2.resample('W').last()

# ↓ 你的代码 ↓


# ■ 练习 3.2: OHLC 周线
#
# 从 df_2 生成周线 OHLC (4 列: Open/High/Low/Close).
# 然后找这一列数据哪一周涨幅最大 (Close - Open).

# 提示:
#   weekly = df_2['close'].resample('W').ohlc()
#   weekly['涨跌幅'] = weekly['close'] - weekly['open']

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 四, GroupBy -- 分组聚合
# ═══════════════════════════════════════════════════
# GroupBy = 按某个列分组, 再对各组分别计算.
# 量化场景: 按股票分组、按行业分组、按月分组.

# --- 4.1 基本 GroupBy ---

# 简单的分组例子:
"df_group = pd.DataFrame({"
"    'stock': ['AAPL', 'MSFT', 'AAPL', 'MSFT', 'AAPL', 'MSFT'],"
"    'date':  ['周一', '周一', '周二', '周二', '周三', '周三'],"
"    'ret':   [0.01, 0.02, -0.01, 0.01, 0.02, -0.01]"
"})"
"print(df_group)"
""
"# 按股票分组, 算每只股票的收益率均值:"
"print(df_group.groupby('stock')['ret'].mean())"
"# stock"
"# AAPL    0.0067"
"# MSFT    0.0067"
""
"# 按日期分组, 算每天所有股票的平均收益率:"
"print(df_group.groupby('date')['ret'].mean())"

# 关键理解:
#   groupby('stock') 把数据按 'stock' 列分成若干组
#   然后 ['ret'] 提取每组的 ret 列
#   最后 .mean() 对每组分别算均值

# --- 4.2 多列分组 + agg ---

# 按 'stock' 和 'date' 两列分组:
"print(df_group.groupby(['stock', 'date'])['ret'].mean())"
"# stock  date"
"# AAPL  周一    0.01"
"#       周三    0.02"
"#       周二   -0.01"
"# MSFT  周一    0.02"
"#       周三   -0.01"
"#       周二    0.01"
""
"# 多聚合: 同时算均值、标准差、计数"
"print(df_group.groupby('stock')['ret'].agg(['mean', 'std', 'count']))"

# --- 4.3 量化场景: 月收益率分组 ---

# 先用 resample 按月份, 再用 groupby? 不对.
# 更常见的场景: 有多只股票的全量数据, 想算每只股票的月均收益率.
# 这时候需要: 先新增一列 "year_month", 再 groupby

# 生成示例: 2 只股票, 3 个月的数据
"dates_m = pd.date_range('2024-01-01', '2024-03-31', freq='D')"
"df_multi = pd.DataFrame({"
"    'date': np.concatenate([dates_m, dates_m]),  # AAPL 和 MSFT 各一份"
"    'stock': ['AAPL']*len(dates_m) + ['MSFT']*len(dates_m),"
"    'close': np.random.randn(len(dates_m)*2).cumsum() + 100"
"})"
""
"# 新增 'ym' 列: 提取年月"
"df_multi['ym'] = df_multi['date'].dt.to_period('M')  # .dt 访问时间属性"
"# .dt 是 Pandas 访问时间属性的入口: .dt.year, .dt.month, .dt.day, .dt.weekday"
"# .dt.to_period('M') 提取年月, 变成 Period 类型 ('2024-01', '2024-02'...)"
""
"# 按 stock 和 ym 分组, 算每月每只股票的均价:"
"monthly_avg = df_multi.groupby(['stock', 'ym'])['close'].mean()"
"print(monthly_avg)"


print("\n" + "=" * 40 + "\n知识块4 练习: GroupBy 分组聚合")

# ■ 练习 4.1: 按股票分组
#
# 以下数据包含了 3 只股票连续几天的收益率.
# 按 stock 分组, 找出每只股票的:
#   1. 平均收益率
#   2. 收益率标准差
#   3. 正收益天数占比 (ret > 0 的天数 / 总天数)

data_ret = pd.DataFrame({
    'stock': ['AAPL', 'AAPL', 'AAPL', 'AAPL', 'AAPL',
              'MSFT', 'MSFT', 'MSFT', 'MSFT', 'MSFT',
              'GOOGL', 'GOOGL', 'GOOGL', 'GOOGL', 'GOOGL'],
    'ret':   [0.01, -0.02, 0.03, 0.01, -0.01,
              0.02, 0.01, -0.01, 0.03, 0.02,
              -0.01, 0.00, 0.02, -0.02, 0.01]
})

# 提示:
#   grouped = data_ret.groupby('stock')['ret']
#   mean_ret = grouped.mean()
#   std_ret = grouped.std()
#   正收益占比: grouped.apply(lambda x: (x > 0).mean())

# ↓ 你的代码 ↓


# ■ 练习 4.2: 按月分组统计
#
# 给 df_multi 的代码补全 (或在上面基础上继续):
#   1. 新增一列 'month' 提取月份数字 (df['date'].dt.month)
#   2. 按 month 分组, 算每个月所有股票的均价
#   3. 找出收益率最好的月份

# 提示: df_multi['month'] = df_multi['date'].dt.month

# ↓ 你的代码 ↓


# ▸ 知识块4 总练习: 多股票分组统计
#
# 给定3只股票各5天的收益率数据:
#   1. 用 groupby 按股票分组, 算每只股票的均值/标准差/正收益天数占比
#   2. 找出哪只股票表现最好 (均值最高)
#   3. 找出哪只股票波动最大 (标准差最大)
data_block4 = pd.DataFrame({
    'stock': ['A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
    'ret': [0.01,-0.02,0.03,0.01,-0.01, 0.02,0.01,-0.01,0.03,0.02, -0.01,0.0,0.02,-0.02,0.01]
})


# ═══════════════════════════════════════════════════
# 知识块5: 合并多表 -- Concat + Merge
# ═══════════════════════════════════════════════════
# 真实量化开发: 多只股票数据各自存一个 DataFrame,
# 需要把它们并在一起分析. 两种合并方式:
#   pd.concat()  -- 纵向堆叠 (增加行) 或 横向拼接 (增加列)
#   pd.merge()   -- SQL 式 join, 按 key 匹配

# --- 5.1 pd.concat() -- 纵向堆叠 ---

# 纵向: 把 AAPL 和 MSFT 的数据按行拼在一起
"aapl_data = pd.DataFrame({"
"    'date': ['2024-01-02', '2024-01-03'],"
"    'close': [180, 182],"
"    'volume': [10000, 12000]"
"})"
"msft_data = pd.DataFrame({"
"    'date': ['2024-01-02', '2024-01-03'],"
"    'close': [380, 385],"
"    'volume': [15000, 14000]"
"})"
""
"# 纵向拼接 (行数增加)"
"combined = pd.concat([aapl_data, msft_data], axis=0, ignore_index=True)"
"print(combined)"
"#          date  close  volume"
"# 0  2024-01-02    180   10000"
"# 1  2024-01-03    182   12000"
"# 2  2024-01-02    380   15000"
"# 3  2024-01-03    385   14000"
""
"# 参数说明:"
"#   axis=0:  纵向 (行方向), 默认"
"#   axis=1:  横向 (列方向)"
"#   ignore_index=True: 重置行索引 (0,1,2...)"

# 横向拼接 (列数增加):
"combined_col = pd.concat([aapl_data, msft_data], axis=1, keys=['AAPL', 'MSFT'])"
"print(combined_col)"
"#    AAPL                 MSFT"
"#    date close volume    date close volume"
"# 0  2024-01-02  180  10000  2024-01-02  380  15000"
"# 1  2024-01-03  182  12000  2024-01-03  385  14000"
"# 用 keys 参数指定上层列名, 就产生了 MultiIndex"

# --- 5.2 pd.merge() -- SQL 式 join ---

# 按某个 key 列匹配, 把两张表拼在一起.
# 类似 Excel 的 VLOOKUP.

"prices = pd.DataFrame({"
"    'date': ['2024-01-02', '2024-01-03', '2024-01-04'],"
"    'close': [180, 182, 181]"
"})"
"info = pd.DataFrame({"
"    'date': ['2024-01-02', '2024-01-03', '2024-01-04'],"
"    'volume': [10000, 12000, 11000],"
"    'sector': ['Tech', 'Tech', 'Tech']"
"})"
""
"# 按 date 列匹配, 横向合并"
"merged = pd.merge(prices, info, on='date')"
"print(merged)"
"#          date  close  volume sector"
"# 0  2024-01-02    180   10000   Tech"
"# 1  2024-01-03    182   12000   Tech"
"# 2  2024-01-04    181   11000   Tech"
""
"# 参数说明:"
"#   on:     按哪列匹配 (两边列名相同)"
"#   left_on / right_on: 两边列名不同时分别指定"
"#   how:    匹配方式 (默认 inner)"
"#     'inner': 只保留两边都有的 key (交集)"
"#     'left':  保留左表全部, 右表没有的填 NaN"
"#     'right': 保留右表全部"
"#     'outer': 保留全部 (并集)"

# 不同 how 的效果:
"# 左表: key=[1,2,3]   右表: key=[2,3,4]"
"# inner -> key=[2,3]   (两边都有)"
"# left  -> key=[1,2,3] (左表全保留, 右表没有 1)"
"# outer -> key=[1,2,3,4] (全部保留)"


print("\n" + "=" * 40 + "\n知识块5 练习: 合并多表")

# ■ 练习 5.1: 纵向合并多只股票
#
# 已有 3 只股票的独立 DataFrame, 把它们纵向合并成一个.
# 每只股票的数据都有 'date', 'close', 'volume' 三列.
# 合并后新增一列 'stock' 标注是哪个股票.

aapl = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-02', '2024-01-03', '2024-01-04']),
    'close': [180, 182, 181],
    'volume': [10000, 12000, 11000]
})
msft = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-02', '2024-01-03', '2024-01-04']),
    'close': [380, 385, 383],
    'volume': [15000, 14000, 16000]
})
googl = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-02', '2024-01-03', '2024-01-04']),
    'close': [140, 142, 141],
    'volume': [8000, 9000, 8500]
})

# 提示:
#   1. 先给每个 df 加 'stock' 列
#   2. pd.concat([...], ignore_index=True)

# ↓ 你的代码 ↓


# ■ 练习 5.2: Merge 合并价量数据
#
# 你有两只股票的价格数据和成交量数据分别存着,
# 按日期合并, 计算每天每只股票的成交额 (price * volume).

price_data = pd.DataFrame({
    'date': ['2024-01-02', '2024-01-03', '2024-01-04'],
    'AAPL': [180, 182, 181],
    'MSFT': [380, 385, 383]
})
volume_data = pd.DataFrame({
    'date': ['2024-01-02', '2024-01-03', '2024-01-04'],
    'AAPL': [10000, 12000, 11000],
    'MSFT': [15000, 14000, 16000]
})

# 提示:
#   1. 先把 price_data 和 volume_data 按 'date' merge
#   2. 然后算 AAPL 成交额 = 价 * 量
#   3. 再算 MSFT 成交额

# ↓ 你的代码 ↓


# ▸ 知识块5 总练习: 价量合并分析
#
# 给定 price 和 volume 两个 DataFrame,
# 按 date merge 后计算每只股票的每日成交额,
# 然后按 stock 分组求月均成交额.
price_b5 = pd.DataFrame({'date': ['2024-01-02','2024-01-03','2024-01-04'], 'AAPL': [180,182,181], 'MSFT': [380,385,383]})
vol_b5 = pd.DataFrame({'date': ['2024-01-02','2024-01-03','2024-01-04'], 'AAPL': [10000,12000,11000], 'MSFT': [15000,14000,16000]})

# 提示: merge → 算成交额 → groupby


# ═══════════════════════════════════════════════════
# ▸ Day 综合练习: 股票均线策略分析 (离线可用)
# ═══════════════════════════════════════════════════

print("\n" + "=" * 50)
print("综合练习: 股票均线策略分析")
print("=" * 50)

# 国内 yfinance 用不了, 所以直接用累乘生成"看起来像"真实股价的数据.
# AAPL 2024 年从 ~180 起步, 年化波动约 25%, 日波动率约 1.6%.
# 用了固定种子, 每次运行结果一样.

np.random.seed(2024)
dates_stock = pd.date_range('2024-01-02', '2024-12-31', freq='B')
n_days = len(dates_stock)

# 生成"真实感"价格: 基准价格 180 + 随机游走 + 一点向上趋势
daily_vol = 0.016  # 日波动率 ~1.6%
trend = 0.0004     # 每日微涨趋势 (~10%/年)
returns = np.random.randn(n_days) * daily_vol + trend
price_start = 180.0
prices_stock = price_start * np.cumprod(1 + returns)

spy = pd.DataFrame({
    'close': prices_stock,
    'volume': np.random.randint(30000000, 80000000, n_days)
}, index=dates_stock)

# 可以用 spy 替代 yfinance 做全部练习.
# 想看数据长什么样:
print(spy.head())
print(f"数据范围: {spy.index[0].date()} ~ {spy.index[-1].date()}")
print(f"价格区间: {spy['close'].min():.2f} ~ {spy['close'].max():.2f}")

# 综合运用今日全部知识点, 分析 spy 的均线策略
#
# 步骤:
#
# 1. 计算:
#    a) SMA_5 (5日均线)
#    b) SMA_20 (20日均线)
#    c) 20日年化波动率
#
# 2. 生成交易信号:
#    - 金叉买入: SMA_5 上穿 SMA_20 (当天 SMA_5 > SMA_20, 前一天 SMA_5 <= SMA_20)
#    - 死叉卖出: SMA_5 下穿 SMA_20 (当天 SMA_5 < SMA_20, 前一天 SMA_5 >= SMA_20)
#    - 持仓状态: signal = 1 (持仓, SMA_5 > SMA_20) / -1 (空仓, SMA_5 < SMA_20)
#
# 3. (核心) 计算策略的累计收益率:
#    - 日收益率: daily_ret = spy['close'].pct_change()
#    - 每天策略收益 = signal.shift(1) * daily_ret
#      (shift(1) 是因为今天收盘出信号, 明天开盘才执行)
#    - 策略净值 = (1 + 策略收益).cumprod()
#    - 基准净值 = (1 + daily_ret).cumprod()
#
# 4. (选做) 用 groupby 按月统计收益率
#    - 提取 month, 按月分组看收益分布
#
# 5. 打印分析报告:
#    === 均线策略分析报告 ===
#    总交易日: xxx
#    金叉次数: xx
#    死叉次数: xx
#    Buy-and-Hold 累计收益: +xx.xx%
#    策略累计收益: +xx.xx%
#    最大单日涨幅: +x.xx%
#    最大单日跌幅: -x.xx%

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# ▸ 附: Baostock 真实 A 股数据 (国内直连)
# ═══════════════════════════════════════════════════
#
# Baostock 免费直连, 无需注册, 极其稳定.

"import baostock as bs"
""
"bs.login()"
"rs = bs.query_history_k_data_plus("
"    'sz.000001',"
"    'date,open,close,high,low,volume',"
"    start_date='2024-01-01', end_date='2024-12-31'"
")"
"df_bs = rs.get_data()"
"bs.logout()"
""
"# 转类型 + 日期索引"
"for col in ['open', 'close', 'high', 'low', 'volume']:"
"    df_bs[col] = df_bs[col].astype(float)"
"df_bs.index = pd.to_datetime(df_bs['date'])"
""
"# 均线和波动率 (和上面练习完全一样)"
"df_bs['SMA_5'] = df_bs['close'].rolling(5).mean()"
"df_bs['SMA_20'] = df_bs['close'].rolling(20).mean()"
"df_bs['daily_ret'] = df_bs['close'].pct_change()"
"df_bs['vol_20'] = df_bs['daily_ret'].rolling(20).std() * np.sqrt(252)"
""
"print(df_bs[['close', 'SMA_5', 'SMA_20']].tail())"
"print(f'平安银行2024年化波动率: {df_bs[\"vol_20\"].mean():.1%}')"
""
# ⚠️ A 股有涨跌停 (±10%), 日波动率比美股小很多.
