"""
遗漏知识点 — 各 Day 教学时未覆盖/补充的内容 (已归档)

本文件记录教学过程中发现的遗漏知识点，按 Day 分类。
可独立运行，也可作为复习参考。

历史: 本文件内容已部分纳入 Day 07 复习课。
Day 01-03 的控制流/字符串/类型注解等内容, 在复习课中以找bug+综合题形式覆盖。
此文件保留作为补充练习, 如需深入练习仍可使用。

⚠️ 不要修改之前的 day 文件，遗漏统一记在这里。
"""

# ═══════════════════════════════════════════════════
# Day 01 遗漏: if/elif/else, for, while, 比较/逻辑运算符
# ═══════════════════════════════════════════════════

# --- 1.1 if/elif/else ---

price = 1800
if price > 1000:
    print("高价股")
else:
    print("低价股")

# 多个条件:elif = else + if
if price > 2000:
    print("超高价")
elif price > 1000:
    print("高价")
else:
    print("正常价")

# --- 1.2 比较运算符 ---
# >  大于   <  小于   >=  大于等于   <=  小于等于
# == 等于   != 不等于
# 返回 True 或 False
print(100 > 50)     # True
print(100 == 50)    # False
print(100 != 50)    # True

# --- 1.3 逻辑运算符 ---
# and: 两边都 True 才 True
# or:  一边 True 就 True
# not: 取反
if price > 1000 and price < 2000:
    print("千元股")

if price < 500 or price > 2000:
    print("极端价格")

if not price == 0:
    print("价格不为零")

# --- 1.4 for 循环 ---
# 遍历序列(列表/字符串/range等)的每个元素
# C++: for (int i = 0; i < 5; i++) { ... }
# Python: for i in range(5): ...

stocks = ["茅台", "招行", "腾讯"]
for s in stocks:
    print(s)

# range(stop): 0 到 stop-1
for i in range(5):
    print(i)            # 0,1,2,3,4

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)            # 1,3,5,7,9

# --- 1.5 while 循环 ---
# 条件为 True 时一直执行
# 必须确保条件最终变为 False, 否则死循环

cash = 1000
target = 5000
while cash < target:
    cash += 500
    print(f"当前资金: {cash}")
print("目标达成!")

# break: 提前跳出循环
# continue: 跳过本次循环剩余部分
for s in stocks:
    if s == "招行":
        continue        # 跳过招行
    print(f"处理: {s}")

for s in stocks:
    if s == "腾讯":
        print("找到腾讯, 停止")
        break


# --- 练习: 综合控制流 ---
print("\n--- Day 01 遗漏: 控制流练习 ---")
# 给定股票列表和价格, 找出所有价格 > 50 的股票
stock_prices = {"茅台": 180, "招行": 35, "腾讯": 420, "平安": 45, "宁德": 220}
# 用 for 循环遍历字典, 用 if 筛选
# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# Day 02 遗漏: not in, 字符串不可变
# ═══════════════════════════════════════════════════

# --- 2.1 not in ---
# 判断"不包含"
stocks_list = ["茅台", "五粮液", "泸州老窖"]
if "招商" not in stocks_list:
    print("招商不在列表中")

# --- 2.2 字符串不可变 ---
s = "hello"
# s[0] = "H"  # ❌ 报错! 字符串不能修改
s = "H" + s[1:]  # ✅ 正确做法:创建新字符串
print(s)

# --- 2.3 深浅拷贝(拓展) ---
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999  # 影响原列表!
print(f"浅拷贝: original={original}")  # 也被改了

import copy
deep = copy.deepcopy(original)
deep[0][0] = 111
print(f"深拷贝: original={original}, deep={deep}")


print("\n--- Day 02 遗漏练习 ---")
# 列表去重: 给定 stocks = ["A", "B", "A", "C", "B"]
# 用 for 循环 + not in 实现去重(不用set)
# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# Day 03 遗漏: 类型注解, 文档字符串
# ═══════════════════════════════════════════════════

# --- 3.1 类型注解 (type hints) ---
# 告诉读代码的人: 参数应该是什么类型, 返回什么类型
# 不会强制检查, 但 IDE 和 Pylance 会用它们做提示

def calculate_pnl(buy_price: float, current: float, shares: int) -> float:
    """计算持仓盈亏

    参数:
        buy_price: 买入价
        current: 当前价
        shares: 持仓数量
    返回:
        浮动盈亏金额
    """
    return (current - buy_price) * shares

pnl = calculate_pnl(1750.50, 1820.00, 100)
print(f"类型注解版 PnL: {pnl}")

# --- 3.2 文档字符串 (docstring) ---
# 函数第一行的 """...""" 就是文档字符串
# 可以用 help(函数名) 查看

def calc_sharpe(returns: list) -> float:
    """计算夏普比率(简化版)

    夏普比率衡量风险调整后收益,
    越大代表策略性价比越高.
    """
    avg = sum(returns) / len(returns)
    return avg

help(calc_sharpe)


# ═══════════════════════════════════════════════════
# 综合练习: 简单的均线策略判断
# ═══════════════════════════════════════════════════

print("\n--- 综合练习 ---")
# 给定5天的收盘价, 用 for 循环 + if 判断:
# 如果今天价格 > 5日均线(简单平均), 打印 "↑ 多头"
# 如果今天价格 < 5日均线, 打印 "↓ 空头"
# 如果价格突破 5日均线 ±2%, 打印 "⚠️ 异常"

prices = [178, 180, 179, 182, 181, 185, 183]
# 提示: 用 prices[i] 获取第 i 天价格
#      用 sum(prices[:i]) / i 算到第 i 天为止的均线

# ↓ 你的代码 ↓
