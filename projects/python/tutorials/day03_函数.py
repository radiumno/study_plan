"""
====================================================
 Day 3 | 函数 -- 把代码封装成可复用的模块
====================================================

 目标: 掌握函数定义, 参数传递, 多返回值, 作用域和 lambda

 结构: 讲一个知识点 -> 练一个 -> 再讲下一个 -> 最后综合练习

 对比 C++: Python 函数更灵活(多返回值/*args/**kwargs/lambda)
           但核心思想一样 -- 封装重复逻辑, 避免写重复代码

====================================================
"""

# ═══════════════════════════════════════════════════
# 一, 函数定义和调用
# ═══════════════════════════════════════════════════

"def 函数名(参数):"
"    \"\"\"文档字符串(可选)\"\"\""
"    # 函数体"
"    return 返回值"

# C++: int add(int a, int b) { return a + b; }
# Python:
"def add(a, b):"
"    return a + b"

"result = add(3, 5)"
"print(result)  # 8"

# 没有 return 返回 None
"def greet(name):"
"    print(f\"你好, {name}\")"

"ret = greet(\"兄弟\")"
"print(ret)  # None"


print("\n" + "=" * 40 + "\n练习 1")

# ■ 练习 1:定义函数
# 1. 写一个函数 calc_pnl(buy_price, sell_price, shares)
#    返回 (sell_price - buy_price) * shares
# 2. 写一个函数 price_trend(current, prev_close)
#    如果 current > prev_close 返回 "涨", 小于返回 "跌", 否则返回 "平"
# 3. 调用这两个函数并打印结果

# ↓ 你的代码 ↓
def calc_pnl(buy_price,sell_price,shares):
  return (sell_price-buy_price)*shares
def price_trend(current,prev_close):
  if current > prev_close:
    return "涨"
  if current < prev_close:
    return "跌"
  else :
    return "平"
print(calc_pnl(100,200,200))
print(price_trend(100,101))



# ═══════════════════════════════════════════════════
# 二, 参数进阶
# ═══════════════════════════════════════════════════

# --- 2.1 默认参数 ---
# C++ 也有默认参数, Python 写法类似

"def calc_commission(trade_value, rate=0.00025):"
"    return trade_value * rate"

"print(calc_commission(100000))           # 25.0 (默认万2.5)"
"print(calc_commission(100000, 0.0005))   # 50.0 (万5)"

# --- 2.2 关键字参数 ---
# 调用时指名道姓, 顺序可以乱

"def stock_info(name, price, pe):"
"    print(f\"{name}: {price}元, PE={pe}\")"

# 位置参数(和 C++ 一样)
"stock_info(\"茅台\", 180, 30)"

# 关键字参数(顺序无关)
"stock_info(price=30, name=\"招行\", pe=5)"

# 混用: 位置参数必须在关键字参数之前
"stock_info(\"宁德\", pe=20, price=250)"


# --- 2.3 *args -- 任意数量位置参数 ---
# 把多个参数打包成元组

"def total_market_cap(*args):"
"    total = 0"
"    for value in args:"
"        total += value"
"    return total"

"print(total_market_cap(10000, 20000, 15000))  # 45000"
"print(total_market_cap(5000))                  # 5000"


# --- 2.4 **kwargs -- 任意数量关键字参数 ---
# 把关键字参数打包成字典

"def print_stock_report(**kwargs):"
"    for key, value in kwargs.items():"
"        print(f\"{key}: {value}\")"

"print_stock_report(名称=\"茅台\", 价格=180, 涨幅=\"+2.5%\")"


# --- 2.5 混合使用顺序 ---
# 位置参数 > *args > 默认参数 > **kwargs

"def complex_func(a, b, *args, rate=0.01, **kwargs):"
"    print(f\"a={a}, b={b}, args={args}, rate={rate}, kwargs={kwargs}\")"

"complex_func(1, 2, 100, 200, rate=0.02, name=\"test\", value=500)"
# a=1, b=2, args=(100, 200), rate=0.02, kwargs={'name': 'test', 'value': 500}


print("\n" + "=" * 40 + "\n练习 2")

# ■ 练习 2:各种参数
# 1. 写一个函数 calc_asset_value(price, shares, tax_rate=0.001)
#    返回 price * shares * (1 - tax_rate)
# 2. 用位置参数调用: calc_asset_value(100, 50)
# 3. 用关键字参数调用: calc_asset_value(shares=50, price=100, tax_rate=0.002)
# 4. 写一个函数 print_report(**data), 遍历打印所有键值对

# ↓ 你的代码 ↓
def calc_asset_value(price,shares,tax_rate=0.001):
  return price * shares * (1-tax_rate)
cav_1 = calc_asset_value(100,50)
print(cav_1)
cav_2 = calc_asset_value(shares= 50 ,price= 100 ,tax_rate = 0.002)
print(cav_2)
def print_reoort(**data):
  for key,value in data.items():
     print(f"{key}:{value}")
print_reoort(名称='茅台',价格="180",涨幅="-2.5%")


# ═══════════════════════════════════════════════════
# 三, 函数是一等公民
# ═══════════════════════════════════════════════════

# Python 里函数也是值, 可以赋值给变量, 传参, 嵌套

"def add(a, b):"
"    return a + b"

"def sub(a, b):"
"    return a - b"

"# 函数赋值给变量"
"operation = add"
"print(operation(10, 5))  # 15"

"# 函数作为参数"
"def apply(func, a, b):"
"    return func(a, b)"

"print(apply(add, 10, 5))  # 15"
"print(apply(sub, 10, 5))  # 5"

# 多返回值(本质是返回元组, 自动解包)

"def analyze_kline(open_, high, low, close):"
"    avg = (open_ + high + low + close) / 4"
"    amp = high - low"
"    is_up = close > open_"
"    return avg, amp, is_up  # 返回3个值(实际上是元组)"

"avg, amp, up = analyze_kline(100, 105, 98, 102)"
"print(f\"均价:{avg:.2f}, 振幅:{amp}, 收涨:{up}\")"


print("\n" + "=" * 40 + "\n练习 3")

# ■ 练习 3:函数作为对象 + 多返回值
# 1. 写一个函数 calculate(func, a, b), 返回 func(a, b)
# 2. 写三个函数: multiply(a, b), divide(a, b), max_value(a, b)
#    分别传入 calculate 并打印结果
# 3. 写一个函数 stock_stats(prices_list)
#    接收一个价格列表, 返回 (最高价, 最低价, 平均价, 价格个数)
# 4. 调用 stock_stats 并解包接收

# ↓ 你的代码 ↓
def multiply(a,b):
  return a*b
def divide(a,b):
  return a/b
def max_value(a,b):
  if a>b:
    return a
  else:
    return b
def calculate(func, a, b):
    return func(a, b)
def find_max(prices_list):
  max_price = prices_list[0]
  for i in prices_list:
    if i > max_price:
      max_price = i
  return max_price
def find_min(prices_list):
  min_price = prices_list[0]
  for i in prices_list:
    if i < min_price:
      min_price = i
  return min_price
def avg_(prices_list):
  total = 0
  for i in prices_list:
    total = total + i
  avg = total / len(prices_list)
  return avg
def stock_stats(prices_list):
  max_price = find_max(prices_list)
  min_price = find_min(prices_list)
  avg = avg_(prices_list)
  num = len(prices_list)
  print(f"{max_price},{min_price},{avg},{num}")
stock_stats([1,2,3,4])
def stock_stats_right(prices_list):
   return max(prices_list),min(prices_list),sum(prices_list),sum(prices_list)/len(prices_list)


# ═══════════════════════════════════════════════════
# 四, 作用域(scope)
# ═══════════════════════════════════════════════════

"x = \"全局变量\""

"def my_func():"
"    x = \"局部变量\"  # 函数内部, 不影响全局"
"    print(x)"

"my_func()   # 局部变量"
"print(x)    # 全局变量"


# global:声明要修改全局变量
"count = 0"

"def add_one():"
"    global count"
"    count += 1"

"add_one()"
"add_one()"
"print(count)  # 2"


# nonlocal:嵌套函数中修改外层变量
"def outer():"
"    n = 0"
"    def inner():"
"        nonlocal n"
"        n += 1"
"        return n"
"    return inner"

"counter = outer()"
"print(counter())  # 1"
"print(counter())  # 2"


print("\n" + "=" * 40 + "\n练习 4")

# ■ 练习 4:作用域
# 1. 定义全局变量 call_count = 0
# 2. 写一个函数 analyze_stock(name, price, pe)
#    用 global 让 call_count 每次调用 +1
#    如果 pe < 15 返回 "低估", pe < 30 返回 "合理", 否则返回 "高估"
# 3. 对以下数据调用 3 次, 打印每次结果, 最后打印 call_count

stocks_data = [("招行", 32, 5), ("茅台", 180, 30), ("宁德", 250, 50)]

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 五, Lambda 表达式(匿名函数)
# ═══════════════════════════════════════════════════

# lambda 参数: 返回值
# 相当于简写的函数

"def add(a, b):"
"    return a + b"

"add_lambda = lambda a, b: a + b"

"print(add(3, 5))           # 8"
"print(add_lambda(3, 5))    # 8"

# 实际更多是直接传, 不赋值给变量
# 配合 sorted() 最常用

"stocks = [(\"茅台\", 180), (\"招行\", 32), (\"宁德\", 250)]"

# 按价格排序
"sorted(stocks, key=lambda x: x[1])"
# [('招行', 32), ('茅台', 180), ('宁德', 250)]

"sorted(stocks, key=lambda x: x[1], reverse=True)"
# [('宁德', 250), ('茅台', 180), ('招行', 32)]

# 按名称长度排序
"sorted(stocks, key=lambda x: len(x[0]))"

# max/min 也可以用 key
"max(stocks, key=lambda x: x[1])   # ('宁德', 250)"
"min(stocks, key=lambda x: x[1])   # ('招行', 32)"

# map(函数, 可迭代对象) -- 对每个元素应用函数
# filter(函数, 可迭代对象) -- 筛选返回 True 的元素

"prices = [100, 200, 300, 50, 150]"
"list(map(lambda x: x * 2, prices))         # [200, 400, 600, 100, 300]"
"list(filter(lambda x: x > 150, prices))    # [200, 300]"


print("\n" + "=" * 40 + "\n练习 5")

# ■ 练习 5:lambda 实战
data = [("茅台", 1820, 100), ("招行", 35, 500), ("宁德", 225, 200)]
# 1. 按市值(价格 x 数量)从高到低排序, 用 lambda
# 2. 用 max + lambda 找出市值最高的股票
# 3. 用 map 提取所有股票名称
# 4. 用 filter 找出价格 > 100 的股票
# 提示: data 里每个元素是 (name, price, volume)

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 六, 综合练习 -- 股票计算器工具箱
# ═══════════════════════════════════════════════════
#
# 把今天学的函数知识全部用上

print("\n" + "=" * 50)
print("综合练习: 股票计算器工具箱")
print("=" * 50)

portfolio = [
    ("茅台", 1820.50, 100),
    ("招行", 36.80, 500),
    ("宁德", 225.00, 200),
    ("药明", 68.50, 300),
    ("腾讯", 380.00, 50),
]

# 1. 写一个函数 calc_market_value(price, shares), 返回市值
# 2. 写一个函数 calc_total(portfolio, func) -- 接受持仓列表和一个函数
#    遍历每只股票调用 func(price, shares), 累加返回总市值
# 3. 用 lambda 按市值从高到低排序
# 4. 用 filter + lambda 找出价格 > 100 的股票
# 5. 写一个函数 print_report(portfolio), 打印格式:
#   ========================
#   持仓报告
#   ========================
#   茅台: 182050.0 元
#   招行: 18400.0 元
#   宁德: 45000.0 元
#   药明: 20550.0 元
#   腾讯: 19000.0 元
#   ------------------------
#   总市值: 285000.0 元
#   股票数量: 5 只
#   ========================

# ↓ 你的代码 ↓


# ====================================================
# 今天学到的
# ====================================================
# ✅ def/return: 定义和调用函数
# ✅ 参数: 默认值, 关键字, *args, **kwargs
# ✅ 函数是一等公民: 可以赋值和传参
# ✅ 多返回值: return 多个值, 解包接收
# ✅ 作用域: global 修改全局变量, nonlocal 嵌套
# ✅ lambda: 匿名函数, 配合 sorted/max/min/map/filter
#
# 明天预告: 文件I/O + 异常处理 -- 读写股票CSV文件


#
# ════════════════════════════════════════════════════
# 阶段进度  (6阶段路线图)
# ════════════════════════════════════════════════════
#  阶段1 Python基础  ████████░░░░  正在当前阶段
#   ├─ day01 变量与类型 ✅
#   ├─ day02 列表与字典 ✅
#   ├─ day03 函数         ✅   ← 你在这里
#   ├─ day04 文件与异常   ⏳
#   ├─ day05 模块与包     ⏳
#   ├─ day06-07 综合项目  ⏳
#  阶段2 C++核心      ░░░░░░░░░░░░  下一阶段
#  阶段3 数据结构与算法 ░░░░░░░░░░░░
#  阶段4 数据库与网络  ░░░░░░░░░░░░
#  阶段5 量化入门项目  ░░░░░░░░░░░░
#  阶段6 进阶与面试    ░░░░░░░░░░░░
# ════════════════════════════════════════════════════
