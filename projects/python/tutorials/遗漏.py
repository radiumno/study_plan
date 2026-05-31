"""
遗漏知识点 — 各 Day 教学时未覆盖/补充的内容

本文件记录教学过程中发现的遗漏知识点，按 Day 分类。
可独立运行，也可作为复习参考。
"""

# ═══════════════════════════════════════════════════
# Day 01 遗漏: if/else 条件判断
# ═══════════════════════════════════════════════════
# C++: if (条件) { ... } else { ... }
# Python: 不用括号, 用缩进. 条件后加冒号 :

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

# 逻辑运算符:and or not
if price > 1000 and price < 2000:
    print("千元股")

print("--- Day 01 遗漏: if/else 基础 ---")
# 练习:用 if 判断盈亏
buy = 1750.50
current = 1820.00
profit = current - buy
if profit > 0:
    print("✅ 盈利")
else:
    print("❌ 亏损")


# ═══════════════════════════════════════════════════
# Day 02 遗漏: not in / 字符串不可变 / 深浅拷贝
# ═══════════════════════════════════════════════════
print("--- Day 02 遗漏: not in / 字符串不可变 ---")

# not in 判断不包含
stocks = ["茅台", "五粮液", "泸州老窖"]
if "招商" not in stocks:
    print("招商不在列表中")

# 字符串不可变
s = "hello"
# s[0] = "H"  # ❌ 报错! 字符串不能修改
s = "H" + s[1:]  # ✅ 正确做法:创建新字符串
print(s)

# 深浅拷贝(拓展)
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 999  # 影响原列表!
print(f"浅拷贝后: original={original}")  # 也被改了


# ═══════════════════════════════════════════════════
# Day 03 遗漏: 类型注解 (type hints)
# ═══════════════════════════════════════════════════
print("--- Day 03 遗漏: 类型注解 ---")

def calculate_pnl(buy_price: float, current: float, shares: int) -> float:
    return (current - buy_price) * shares

pnl = calculate_pnl(1750.50, 1820.00, 100)
print(f"类型注解版 PnL: {pnl}")
