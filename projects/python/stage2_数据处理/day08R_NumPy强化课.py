"""
====================================================
 Day 08R | NumPy 强化课 — 补短板, 打扎实
====================================================

 目标: 攻克 Day 08 最常见的 4 个薄弱点:
   1. axis 参数 (axis=0 到底是行还是列?)
   2. 广播机制 (不同形状怎么算?)
   3. 布尔索引 + 条件组合 (& 和 | 的括号陷阱)
   4. 向量化思维 (告别 for 循环)

 形式: 每个知识点先"纠正误解", 再"练到对"

 参考源:
   - NumPy 官方文档 (numpy.org/doc/stable/user/basics.broadcasting.html)
   - 尚硅谷 Python 数据分析 (b23.tv/BV1D9GLzyEL6)
   - Real Python NumPy 教程 (realpython.com/numpy-array-programming)

====================================================
"""

# ═══════════════════════════════════════════════════
# 进度: 阶段1 Python基础 -- Part 2 数据处理 (Day 08~14)
#   Day 08 NumPy 数组运算   ✅
#   Day 08R ▶ NumPy 强化    (今天)
#   Day 09 Pandas 入门      (后续)
#   Day 10 Pandas 进阶      (后续)
#   Day 11 Matplotlib 可视化
#   Day 12 复习日
#   Day 13-14 数据采集+综合
# ═══════════════════════════════════════════════════

import numpy as np

# 颜色输出
GREEN  = '\033[92m'
YELLOW = '\033[93m'
BLUE   = '\033[94m'
RED    = '\033[91m'
CYAN   = '\033[96m'
RESET  = '\033[0m'


# ═══════════════════════════════════════════════════
# 热身: 快速回顾创建 + 基础运算 (3 分钟)
# ═══════════════════════════════════════════════════
# 如果下面的代码你一眼看不懂, 回去复习 Day 08 的 Part 1-2.

prices = np.array([12.5, 12.8, 12.4, 12.75, 13.0])
print(f"{GREEN}热身检查{RESET}")
print(f"  prices: {prices}")
print(f"  shape: {prices.shape}, dtype: {prices.dtype}")
print(f"  prices + 0.5: {prices + 0.5}")    # 广播
print(f"  prices[1:] / prices[:-1] - 1: {prices[1:] / prices[:-1] - 1}")  # 日收益率
print()

# ═══════════════════════════════════════════════════
# 一, axis 参数 — 量化开发 90% 的人在这里错过年薪
# ═══════════════════════════════════════════════════
# 最常见的误解:
#   ❌ "axis=0 是按行操作" (错!)
#   ✅ "axis=0 是沿着行的方向压扁 -> 得到每列的聚合"
#   ✅ "axis=1 是沿着列的方向压扁 -> 得到每行的聚合"
#
# 换个角度理解:
#   对一个 (3, 4) 的矩阵:
#     axis=0 -> 把 3 行"压"成 1 行 -> 结果有 4 个值 (每列一个)
#     axis=1 -> 把 4 列"压"成 1 列 -> 结果有 3 个值 (每行一个)
#
# 量化场景: 你有 5 只股票 x 252 个交易日
#   axis=0 按列聚合 -> 每只股票的全年均值 (5 个值)
#   axis=1 按行聚合 -> 每天所有股票的平均价 (252 个值)

print(f"{GREEN}═══ 一, axis 参数深度理解 ═══{RESET}")

# 用 3x4 矩阵做直观演示
demo = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])
print(f"\ndemo 矩阵 (3行 x 4列):\n{demo}")

# axis=0: 沿着"行方向"往下走, 每列 3 个数聚合成 1 个
print(f"\naxis=0 (沿行方向压扁 → 每列聚合):")
print(f"  np.sum(demo, axis=0)     = {np.sum(demo, axis=0)}")     # [15 18 21 24]
print(f"  np.mean(demo, axis=0)    = {np.mean(demo, axis=0)}")    # [5. 6. 7. 8.]
# 第 0 列: 1+5+9 = 15, 第 1 列: 2+6+10 = 18 ...

# axis=1: 沿着"列方向"往右走, 每行 4 个数聚合成 1 个
print(f"\naxis=1 (沿列方向压扁 → 每行聚合):")
print(f"  np.sum(demo, axis=1)     = {np.sum(demo, axis=1)}")     # [10 26 42]
print(f"  np.mean(demo, axis=1)    = {np.mean(demo, axis=1)}")    # [2.5 6.5 10.5]
# 第 0 行: 1+2+3+4 = 10, 第 1 行: 5+6+7+8 = 26 ...

print(f"\n  记住: axis=0 按列出结果, axis=1 按行出结果")
print(f"   因为 axis=0 压扁的是行, 留下的当然是列!")


print("\n" + "=" * 40 + "\n练习 1.1: axis 选择题")

# ■ 练习 1.1: 不运行代码, 写出结果
#
# 以下数据: 4 只股票 x 5 个交易日的收益率(%)
#           股票A  股票B  股票C  股票D
#   day1    [0.5,  -0.2,  1.0,  -0.5],
#   day2    [0.3,   0.1,  0.8,  -0.3],
#   day3    [-0.2,  0.4,  1.2,  0.1],
#   day4    [0.6,   0.0,  0.9,  0.2],
#   day5    [0.1,  -0.1,  1.1,  0.0]
#
# 先手写答案, 再运行验证:

returns = np.array([
    [0.5, -0.2,  1.0, -0.5],
    [0.3,  0.1,  0.8, -0.3],
    [-0.2, 0.4,  1.2,  0.1],
    [0.6,  0.0,  0.9,  0.2],
    [0.1, -0.1,  1.1,  0.0]
])

# Q1: np.mean(returns, axis=0) 的形状和值是什么?
#     shape = (4,) 还是 (5,)?
#     每只股票的 5 日平均收益率?
#     还是每天的 4 只股票平均收益率?

# ↓ 先写你的答案 (注释), 再运行:
#（4，）
#每只的平均
date = np.mean(returns,axis=0)
print(date)
print(np.shape(date))


# Q2: np.max(returns, axis=1) 的形状和值是什么?
#     每天的最差股票? 还是每只股票的最好一天?

# ↓ 先写答案, 再运行:
#每只股票最好的一天
print(np.max(returns,axis=1))


# Q3: np.argmin(returns, axis=0) 的结果是什么?
#     每列最低点的索引? 还是每行最低点的索引?

# ↓ 先写答案, 再运行:
#每列最低点的索引
print(f'每列最低点的索引{np.argmin(returns,axis=0)}')



print("\n" + "=" * 40 + "\n练习 1.2: axis 实战 — 多股票分析")

# ■ 练习 1.2: 用合适的 axis 完成以下任务
#
# prices_3d: shape (5, 3) = 5 天 x 3 只股票
#   列 0: 茅台 (高价), 列 1: 招行 (中价), 列 2: 宁德 (高价)

prices_3d = np.array([
    [1800.0, 35.5, 225.0],
    [1810.5, 35.8, 226.5],
    [1805.0, 35.2, 224.0],
    [1820.0, 35.9, 227.5],
    [1835.0, 36.5, 229.0]
])

# 1. 每只股票的 5 日平均价 (3 个值)
#    提示: 沿行方向压扁, axis=?
avg_per_stock = np.mean(prices_3d,axis = 0 )  # 你的代码
print(f"每只股票均价: {avg_per_stock}")

# 2. 每天所有股票的平均价 (5 个值)
#    提示: 沿列方向压扁, axis=?
avg_per_day = np.mean(prices_3d,axis = 1)  # 你的代码
print(f"每天均价: {avg_per_day}")

# 3. 每只股票的最高价
high_per_stock = np.max(prices_3d,axis = 0)  # 你的代码
print(f"每只股票最高价: {high_per_stock}")

# 4. 找出每天涨幅最大的股票索引 (np.argmax)
ratio = prices_3d[1:]/prices_3d[:-1]-1
best_per_day = np.argmax(ratio,axis = 1)  # 你的代码, 提示: 对日收益率做 argmax
print(f"每天涨幅最大股票索引: {best_per_day}")

# 5. (附加) 计算每只股票的日收益率标准差 (波动率)
#    先算日收益率 (向量化), 再按列算 std
daily_ret_3d = ratio  # prices_3d[1:] / prices_3d[:-1] - 1
vol_per_stock = np.std(ratio,axis =0)  # 你的代码
print(f"每只股票波动率: {vol_per_stock}")


# ═══════════════════════════════════════════════════
# 二, 广播 (Broadcasting) — 看着怪但必须懂
# ═══════════════════════════════════════════════════
# 广播规则: 两个数组从末尾开始比维度,
#   维度相同 -> OK
#   维度不同但一方是 1 -> 扩展成相同
#   维度不同且都不是 1 -> 报错
#
# 量化场景: 批量标准化多只股票
#   shape (1000, 5) 减去 shape (5,) -> 每列减该列均值

print(f"\n{GREEN}═══ 二, 广播机制 ═══{RESET}")

# 最常见的广播: 数组 + 标量
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n数组 + 标量:")
print(f"  arr:       {arr}")
print(f"  arr + 10:  {arr + 10}")   # 标量 10 广播成 [[10,10,10],[10,10,10]]

# 一维 + 二维广播:
row = np.array([10, 20, 30])
print(f"\n二维 + 一维:")
print(f"  arr:  {arr}")
print(f"  row:  {row}")
print(f"  arr + row: \n{arr + row}")
# row (3,) 广播为 (2,3) -> [[10,20,30],[10,20,30]]

# 列向量广播:
col = np.array([[10], [20]])   # shape (2, 1)
print(f"\n二维 + 列向量:")
print(f"  arr:  {arr}")
print(f"  col:  {col}")
print(f"  arr + col: \n{arr + col}")
# col (2,1) 广播为 (2,3) -> [[10,10,10],[20,20,20]]


print("\n" + "=" * 40 + "\n练习 2.1: 广播纠错")

# ■ 练习 2.1: 这些广播哪个会报错? 为什么?
#
# 在下面写出你的判断, 再运行验证.

a = np.ones((3, 4))      # shape (3, 4)
b = np.ones(4)            # shape (4,)
c = np.ones((3, 1))      # shape (3, 1)
d = np.ones((2, 3))      # shape (2, 3)  ← 注意: 和 a 不同

# Q1: a + b      → 可行?   (3,4) vs (4,)
# Q2: a + c      → 可行?   (3,4) vs (3,1)
# Q3: a + d      → 可行?   (3,4) vs (2,3)
# Q4: b + c      → 可行?   (4,) vs (3,1)
# Q5: d + c      → 可行?   (2,3) vs (3,1)

# ↓ 把结论写在这里:



# 运行验证
# print(f"\na + b: {a + b}")        # 你的判断:
# print(f"a + c: \n{a + c}")        # 你的判断:
# print(f"d + c: \n{d + c}")        # 你的判断:


print("\n" + "=" * 40 + "\n练习 2.2: 广播标准化")

# ■ 练习 2.2: 批量标准化
#
# 标准化公式: (x - mean) / std
# 对 prices_3d (5天x3只股票) 做标准化:
#   1. 计算每只股票的均值和标准差 (axis=?)
#   2. 用广播从每列减去均值、除以标准差
#   3. 验证标准化后的每列均值为 0, 标准差为 1

# 先用正确的 axis 算均值和标准差
mean_vals = np.mean(prices_3d , axis = 0)  # 你的代码 (shape: (3,))
std_vals = np.std(prices_3d , axis =0)   # 你的代码 (shape: (3,))

print(f"\n均值: {mean_vals}")
print(f"标准差: {std_vals}")

# 用广播做标准化
normalized = (prices_3d - mean_vals) / std_vals  # (prices_3d - mean_vals) / std_vals

print(f"\n标准化后矩阵:\n{normalized}")

# 验证: 检查每列是否均值为 0
check_mean = np.mean(normalized, axis=0)
check_std = np.std(normalized, axis=0)
# ↓ 你的代码: 用 np.allclose 验证差值接近 0
print(check_mean)
print(check_std)

# ═══════════════════════════════════════════════════
# 三, 布尔索引 + 复合条件 — & 和 | 的括号陷阱
# ═══════════════════════════════════════════════════
# 最常见的错误:
#   ❌ prices > 12.5 & prices < 13.0  (报错)
#   ✅ (prices > 12.5) & (prices < 13.0)
#
# 原因: & 的优先级比 < > 低, 必须加括号.
# 另一个: Python 的 and/or 不能用在 NumPy 布尔数组上!
#   ❌ (prices > 12.5) and (prices < 13.0)  (报错)
#   ✅ (prices > 12.5) & (prices < 13.0)

print(f"\n{GREEN}═══ 三, 布尔索引 + 复合条件 ═══{RESET}")

# 陷阱对比
test_arr = np.array([10, 15, 20, 25, 30])

# ✅ 正确写法
result = test_arr[(test_arr > 12) & (test_arr < 28)]
print(f"\n✅ (test_arr > 12) & (test_arr < 28): {result}")

# ❌ 常见报错: 不加括号
# prices > 12 & prices < 28  # ValueError

# ❌ 常见报错: 用 and/or
# prices > 12 and prices < 28  # ValueError


print("\n" + "=" * 40 + "\n练习 3.1: 条件筛选纠错")

# ■ 练习 3.1: 找出下面代码中的错误并修正
#
# 目标: 找到 stock_data 中价格在 12.5 ~ 14.0 之间的元素

stock_data = np.array([11.5, 13.2, 14.5, 12.8, 13.0, 11.0, 14.2])

# 下面这行哪里错了? 修正它.
# wrong_result = stock_data > 12.5 & stock_data < 14.0

# ↓ 修正后的代码:
right_result = (stock_data > 12.5)&(stock_data < 14.0)


# print(f"\n修正前的结果: {wrong_result}")

# 这是另一个常见错误:
price_high = stock_data > 13.0
volume_high = np.array([True, False, True, True, False, False, True])

# 下面的 and 哪里错了? 用 & 修正
combined = price_high & volume_high

# ↓ 修正后的代码: 用 & 连接两个布尔数组


print(f"\n修改后的组合条件: {combined}")


print("\n" + "=" * 40 + "\n练习 3.2: 布尔索引实战 — 异常检测")

# ■ 练习 3.2: 检测量价异常
#
# 给定 10 天的收盘价和成交量, 找出:
#   1. 收盘价 > 14.0 的天数
#   2. 成交量 > 50000 的天数
#   3. 收盘价 > 14.0 且 成交量 > 50000 的天数 (量价齐升)
#   4. 收盘价 < 13.5 或 成交量 < 30000 的天数 (冷清)

close_prices = np.array([12.5, 14.2, 13.8, 15.0, 13.2, 14.5, 12.8, 14.0, 13.5, 14.8])
volumes = np.array([30000, 52000, 28000, 58000, 25000, 55000, 32000, 48000, 35000, 60000])

# ↓ 你的代码:
# 1. 收盘价 > 14.0
mask_price_high = close_prices > 14.0
print(f"收盘价 > 14.0 的天数: {np.sum(mask_price_high)}, 价格: {close_prices[mask_price_high]}")

# 2. 成交量 > 50000
mask_vol_high = volumes > 50000
print(f"成交量 > 50000 的天数: {np.sum(mask_vol_high)}")

# 3. 量价齐升 (价格高 & 成交量高)
mask_both = (close_prices[1:]>close_prices[:-1])&(volumes[1:]>volumes[:-1])
print(f"量价齐升天数: {np.sum(mask_both)}")

# 4. 冷清 (价格低 或 成交量低)
mask_cold = ~mask_both
print(f"冷清天数: {np.sum(mask_cold)}")

# 5. (附加) 用 ~ 取反: 找出不是"量价齐升"的天数


# ═══════════════════════════════════════════════════
# 四, 向量化思维 — 从 for 循环到数组运算
# ═══════════════════════════════════════════════════
# 这是 NumPy 最核心的思维转变:
#   不是"逐个元素处理", 而是"整批数据一起算".

print(f"\n{GREEN}═══ 四, 向量化思维 ═══{RESET}")

# 演示: 用 for 循环 vs 向量化 做同一件事
N = 1000000
loop_data = np.random.randn(N)

# for 循环版本
import time

def compute_with_loop(data):
    """计算 data 中所有正数的平方"""
    result = np.zeros_like(data)
    for i in range(len(data)):
        if data[i] > 0:
            result[i] = data[i] ** 2
    return result

def compute_vectorized(data):
    """向量化版本"""
    return np.where(data > 0, data ** 2, 0)

# 用小数据量比较 (大数据量 for 循环太慢了)
small_data = np.random.randn(100000)
t0 = time.time()
r1 = compute_with_loop(small_data)
t1 = time.time()
r2 = compute_vectorized(small_data)
t2 = time.time()

print(f"\n处理 100,000 个元素:")
print(f"  for 循环:    {(t1-t0)*1000:.1f} ms")
print(f"  向量化:      {(t2-t1)*1000:.1f} ms")
print(f"  加速比:      {(t1-t0)/(t2-t1):.0f}x")

# 结果验证相同
print(f"  结果一致:    {np.allclose(r1, r2)}")


print("\n" + "=" * 40 + "\n练习 4.1: 循环转向量化")

# ■ 练习 4.1: 把 for 循环改写成向量化
#
# 下面的函数用 for+if 实现了"信号生成":
#   如果昨日收益率 > 0, 今日信号 = 1 (买入)
#   如果昨日收益率 < 0, 今日信号 = -1 (卖出)
#   否则信号 = 0 (持有)

def generate_signals_loop(daily_returns):
    """用 for 循环生成交易信号"""
    n = len(daily_returns)
    signals = np.zeros(n)
    for i in range(1, n):
        if daily_returns[i-1] > 0:
            signals[i] = 1
        elif daily_returns[i-1] < 0:
            signals[i] = -1
        else:
            signals[i] = 0
    return signals

# 将上面改写成向量化版本 (用 np.where 或布尔索引)
# 提示: np.sign() 返回每个元素的正负号
#       或: np.where(条件, 值, 其他值)

def generate_signals_vectorized(daily_returns):
    """向量化版本 — 不用 for 循环, 不用 if"""
    n = len(daily_returns)
    signals = np.zeros(n)
    # ↓ 你的代码: 用前一天的 return 判断今天的信号
    # 提示: daily_returns[:-1] 得到前 n-1 天的收益率
    signals[1:]=np.where(daily_returns[:-1]>0,1,np.where(daily_returns[:-1]<0,-1,0))
    #signals[1:]=np.sign(daily_returns[:-1])
    return signals


# 测试
test_returns = np.array([0.02, -0.01, 0.0, 0.03, -0.02, 0.01, -0.005])
sig_loop = generate_signals_loop(test_returns)
sig_vec = generate_signals_vectorized(test_returns)
print(f"\nfor 循环版本:       {sig_loop}")
print(f"向量化版本:         {sig_vec}")
print(f"结果一致吗?         {np.array_equal(sig_loop, sig_vec)}")


print("\n" + "=" * 40 + "\n练习 4.2: 向量化计算移动平均线")

# ■ 练习 4.2: 不用卷积, 用广播/切片算移动平均
#
# 给定收盘价数组, 计算 3 日移动平均线 (SMA3).
# SMA3 的第 i 天 = (close[i-2] + close[i-1] + close[i]) / 3
# 结果应有 n-2 个值 (因为前 2 天算不了)
#
# 要求: 向量化, 不要 for 循环
# 提示: close[:-2] + close[1:-1] + close[2:]

closes_sma = np.array([100, 102, 101, 105, 108, 107, 110, 112])
# 预期 SMA3:
#   day3 (索引2): (100+102+101)/3 = 101.0
#   day4 (索引3): (102+101+105)/3 = 102.67
#   ...

# ↓ 你的向量化代码 (一行搞定)
sma3 = (closes_sma[:-2]+closes_sma[1:-1]+closes_sma[2:])/3
print(f"\n3 日移动平均: {sma3}")

# ---------- 分割线: 5 日移动平均 ----------
# 如果现在要算 SMA5, 怎么改?
# 不需要写新的, 想想通用公式: SMA_N = ?
def smaN(data,n):
    result=sum(data[i:i+1-n or None] for i in range(n))/n
    return result



# ═══════════════════════════════════════════════════
# 综合练习: 全流程日内交易信号引擎
# ═══════════════════════════════════════════════════

print(f"\n{GREEN}═══ 综合: 日内交易信号引擎 ═══{RESET}")

# 综合运用 axis / 广播 / 布尔索引 / 向量化
#
# 给定 3 只股票的 1 分钟高频数据 (100 分钟 x 3 只股票),
# 完成以下分析:
#
# 数据: minute_data (100, 3) — 每分钟收盘价
#   列 0: 股票 A, 列 1: 股票 B, 列 2: 股票 C
#
# 任务:
# 1. 用向量化计算每只股票每分钟的收益率 (99 x 3 矩阵)
# 2. 计算每只股票的"价格突破"信号:
#    - 如果当前价格 > 前 5 分钟均价 * 1.001 → 买入信号 (1)
#    - 如果当前价格 < 前 5 分钟均价 * 0.999 → 卖出信号 (-1)
#    - 否则 → 持有 (0)
#    提示: 算 SMA5 作为基准, 然后用广播做比较
# 3. 用布尔索引找出所有买入信号的总次数和分布
# 4. 计算每只股票在买入信号后的 1 分钟收益率 (信号有效性)
#    (买入后下一分钟涨了没有?)
# 5. (附加) 找到同时触发买入信号的分钟 (三只股票都买入)

# 生成模拟数据 (用随机游走)
np.random.seed(42)
n_minutes = 100
n_stocks = 3
# 从 100 开始, 每步加一个随机变动
price_changes = np.random.randn(n_minutes - 1, n_stocks) * 0.2
start_prices = np.array([50.0, 30.0, 80.0])

# 生成价格矩阵 (100 x 3):
#   第 0 分钟 = start_prices
#   第 t 分钟 = 第 t-1 分钟 + 变动
minute_data = np.zeros((n_minutes, n_stocks))
minute_data[0] = start_prices

# 用向量化填充 (np.cumsum + 广播)
minute_data = start_prices + np.cumsum(np.vstack([np.zeros((1, n_stocks)), price_changes]), axis=0)

print(f"\n数据生成完成: {minute_data.shape} (100 分钟 x 3 只股票)")

# ↓ 你的代码开始 ↓

# 1. 每分钟收益率 (99 x 3)
returns = minute_data[1:]/minute_data[:-1]  # 向量化计算
print(f"\n1. 收益率矩阵 shape: {returns.shape}")

# 2. 计算 SMA5 (前 5 分钟均价) 作为基准
#    提示: 用切片相加法, 结果 shape (96, 3)
sma5 = smaN(minute_data , 5)  # 你的代码
print(f"   SMA5 shape: {sma5.shape}")

# 生成信号: 比较 minute_data[4:] (第 5 分钟起) 和 sma5
#    注意: sma5 的第 0 行对应 minute_data[4:], 长度 96
current_prices = minute_data[4:]  # shape (96, 3)

# 条件判断 (布尔 -> 转成 1/-1/0)
buy_signal = None   # 条件: current_prices > sma5 * 1.001
sell_signal = None  # 条件: current_prices < sma5 * 0.999
# 我直接写行吗

# 合并成信号矩阵: 买入=1, 卖出=-1, 其他=0
# 提示: 用 np.where, 或者用 1*buy + (-1)*sell
signals = np.where(current_prices > sma5 * 1.001 ,1 ,np.where(current_prices < sma5 * 0.999,-1,0))  # 你的代码
print(f"\n2. 信号矩阵 shape: {signals.shape}")
print(f"   买入信号总数: {np.sum(signals == 1)}")
print(f"   卖出信号总数: {np.sum(signals == -1)}")

# 3. 按股票统计买入信号次数
buy_count_per_stock = np.sum(signals==1,axis = 0) # 你的代码 (axis=?)
print(f"\n3. 每只股票买入信号次数: {buy_count_per_stock}")

# 4. 买入信号后的 1 分钟收益率
#    买入信号发生在 t, 计算 returns[t+1] 的均值
#    提示: 对 signals == 1 的位置, 取下一分钟的 returns
#    注意: signals 有 96 行, returns 有 99 行, 索引对应关系?
#          signals[t] 对应 returns[t+4]  (因为 sma5 从索引 4 开始)
buy_returns = returns[4:][signals[:-1]==1].mean()  # signals[:-1] 舍弃最后一分钟（无对应收益率）
print(f"\n4. 买入信号后 1 分钟平均收益率: {buy_returns}")

# 5. (附加) 三只股票同时买入的分钟
all_buy = np.all(signals==1,axis = 1)  # 你的代码
print(f"\n5. 三只股票同时买入的分钟数: {np.sum(all_buy)}")
