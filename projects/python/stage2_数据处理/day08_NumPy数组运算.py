"""
====================================================
 Day 8 | NumPy 数组运算 -- 量化数据处理第一步
====================================================

 目标: 告别 Python 原生循环, 用 NumPy 向量化处理股票数据

 副线: 正则表达式(re模块) — 数据清洗必备工具

 参考源:
   - NumPy 官方 Quickstart (numpy.org/doc/stable/user/quickstart.html)
   - 尚硅谷 Python 数据分析 (b23.tv/BV1D9GLzyEL6)
   - whale-quant ch07 净值曲线与回测 (github.com/datawhalechina/whale-quant)
   - Real Python NumPy 教程 (realpython.com/numpy-array-programming)

 无 C++ 对比

 结构: 前情回顾 -> 讲一个知识点 -> 练一个 -> 再讲 -> 综合

====================================================
"""

# ═══════════════════════════════════════════════════
# 阶段1: Python 基础 (5)
# Part 2: 数据处理 (Days 08-13, 2周)  ★ 今天开始!
#
# Day 01 ✅ 变量, 类型, 字符串, I/O
# Day 02 ✅ 列表, 字典, 元组, 推导式
# Day 03 ✅ 函数, 作用域, lambda
# Day 04 ✅ set, 文件 I/O, 异常处理, CSV 读写
# Day 05 ✅ 模块与包, pip, datetime, 路径操作
# Day 06 ✅ 综合项目: 股票数据管理器
# Day 07 ✅ 复习: Python 核心查漏补缺
# Day 08 ▶ NumPy 数组运算 (今天!)
#
# Part 2 路线图:
# Day 08 NumPy 数组运算
# Day 09 Pandas 入门
# Day 10 Pandas 进阶
# Day 11 Matplotlib 可视化
# Day 12 数据采集与清洗
# Day 13 综合练习
# ═══════════════════════════════════════════════════

# ═══════════════════════════════════════════════════
# Day 8 依赖清单
# ═══════════════════════════════════════════════════
#
# | 依赖项 | 类型 | 首次出现 | 确认覆盖 |
# |--------|------|----------|----------|
# | list | 基础类型 | Day 02 | 列表创建,索引,切片 |
# | str/int/float | 基础类型 | Day 01 | 数值运算,类型转换 |
# | import | 语法 | Day 05 | import numpy as np, import re |
# | if/for | 控制流 | Day 01-03 | 条件判断,循环遍历 |
# | 比较运算 | 运算符 | Day 01 | >, <, ==, >=, <= |
# | bool | 基础类型 | Day 01 | True/False 布尔值 |
# | 索引/切片 | 语法 | Day 02 | list[start:stop:step] |
#
# 本 day 首次教: numpy 包, 向量化思想, re 模块(正则表达式)

# ═══════════════════════════════════════════════════
# 前情回顾 — 列表切片 (Day 02)
# ═══════════════════════════════════════════════════
# NumPy 的切片语法和 list 一脉相承, 快速过一遍.

"prices = [12.5, 12.8, 13.0, 12.9, 13.2]"
"print(prices[0])     # 12.5   (正索引)"
"print(prices[-1])    # 13.2   (负索引: 最后一个)"
"print(prices[1:4])   # [12.8, 13.0, 12.9]  (切片: 左闭右开)"
"print(prices[::-1])  # [13.2, 12.9, 13.0, 12.8, 12.5]  (倒序)"
""
# 规则: list[start:stop:step], 和 NumPy 完全一样.


print("\n" + "=" * 40 + "\n前情回顾: 列表切片热身")

# 用切片从 weekly_data 里提取:
#   1. 前 3 天的价格
#   2. 后 2 天的价格
#   3. 偶数天的价格 (步长 2)

weekly_data = [10.5, 11.0, 10.8, 11.2, 10.9]

# ↓ 你的代码 ↓
print(weekly_data[0:3])
print(weekly_data[-1:-3:-1])
print(weekly_data[::2])



# ═══════════════════════════════════════════════════
# 一, NumPy 与 ndarray --- 为什么量化开发离不开它
# ═══════════════════════════════════════════════════
# NumPy (Numerical Python) 是 Python 科学计算的基石.
# 和 Python 原生 list 相比:
#   - 速度: 快 10~100 倍 (底层 C 实现, 向量化运算)
#   - 内存: 省 (连续内存, 固定类型)
#   - 功能: 广播, 矩阵运算, 随机数, 线性代数...
#
# 量化场景: 你手上 100 万行股票数据, 算每只股票的
# 日收益率. 用 for 循环要几秒, 用 NumPy 只要几毫秒.

import numpy as np

# 颜色输出 (ANSI转义码, macOS终端支持)
GREEN  = '\033[92m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
RED    = '\033[91m'
CYAN   = '\033[96m'
RESET  = '\033[0m'

# --- 1.1 创建 ndarray ---

# 最直接: 从 list 转
"prices = [12.5, 12.8, 12.4, 12.75, 13.0]"
"arr = np.array(prices)"
"print(arr)        # [12.5  12.8  12.4  12.75 13. ]"
"print(type(arr))  # <class 'numpy.ndarray'>"
""
# arr 是一个 ndarray (N 维数组) 对象.
# np.array(数据源) -> 参数可以是 list, tuple, 嵌套 list

# 查看数组属性:
"print(arr.shape)  # (5,)       -> 形状: 5 个元素的一维数组"
"print(arr.ndim)   # 1          -> 维度数"
"print(arr.dtype)  # float64    -> 元素类型(64位浮点)"
"print(len(arr))   # 5          -> 长度(一维)"
""
# shape 是元组 (行数, 列数). 一维数组 shape=(n,)
# dtype 自动推断: int -> int64, float -> float64

# 多维数组:
"matrix = np.array([[1, 2, 3], [4, 5, 6]])"
"print(matrix)"
"# [[1 2 3]"
"#  [4 5 6]]"
"print(matrix.shape)  # (2, 3)   -> 2 行 3 列"
"print(matrix.dtype)  # int64"


print("\n" + "=" * 40 + "\n练习 1.1: 创建数组")

# ■ 练习 1.1: 从股票价格列表创建一维数组
#
# 给定以下股票收盘价列表, 转成 ndarray 并打印 shape 和 dtype.
# 然后查看它的形状, 元素个数, 和数据类型.

closes = [12.5, 12.8, 12.4, 12.75, 13.0, 12.9]

# 提示: 转成数组后看看它的 shape 和 dtype

# ↓ 你的代码 ↓
ndarry = np.array(closes)
print(ndarry.shape)
print(ndarry.dtype)
print(ndarry.ndim)
print(len(ndarry))


# --- 1.2 常用创建函数 ---

# np.zeros(shape)     全 0 数组
"zeros = np.zeros(5)           # [0. 0. 0. 0. 0.]  (默认 float64)"
"zeros_2d = np.zeros((3, 4))   # 3 行 4 列, 全 0"
""
# shape 参数 -> int 或 tuple. 一维传 int, 多维传 (行, 列)

# np.ones(shape)      全 1 数组
"ones = np.ones((2, 3))        # [[1. 1. 1.], [1. 1. 1.]]"

# np.arange(start, stop, step)  类似 range() 但返回数组
"arr = np.arange(10)           # [0 1 2 3 4 5 6 7 8 9]"
"arr2 = np.arange(5, 15, 2)   # [ 5  7  9 11 13]"
""
# 参数: start(默认0), stop(不含), step(默认1)
# 和 Python 的 range() 完全一样, 但返回 ndarray 而非 range 对象

# np.linspace(start, stop, num)  等间隔取 num 个点
"arr = np.linspace(0, 1, 5)   # [0.   0.25 0.5  0.75 1.  ]"
""
# 和 arange 的区别: linspace 指定"个数", arange 指定"步长"
# linspace(0, 1, 5) 在 0~1 之间均匀取 5 个数, 包含两端

# np.random 模块 -- 量化中生成随机数/模拟数据
# np.random.randn(n)   标准正态分布 (均值 0, 标准差 1)
"normal = np.random.randn(5)    # 5 个标准正态随机数"
""
# np.random.randint(low, high, size)  随机整数
"ints = np.random.randint(0, 100, 10)  # 0~99 的 10 个随机整数"
""
# size 参数 -> int 或 tuple. (3, 4) 生成 3x4 的随机矩阵


print("\n" + "=" * 40 + "\n练习 1.2: 用 arange / zeros / random 创建")

# ■ 练习 1.2: 创建交易日期索引和模拟数据
#
# 1. 用 np.arange() 创建 1~20 (不含 21) 的整数数组 -> trading_days
# 2. 用 np.zeros() 创建长度为 20 的全 0 数组 -> prices
# 3. 用 np.random.randn() 生成 20 个标准正态分布随机数 -> daily_returns
# 4. 打印 3 个数组的 shape

# ↓ 你的代码 ↓
trading_days = np.arange(1,21)
prices = np.zeros(20)
daily_returns = np.random.randn(20)
print(trading_days.shape)
print(prices.shape)
print(daily_returns.shape)


print("\n" + "=" * 40 + "\n▸ Part 1 综合: 二维数组")

# ■ Part 1 综合: 创建 5 日 3 只股票的行情矩阵
#
# 用 np.array() 创建一个 5x3 的二维数组:
#   5 行 (交易日) x 3 列 (股票)
# 数据: 5 天收盘价 (3 只股票)
#   [茅台, 招商, 宁德]
#   [12.5, 8.2, 225.0],
#   [12.8, 8.3, 226.5],
#   [12.4, 8.1, 224.0],
#   [12.7, 8.4, 227.0],
#   [13.0, 8.5, 228.0]
#
# 打印: 数组, shape, ndim, dtype

# ↓ 你的代码 ↓
list_1=[12.5, 8.2, 225.0],[12.8, 8.3, 226.5],[12.4, 8.1, 224.0], [12.7, 8.4, 227.0],  [13.0, 8.5, 228.0]
arr_1=np.array(list_1)
print(arr_1)
print(arr_1.shape)
print(arr_1.ndim)
print(arr_1.dtype)

# ═══════════════════════════════════════════════════
# 二, 数组运算 (向量化) -- 告别 for 循环
# ═══════════════════════════════════════════════════
# NumPy 最强大的特性: 对数组整体做运算, 不需要写循环.
# 这种"对整批数据同时做运算"的方式叫 向量化.
#
# 量化的核心: 计算千万级数据, 向量化比 for 循环快 50~100 倍.

# --- 2.1 算术运算 (element-wise, 元素对元素) ---

"a = np.array([10, 20, 30, 40])"
"b = np.array([1, 2, 3, 4])"
""
"print(a + b)   # [11 22 33 44]"
"print(a - b)   # [ 9 18 27 36]"
"print(a * b)   # [10 40 90 160]  (对应元素相乘, 不是矩阵乘)"
"print(a / b)   # [10. 10. 10. 10.]"
"print(a ** 2)  # [ 100  400  900 1600]  (每个元素平方)"
""
# 数组 + 标量: 广播 (标量自动扩展到每个元素)
"print(a + 5)   # [15 25 35 45]"

# 量化场景:计算日收益率
"close = np.array([100, 102, 101, 105, 108])"
"daily_return = close[1:] / close[:-1] - 1  # 向量化, 一行搞定"
"# 等价于: [102/100-1, 101/102-1, 105/101-1, 108/105-1]"


print("\n" + "=" * 40 + "\n练习 2.1: 向量化计算")

# ■ 练习 2.1: 用向量化计算日收益率
#
# 给定收盘价数组, 用向量化方式计算日收益率.
# 日收益率公式: (当日收盘 - 前日收盘) / 前日收盘
# 或用更简洁的: 当日收盘 / 前日收盘 - 1

close_prices = np.array([100.0, 102.5, 101.0, 105.5, 108.0, 107.0])

# 提示: 切片错位相除, 一行搞定

# ↓ 你的代码 ↓
rate = close_prices[1:]/close_prices[0:-1]-1
print(rate)


# --- 2.2 比较运算 (返回布尔数组) ---

"prices = np.array([12.5, 12.8, 12.4, 12.75, 13.0])"
"print(prices > 12.6)   # [False  True False  True  True]"
"print(prices >= 13.0)  # [False False False False  True]"
""
# 比较结果可以当索引用 (布尔索引, 后面讲)

# --- 2.3 聚合函数 (把数组缩减为单个值) ---

"arr = np.array([[1, 2, 3], [4, 5, 6]])"
"print(np.sum(arr))      # 21        (全部元素求和)"
"print(np.mean(arr))     # 3.5       (全部元素平均值)"
"print(np.max(arr))      # 6"
"print(np.min(arr))      # 1"
"print(np.std(arr))      # 1.7078    (标准差)"
""
# 指定 axis 参数: axis=0 按列, axis=1 按行
"print(np.sum(arr, axis=0))  # [5 7 9]   (每列之和)"
"print(np.sum(arr, axis=1))  # [6 15]    (每行之和)"
""
# axis 参数含义:
#   axis=0 -> 沿着行方向"压扁", 得到每列的聚合
#   axis=1 -> 沿着列方向"压扁", 得到每行的聚合
#   axis=None(默认) -> 全部压平为 1 个值

# 常用聚合函数一览:
# np.sum() / np.nansum()    -- nansum 忽略 NaN
# np.mean() / np.nanmean()
# np.std() / np.nanstd()    -- 标准差
# np.var()                  -- 方差
# np.max() / np.min()
# np.argmax() / np.argmin() -- 最大值/最小值的索引
# np.median()               -- 中位数
# np.percentile(arr, q)     -- 百分位数

# np.percentile 示例:
"data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])"
"print(np.percentile(data, 50))  # 5.5  (中位数, 同 median)"
"print(np.percentile(data, 25))  # 3.25 (下四分位)"
"print(np.percentile(data, 75))  # 7.75 (上四分位)"


print("\n" + "=" * 40 + "\n练习 2.2: 聚合函数")

# ■ 练习 2.2: 分析一只股票的历史数据
#
# 以下是一组股票的历史收盘价, 用 NumPy 计算:
#   1. 平均收盘价
#   2. 最高收盘价和最低收盘价
#   3. 标准差 (波动率指标)
#   4. 中位数

prices = np.array([12.5, 12.8, 13.2, 12.9, 13.5, 13.1, 12.7, 12.3, 12.9, 13.0])
#省略打印

# 提示: 用 np.mean(), np.max(), np.min(), np.std(), np.median()

# ↓ 你的代码 ↓
avg_price = np.mean(prices)
highest_price = np.max(prices)
lowest_price = np.min(prices)
std_price = np.std(prices)
median_price = np.median(prices)
print(f"平均价:{avg_price}  最高:{highest_price}  最低:{lowest_price}")
print(f"标准差:{std_price:.4f}  中位数:{median_price}")


# --- 2.4 广播 (Broadcasting) 简介 ---
# 广播让不同形状的数组也能做运算.
# 核心规则: 两个数组从末尾开始比维度, 维度相同或其中一个是 1.
""
"# 例子: 每列减去该列均值 (中心化)"
"matrix = np.array([[1, 2, 3],"
"                   [4, 5, 6],"
"                   [7, 8, 9]])"
"col_mean = np.mean(matrix, axis=0)  # [4. 5. 6.]  (每列均值)"
"centered = matrix - col_mean"
"# matrix 是 (3,3), col_mean 是 (3,) -> 广播后 col_mean 扩展为 (3,3)"
"print(centered)"
"# [[-3. -3. -3.]"
"#  [ 0.  0.  0.]"
"#  [ 3.  3.  3.]]"

# 量化场景: 批量计算多只股票的日收益率,
# 把收盘价矩阵 (N 只股票 x T 个交易日) 整体做运算, 不写循环.


print("\n" + "=" * 40 + "\n▸ Part 2 综合: 广播 + 聚合")

# ■ Part 2 综合: 对多只股票做中心化
#
# 以下是一个 3 只股票 x 5 个交易日的价格矩阵.
# 1. 用 np.mean 按列 (axis=0) 计算每只股票的均价
# 2. 用广播从每列中减去该列均值 (中心化)
# 3. 打印中心化后的矩阵, 并验证每列均值近似为 0

price_matrix = np.array([
    [100, 102, 101],
    [101, 103, 102],
    [102, 101, 103],
    [103, 102, 104],
    [104, 103, 105]
])
# shape: (5, 3) -> 5 天, 3 只股票

# 提示: 均值是按列算还是按行算? 减完之后验证.

# ↓ 你的代码 ↓
col_mean = np.mean(price_matrix, axis=0)
centered_matrix = price_matrix - col_mean
print(centered_matrix)
if np.allclose(centered_matrix.mean(axis=0), 0):
    print('均值为零')



# ═══════════════════════════════════════════════════
# 三, 索引与切片
# ═══════════════════════════════════════════════════
# ndarray 的索引/切片和 list 基本一致, 但功能更强.

# --- 3.1 一维数组索引 ---
"arr = np.array([10, 20, 30, 40, 50])"
"print(arr[0])       # 10      (正索引, 第 1 个)"
"print(arr[-1])      # 50      (负索引, 最后 1 个)"
"print(arr[1:4])     # [20 30 40]  (切片, 左闭右开)"
"print(arr[::-1])    # [50 40 30 20 10]  (倒序)"

# 切片语法: arr[start:stop:step], 和 list 完全一样
# start(含), stop(不含), step(步长)


print("\n" + "=" * 40 + "\n练习 3.1: 一维索引与切片")

# ■ 练习 3.1: 提取股票数据的子集
#
# 以下是一周的收盘价 (周一 ~ 周五):
#   1. 用正索引取出周三 (第 3 个) 的价格
#   2. 用负索引取出周五 (最后 1 个) 的价格
#   3. 用切片取出周一 ~ 周三 (前 3 个)
#   4. 用倒序切片输出倒序的周数据

weekly_close = np.array([12.5, 12.8, 13.0, 12.9, 13.2])

# ↓ 你的代码 ↓
print(weekly_close[2])
print(weekly_close[-1])
print(weekly_close[0:3])
print(weekly_close[::-1])



# --- 3.2 二维数组索引 ---
"matrix = np.array([[1, 2, 3],"
"                   [4, 5, 6],"
"                   [7, 8, 9]])"
""
"print(matrix[0, 1])     # 2    (第 0 行, 第 1 列)"
"print(matrix[1])        # [4 5 6]  (第 1 行, 整行)"
"print(matrix[:, 0])     # [1 4 7]  (第 0 列, 整列)"
"print(matrix[0:2, 1:3]) # [[2 3], [5 6]]  (子矩阵)"
""
# 语法: arr[行索引, 列索引]
#   : 表示"全部"或切片
#   用逗号分隔行和列的索引


print("\n" + "=" * 40 + "\n练习 3.2: 二维索引")

# ■ 练习 3.2: 从行情矩阵提取数据
#
# 矩阵: 5 天 x 4 列 (开盘价, 最高价, 最低价, 收盘价)
# 用索引提取:
#   1. 第 3 天的全部数据 (第 3 行)
#   2. 所有天的收盘价 (第 3 列)
#   3. 前 3 天的开盘价和收盘价 (前 3 行, 第 0 列和第 3 列)
#   4. 第 2 天到第 4 天的最高价 (行 1:4, 第 2 列)

kline = np.array([
    [12.5, 12.8, 12.4, 12.7],
    [12.7, 13.0, 12.6, 12.9],
    [12.9, 13.2, 12.8, 13.1],
    [13.1, 13.3, 12.9, 13.2],
    [13.2, 13.5, 13.0, 13.4]
])
# 列: 0=开盘, 1=最高, 2=最低, 3=收盘

# ↓ 你的代码 ↓
print(kline[2])
print(kline[:,3])
print(kline[0:3,[0,3]])
print(kline[1:4,1])

# --- 3.3 布尔索引 (最重要的技巧之一) ---
# 用一个布尔数组筛选元素, 返回满足条件的元素

"prices = np.array([12.5, 12.8, 12.4, 12.75, 13.0])"
"mask = prices > 12.6"
"print(mask)               # [False  True False  True  True]"
"print(prices[mask])       # [12.8  12.75 13. ]"
""
# 一行搞定:
"print(prices[prices > 12.6])  # [12.8  12.75 13. ]"

# 组合条件用 & (and) 和 | (or), 每个条件必须加括号
"print(prices[(prices > 12.5) & (prices < 13.0)])  # [12.5  12.75 12.8]"

# 量化场景: 选出涨幅>5%的股票, 成交量异常的日期


print("\n" + "=" * 40 + "\n练习 3.3: 布尔索引")

# ■ 练习 3.3: 筛选异常行情
#
# 给定收盘价数组, 找到:
#   1. 所有价格 >= 13.0 的日期
#   2. 价格在 12.6 ~ 13.0 之间的日期 (含两端)
#   3. 计算满足条件的天数和占比

prices_arr = np.array([12.5, 13.2, 12.8, 13.5, 12.3, 13.0, 12.9, 13.1])

# 提示: 布尔索引 + & 组合条件, 想想怎么算比例

# ↓ 你的代码 ↓
mask1 = prices_arr >= 13.0
print(prices_arr[mask1])
mask2 = (prices_arr >= 12.6) & (prices_arr <= 13.0)
print(prices_arr[mask2])
days = len(prices_arr[mask1])
print(f"满足条件的天数为{days}")
ratio = days / len(prices_arr)
print(f"满足条件的天数占比为{ratio}")


# --- 3.4 花式索引 (Fancy Indexing) ---
# 用整数数组作为索引, 可以按任意顺序取元素

"arr = np.array([10, 20, 30, 40, 50, 60])"
"indices = np.array([0, 2, 4])"
"print(arr[indices])   # [10 30 50]  (取第 0, 2, 4 个元素)"
""
"# 用 list 也行"
"print(arr[[0, 3, 5]])  # [10 40 60]"


print("\n" + "=" * 40 + "\n练习 3.4: 花式索引")

# ■ 练习 3.4: 用花式索引重排数据
#
# 以下按股票代码排序的收盘价, 用花式索引取出:
#   1. 第 1, 3, 5 只股票的价格 (索引 0, 2, 4)
#   2. 最后 3 只股票 (索引 -3, -2, -1)
#   3. 倒序排列 (想想切片步长 -1)

stock_prices = np.array([12.5, 8.3, 225.0, 20.5, 35.0, 28.0])

# ↓ 你的代码 ↓
print(stock_prices[[0,2,4]])
print(stock_prices[[-3,-2,-1]])
print(stock_prices[::-1])


# ═══════════════════════════════════════════════════
# ▸ Day 综合练习: 向量化股票分析工具
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n综合练习: 向量化股票分析工具")

# 综合运用今天学到的所有 NumPy 知识.
#
# 给定 3 只股票 10 个交易日的行情数据 (收盘价),
# 完成以下分析任务:
#
# 数据说明: prices_matrix (10 天 x 3 只股票)
#   列 0: 贵州茅台 (高价股)
#   列 1: 招商银行 (中价股)
#   列 2: 宁德时代 (高价股)
#
# 任务:
# 1. 计算每只股票的 10 日平均收盘价 (列均值)
# 2. 计算每只股票的日收益率向量 (向量化, 不要 for 循环)
#    日收益率 = (当日价 / 前日价 - 1)
# 3. 计算每只股票日收益率的均值和标准差
#    (均值 -> 平均日收益, 标准差 -> 波动率)
# 4. 找到每只股票的最高收盘价和对应日期索引 (np.argmax)
# 5. 用布尔索引找出茅台收盘价 > 1820 的天数
# 6. 计算 "低价股" 筛选: 找出招商银行收盘价 < 36 的所有数据
# 7. (附加) 计算 3 只股票每日收益率的相关系数矩阵
#    np.corrcoef() 或 np.cov()
#
# 输出格式参考:
#   贵州茅台均价: xxx.xx
#   招商银行均价: xxx.xx
#   宁德时代均价: xxx.xx
#   贵州茅台日收益率均值: x.xx%, 波动率: x.xx%
#   ...

prices_matrix = np.array([
    [1800.0, 35.5, 225.0],
    [1810.5, 35.8, 226.5],
    [1805.0, 35.2, 224.0],
    [1820.0, 35.9, 227.5],
    [1835.0, 36.5, 229.0],
    [1825.0, 36.0, 228.0],
    [1815.0, 35.6, 226.0],
    [1830.0, 36.2, 230.0],
    [1840.0, 36.8, 232.0],
    [1835.0, 36.5, 231.0]
])

# 先把 3 只股票分变量存放 (方便后续引用)

# ↓ 你的代码 ↓
maotai_avg = np.mean(prices_matrix[:,0],axis = 0)
zhaoshang_avg = np.mean(prices_matrix[:,1],axis = 0)
ningde_avg = np.mean(prices_matrix[:,2],axis = 0)
# avg = np.mean(prices_matrix,axis = 0)
raido = prices_matrix[1:]/prices_matrix[:-1]-1
raido_avg = np.mean(raido,axis = 0)
raido_stu = np.std(raido,axis = 0)
max_prices_index = np.argmax(prices_matrix , axis = 0)
max_prices_date = trading_days[max_prices_index]
maotai_price = prices_matrix[:,0]
zhaoshang_price = prices_matrix[:,1]
maotai_price_mask = maotai_price > 1820
maotai_price_days = np.sum(maotai_price_mask)
zhaoshao_prices_mask = zhaoshang_price < 36.0
zhaoshao_prices = prices_matrix[zhaoshao_prices_mask]

print(f"{GREEN}贵州茅台均价:{maotai_avg:.2f}{RESET}")
print(f"{GREEN}招商银行均价:{zhaoshang_avg:.2f}{RESET}")
print(f"{GREEN}宁德时代均价:{ningde_avg:.2f}{RESET}")
print(f"{YELLOW}贵州茅台日收益率均值:{raido_avg[0]:.6f}, 波动率:{raido_stu[0]:.6f}{RESET}")
print(f"{YELLOW}招商银行日收益率均值:{raido_avg[1]:.6f}, 波动率:{raido_stu[1]:.6f}{RESET}")
print(f"{YELLOW}宁德时代日收益率均值:{raido_avg[2]:.6f}, 波动率:{raido_stu[2]:.6f}{RESET}")
print(f"{BLUE}贵州茅台最高收盘价(日期):{max_prices_date}{RESET}")
print(f"{BLUE}贵州茅台收盘价 > 1820 的天数:{maotai_price_days}{RESET}")
print(f"{CYAN}招商银行收盘价 < 36 的所有数据:{zhaoshao_prices}{RESET}")


# ═══════════════════════════════════════════════════
# 副线: 正则表达式 (re 模块) — 清理脏数据
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n副线练习: 正则清洗")

# 量化开发每天面对脏数据: 格式不统一、夹杂空格符号、
# 混合编码. 正则表达式 (re 模块) 是清洗利器.
#
# 常用 re 函数:
#   re.findall(模式, 字符串)  -> 返回所有匹配的列表
#   re.sub(模式, 替换, 字符串) -> 替换匹配的内容
#   re.match(模式, 字符串)    -> 从开头匹配, 返回 Match 或 None
#
# 常用模式写法:
#   \d+    -> 数字 (1位或多位)
#   \w+    -> 字母/数字/下划线
#   [A-Z]+ -> 大写字母
#   .      -> 任意字符
#   *      -> 0次或多次
#   +      -> 1次或多次

import re

# 示例: 从文本中提取股票代码
"text = '平安银行(000001.SZ) 收盘价 12.75 元'"
"codes = re.findall(r'\\d{6}', text)  # ['000001']"
"# r'\\d{6}' 表示: r 原始字符串(不转义), \\d 数字, {6} 正好6位"

# 示例: 替换格式
"price_str = '收盘价: 12.75 元'"
"clean = re.sub(r'[^\\d.]', '', price_str)  # '12.75'"
"# [^\\d.] 表示: 非数字和非小数点, 全部替换为空"


# ■ 练习 R1: 从混合文本中提取股票代码和价格
#
# 以下是从不同数据源抓来的脏数据, 每行格式不统一.
# 用 re.findall 提取出每行的 stock_code 和 price,
# 存入 numpy 数组 (略过提取失败的).
#
# 提示: r'\\d{6}' 匹配6位数字, r'\\d+\\.\\d+' 匹配小数

dirty_data = [
    "平安银行(000001)收盘12.75",
    "000002·招商银行·8.35元",
    "万科A(000002) 收盘 28.5",
    "代码:000651 格力电器 45.20",
    "贵州茅台600519报收1800.50",
    "data error line",
    "300750宁德时代 226.5",
]

# 提示: re.findall(r'\d{6}', line) 取代码
#       re.findall(r'\d+\.\d+', line) 取价格
#       用 try 跳过提取失败的脏行

# ↓ 你的代码 ↓
list_date = []
for raw_date in dirty_data :
        stock_code = re.findall(r'\d{6}',raw_date)
        price = re.findall(r'\d+\.\d+',raw_date)
        if stock_code and price :
            list_date.append([int(stock_code[0]),float(price[0])])
arr =np.array(list_date)

