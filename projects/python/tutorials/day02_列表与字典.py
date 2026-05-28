"""
====================================================
 Day 2 | 列表与字典 -- Python 最核心的数据结构
====================================================

 目标: 掌握 list 和 dict,包括切片和推导式

 结构: 讲一个知识点 → 练一个 → 再讲下一个 → 最后综合练习

====================================================
"""

# ═══════════════════════════════════════════════════
# 一,list -- C++ 的 vector + 超多额外功能
# ═══════════════════════════════════════════════════

# --- 1.1 创建列表 ---

"empty_list = []                     # 空列表"
"numbers = [1, 2, 3, 4, 5]           # 整数列表"
"mixed = [1, \"你好\", 3.14, True]    # 不同类型混装(C++ 做不到)"
"nested = [[1, 2], [3, 4]]           # 嵌套列表(二维数组)"


from enum import Flag


print("\n" + "=" * 40 + "\n练习 1.1")

# ■ 练习 1.1:创建你的股票观察列表
stocks = ["贵州茅台", "招商银行", "宁德时代", "腾讯控股", "药明康德"]
print(stocks)


# --- 1.2 索引和切片(Python 的切片非常强大)---

"正索引(和 C++ 一样从 0 开始)"
"print(numbers[0])   # 1"
"print(numbers[2])   # 3"

"负索引(从末尾开始,C++ 没有)"
"print(numbers[-1])  # 5(最后一个)"
"print(numbers[-2])  # 4(倒数第二个)"

"切片 [start:end:step]"
"print(numbers[1:4])     # [2, 3, 4](左闭右开)"
"print(numbers[:3])      # [1, 2, 3]"
"print(numbers[3:])      # [4, 5]"
"print(numbers[::2])     # [1, 3, 5](步长 2)"
"print(numbers[::-1])    # [5, 4, 3, 2, 1](反转!一行搞定)"


print("\n" + "=" * 40 + "\n练习 1.2")

# ■ 练习 1.2:切片操作
prices = [100, 95, 102, 98, 110, 105, 108]
# 1. 取出前 3 个价格
# 2. 取出最后 2 个价格
# 3. 取出所有偶数索引的价格(第 0,2,4... 个)
# 4. 把 prices 反转并打印

# ↓ 你的代码 ↓
print(prices[:3])      # 前 3 个
print(prices[-2:])
print(prices[::2])
print(prices[::-1])
# --- 1.3 常用方法 ---

"prices = [100, 95, 102, 98, 110]"

"prices.append(105)          # 末尾添加"
"prices.insert(0, 90)        # 在索引 0 插入"
"last = prices.pop()         # 移除并返回最后一个"
"first = prices.pop(0)       # 移除并返回第一个"

"prices = [100, 95, 102, 98, 110]"
"prices.sort()               # 排序 → [95, 98, 100, 102, 110]"
"prices.reverse()            # 反转 → [110, 102, 100, 98, 95]"

"print(len(prices))          # 5(长度)"
"print(100 in prices)        # True(是否包含)"
"print(prices.index(102))    # 1(元素位置)"
"print(prices.count(100))    # 1(出现次数)"


print("\n" + "=" * 40 + "\n练习 1.3")

# ■ 练习 1.3:管理价格列表
prices = [98, 105, 92, 110, 95]
# 1. 末尾添加 103
# 2. 移除最后一个价格并打印它
# 3. 排序后打印
# 4. 检查 100 是否在列表中
# 5. 打印列表长度

# ↓ 你的代码 ↓
prices.append(103)
prices.pop()
print(prices)
prices.sort()
print(prices)
print(100 in prices)
print(len(prices))

# --- 1.4 列表推导式(List Comprehension)---
"Python 最优雅的特性,没有 C++ 等价物"

"squares = [i ** 2 for i in range(10)]"
"print(squares)  # [0, 1, 4, 9, ... 81]"

"带条件"
"evens = [i for i in range(20) if i % 2 == 0]"
"print(evens)  # [0, 2, 4, ... 18]"

"实战:批量处理股票价格"
"prices_str = [\"100.5\", \"98.3\", \"102.7\", \"99.1\"]"
"prices_float = [float(p) for p in prices_str]"
"high = [p for p in prices_float if p > 100]"
"print(high)  # [100.5, 102.7]"


print("\n" + "=" * 40 + "\n练习 1.4")

# ■ 练习 1.4:用推导式处理数据
raw_data = ["12.5", "15.3", "9.8", "11.0", "14.2"]
# 1. 用列表推导式转成浮点数列表
# 2. 从中筛选出大于 13 的值
raw_data_float=[float(p) for p in raw_data]
print(raw_data_float)
high_values=[p for p in raw_data_float if p >13]

# ↓ 你的代码 ↓


# --- 1.5 tuple -- 不可变的列表 ---

"# C++ 没有直接的 tuple 等价物(std::pair 只有两个元素)"
"# Python tuple 是'只读列表', 创建后不能修改"

"# 创建元组"
"t = (1, 2, 3)                # 圆括号"
"single = (42,)                # 单个元素要加逗号!"
"no_paren = 1, 2, 3            # 不加括号也能创建元组"
"print(type(no_paren))         # <class 'tuple'>"

"# 访问(和 list 一样)"
"stock_info = ('茅台', 1800.50, 100)"
"print(stock_info[0])          # '茅台'"
"print(stock_info[-1])         # 100"

"# 元组不可变"
"# stock_info[0] = '五粮液'  # TypeError"

"# 元组可以像列表一样切片"
"print(stock_info[:2])         # ('茅台', 1800.5)"

"# 元组解包(Python特色, C++17才有结构化绑定)"
"name, price, shares = stock_info"
"print(f'{name}: {price}元, {shares}股')"

"# 交换变量(用元组解包一行搞定)"
"a, b = 10, 20"
"a, b = b, a                   # 不用临时变量!"
"print(f'a={a}, b={b}')        # a=20, b=10"

"# 多个返回值本质就是返回元组"
"def get_min_max(prices):"
"    return min(prices), max(prices)  # 返回元组"
"low, high = get_min_max([95, 102, 98, 110])"
"print(f'最低:{low}, 最高:{high}')"


print("\n" + "=" * 40 + "\n练习 1.5")

# ■ 练习 1.5: tuple 实战
# 1. 创建一个元组 stock = ('腾讯', 380.00, 50)
# 2. 用索引打印股票名称和价格
# 3. 用解包把元组赋值给三个变量
# 4. 尝试修改元组的第一个元素(看看会不会报错)
# 5. 用一行代码交换 a=5, b=10 的值

# ↓ 你的代码 ↓


# --- 1.6 常用内置函数(Python 帮你写好了)---

"# C++ 要自己写循环找最大值, Python 一行搞定"

"prices = [95, 102, 98, 110, 105]"

"print(len(prices))     # 5     -- 长度(类似 C++ .size())"
"print(max(prices))     # 110   -- 最大值"
"print(min(prices))     # 95    -- 最小值"
"print(sum(prices))     # 510   -- 求和"
"sorted_asc = sorted(prices)     # [95, 98, 102, 105, 110]"
"sorted_desc = sorted(prices, reverse=True)  # [110, 105, 102, 98, 95]"

"# 注意: sorted() 不修改原列表"
"print(prices)           # 还是原来的顺序"


print("\n" + "=" * 40 + "\n练习 1.6")

# ■ 练习 1.6: 内置函数实战
data = [1800, 35, 220, 68, 380]
# 1. 用 max 找出最高价
# 2. 用 min 找出最低价
# 3. 用 sum 计算总价
# 4. 用 len 计算数量
# 5. 用 sorted + reverse=True 从高到低排序

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# ═══════════════════════════════════════════════════
# 二,dict -- C++ 的 map,但更灵活
# ═══════════════════════════════════════════════════

# --- 2.1 创建字典 ---

"empty_dict = {}"
"stock_prices = {"
"    \"贵州茅台\": 1800.50,"
"    \"招商银行\": 35.20,"
"    \"宁德时代\": 220.00,"
"    \"腾讯控股\": 380.00,"
"}"
"print(stock_prices)"


print("\n" + "=" * 40 + "\n练习 2.1")

# ■ 练习 2.1:创建你的持仓字典
# 创建一个字典 portfolio,包含:
# "贵州茅台": 100(股),"招商银行": 500,"宁德时代": 200

# ↓ 你的代码 ↓
portfolio = {
    "贵州茅台": 100,
    "招商银行": 500,
    "宁德时代": 200
}
print(portfolio)

# --- 2.2 访问和修改 ---

"print(stock_prices[\"贵州茅台\"])          # 1800.5"
"stock_prices[\"贵州茅台\"] = 1810.00       # 修改"
"stock_prices[\"药明康德\"] = 65.00         # 添加新键值对"

"安全访问(get 方法)"
"price = stock_prices.get(\"不存在的股票\")       # None(不报错)"
"price2 = stock_prices.get(\"不存在的股票\", 0)   # 0(默认值)"
"print(price, price2)"


print("\n" + "=" * 40 + "\n练习 2.2")

# ■ 练习 2.2:操作字典
portfolio = {"茅台": 100, "招行": 500}
# 1. "茅台" 的持仓改为 150
# 2. 添加新股票 "宁德" -> 200
# 3. 用 get 安全获取 "平安" 的持仓,不存在时返回 0
# 4. 删除 "招行"

# ↓ 你的代码 ↓
portfolio["茅台"] = 150
portfolio["宁德"] = 200
chicang = portfolio.get("平安", 0)
print(chicang)
del portfolio["招行"]
print(portfolio)

# --- 2.3 常用方法 ---

"print(stock_prices.keys())      # 所有键"
"print(stock_prices.values())    # 所有值"
"print(stock_prices.items())     # 所有键值对"

"遍历(日常用得最多)"
"for name, price in stock_prices.items():"
"    if price > 100:"
"        print(f\"{name}: {price}元\")"

"检查键是否存在"
"print(\"贵州茅台\" in stock_prices)   # True"

"用 not 取反"
"print(\"不存在的股票\" not in stock_prices)   # True"

"del stock_prices[\"药明康德\"]        # 删除"


print("\n" + "=" * 40 + "\n练习 2.3")

# ■ 练习 2.3:遍历并计算市值
portfolio = {"茅台": 100, "招行": 500, "宁德": 200}
prices = {"茅台": 1800, "招行": 35, "宁德": 220}
# 用 items() 遍历 portfolio,计算每只股票市值(持仓 * 价格)
# 然后打印总市值
# 预期:
#   茅台: 180000 元
#   招行: 17500 元
#   宁德: 44000 元
#   总市值: 241500 元

# ↓ 你的代码
market_value_total = 0
for stock, shares in portfolio.items():
    price = prices.get(stock, 0)
    market_value = shares * price
    market_value_total += market_value
    print(f"{stock}: {market_value} 元")
print(f"总市值: {market_value_total} 元")

print("\n" + "=" * 40 + "\n练习 2.3 附加题1")

# ■ 练习 2.3 附加题1:计算每日涨跌额
base_prices = {"茅台": 1800, "招行": 35, "宁德": 220}
close_prices = {"茅台": 1820, "招行": 34, "宁德": 230}
# 用 items() 遍历 base_prices,计算每只股票的涨跌额 = 收盘价 - 基准价
# 打印每只股票的涨跌情况
# 最后打印总涨跌额
for stock , colse_value in close_prices.items():
    base_value = base_prices.get(stock,0)
    changed_value = colse_value - base_value
    print(changed_value)

# ↓ 你的代码 ↓


print("\n" + "=" * 40 + "\n练习 2.3 附加题2")

# ■ 练习 2.3 附加题2:统计盈利股票
holdings = {"茅台": 100, "招行": 500, "宁德": 200}
cost_prices = {"茅台": 1750, "招行": 38, "宁德": 210}
current_prices = {"茅台": 1820, "招行": 34, "宁德": 230}
# 遍历 holdings,对每只股票计算:
#   成本 = cost_prices[股票] * 数量
#   当前市值 = current_prices[股票] * 数量
#   盈亏 = 当前市值 - 成本
# 找出盈利(盈亏 > 0)的股票,打印出来,最后打印盈利的股票数量

# ↓ 你的代码 ↓
# benifit_total = {}
# count = 0
# for name ,value in current_prices.items():
#     cost_prices_ = cost_prices.get(name,0)
#     benifit = (value - cost_prices_)*holdings.get(name,1)
#     print(f"{name},盈利{benifit}")
#     benifit_total[name] = benifit
# print("===================")
# for name,i in benifit_total.items() :
#     if i > 0:
#         count=count +1
#         print(f"{name}:{i}")
# print(f"盈利个数{count}个")
'''
实现二
'''
count = 0
for name, current_price in current_prices.items():
    benifit = (current_price - cost_prices.get(name,0))*holdings.get(name,1)
    if benifit > 0:
        count +=1
        print(f'{name}:{benifit}')
print(count)




print("\n" + "=" * 40 + "\n练习 2.3 附加题3")

# ■ 练习 2.3 附加题3:合并两个字典
dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"b": 20, "c": 30, "d": 40}
# 用 items() 遍历 dict_b,把 dict_b 的键值对添加到 dict_a 中
# 如果键已存在,值相加
# 打印合并后的字典
# 预期: {"a": 1, "b": 22, "c": 33, "d": 40}

# ↓ 你的代码 ↓
for name, value in dict_b.items():
    if name in dict_a :
        dict_a[name] = value + dict_a.get(name,0)
    else :
        dict_a[name] = value
print(dict_a)






# --- 2.4 字典推导式 ---

"original = {\"a\": 1, \"b\": 2, \"c\": 3}"
"reversed_dict = {v: k for k, v in original.items()}"
"print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}"

"过滤"
"filtered = {k: v for k, v in stock_prices.items() if v > 100}"

"两个列表拼成字典"
"names = [\"茅台\", \"招行\", \"宁德\"]"
"prices = [1800, 35, 220]"
"stock_dict = dict(zip(names, prices))"
"print(stock_dict)  # {'茅台': 1800, '招行': 35, '宁德': 220}"


print("\n" + "=" * 40 + "\n练习 2.4")

# ■ 练习 2.4:字典推导式实战
cities = ["北京", "上海", "深圳", "杭州"]
codes = ["BJ", "SH", "SZ", "HZ"]
# 1. 用 zip + dict 创建城市代码映射 {"北京": "BJ", ...}
# 2. 用字典推导式反转为 {"BJ": "北京", ...}
# 3. 从 city_code 字典中筛选出键长度 >= 2 的项

# ↓ 你的代码 ↓
codes_cities ={}
cities_codes = dict(zip(cities,codes))
for city , code in cities_codes.items()  :
    if len(code) >=2:
        codes_cities[code] = city
print(codes_cities)
codes_cities_2={v:c for c,v in cities_codes.items() if len(v)>=2}
print(codes_cities_2)


# ═══════════════════════════════════════════════════
# 三,range / enumerate / zip -- 遍历三剑客
# ═══════════════════════════════════════════════════

# --- range: 生成数字序列 ---

"print(list(range(10)))          # [0,1,2,...,9]"
"print(list(range(3, 10)))       # [3,4,...,9]"
"print(list(range(0, 10, 2)))    # [0,2,4,6,8]"


print("\n" + "=" * 40 + "\n练习 range")

# ■ 练习 range:用 range 打印 5, 10, 15, 20, 25
# 提示:注意起始值和步长

# ↓ 你的代码 ↓
print(list(range(5,36,5)))


# --- enumerate: 同时拿索引和值 ---

"stocks = [\"茅台\", \"招行\", \"宁德\", \"腾讯\"]"
"for i, name in enumerate(stocks):"
"    print(f\"第{i+1}只股票: {name}\")"

"for i, name in enumerate(stocks, start=1):"
"    print(f\"第{i}只股票: {name}\")"


print("\n" + "=" * 40 + "\n练习 enumerate")

# ■ 练习 enumerate:
prices = [1800, 35, 220, 380]
stocks = ["茅台", "招行", "宁德", "腾讯"]
# 用 enumerate 打印:
#   第 1 只: 茅台 = 1800 元
#   第 2 只: 招行 = 35 元
#   ...

# ↓ 你的代码 ↓
# for i , name in enumerate(stocks):
#     prices_ = prices[i]
#     print(f"第{i+1}只:{name}={prices_}")
for i ,(name,price) in enumerate(zip(stocks,prices)):
    print(f"第 {i+1} 只: {name} = {price} 元")


# --- zip: 把多个列表"拉链"在一起 ---

"names = [\"茅台\", \"招行\", \"宁德\"]"
"prices = [1800, 35, 220]"
"volumes = [30000, 50000, 20000]"

"for name, price, volume in zip(names, prices, volumes):"
"    print(f\"{name}: {price}元, 成交量={volume}\")"


print("\n" + "=" * 40 + "\n练习 zip")

# ■ 练习 zip:
tickers = ["AAPL", "GOOGL", "MSFT"]
prices_usd = [175.0, 140.0, 380.0]
# 1. 用 zip 遍历,打印每只股票的代码和价格
# 2. 用 zip + dict 创建股票代码到价格的字典

# ↓ 你的代码 ↓
for ticker , price in zip(tickers,prices_usd) :
    print(f"{ticker}:{price}")
print(dict(zip(tickers,prices_usd)))


print("\n" + "=" * 40 + "\n综合练习")

# ═══════════════════════════════════════════════════
# 综合练习 -- 股票持仓管理系统
# ═══════════════════════════════════════════════════
#
# 运用今天学过的全部知识:list 方法,切片,推导式,dict,enumerate,zip

tickers = ["茅台", "招行", "宁德", "药明", "腾讯"]
holdings = [100, 500, 200, 300, 50]
prices = [1820.50, 36.80, 225.00, 68.50, 380.00]

# 1. 用 zip 创建持仓字典 {"茅台": 100, "招行": 500, ...}
# 2. 用 zip 创建价格字典 {"茅台": 1820.50, ...}
# 3. 计算每只股票市值 = 持仓 * 价格,存入 market_value 字典
# 4. 用 items() 遍历 market_value,找出市值最高的股票
# 5. 总市值 > 300000 打印 "✅ 组合健康",否则 "⚠️ 需要加仓"
# 6. 用列表推导式找出市值 > 50000 的股票代码列表
# 7. 用切片显示持仓量前 3 大的股票
#
# 输出示例:
#   我的持仓: {'茅台': 100, '招行': 500, '宁德': 200, '药明': 300, '腾讯': 50}
#   ========= 市值报表 =========
#   茅台: 182050.0 元
#   招行: 18400.0 元
#   宁德: 45000.0 元
#   药明: 20550.0 元
#   腾讯: 19000.0 元
#   ===========================
#   总市值: 285000.0 元
#   ⚠️ 需要加仓
#   最高市值股票: 茅台 (182050.0 元)
#   高市值股票(>50000): ['茅台']
#   持仓前3: ['茅台', '招行', '宁德']

# ↓ 你的代码 ↓
market_value={}
values=[]
tickers_hodings = dict(zip(tickers,holdings))
# print(tickers_hodings)
tickers_prices = dict(zip(tickers,prices))
for name , hoding, price in zip(tickers,holdings,prices):
    value = hoding*price
    market_value[name] = value
print(market_value)
# items = list(market_value.items())
# max_ = items[0]
# tmep_max_ = items[0]
# for max_1 in items:
#     if max_1[1] > max_[1] :
#         tmep_max_ = max_
#         max_ = max_1
#         max_1 = tmep_max_
# print(max_)
total_value = 0.0
for per_vlaue in market_value.values() :
    total_value += per_vlaue
if(total_value > 300000):
    print(f"总持仓{total_value},组合健康")
else:
    print(f"总持仓{total_value},需要加仓(押韵上了)")
    for name ,value in market_value.items():
        if value >50000:
            print(f"高市值--{name}:{value}")
for i in range(0,3):
    items = list(market_value.items())
    max_ = items[0]
    for max_1 in items:
        if max_1[1] > max_[1] :
            max_ = max_1
    del market_value[max_[0]]
    print(max_)
for i in range(0,3):
    items = list(tickers_hodings.items())
    max_ = items[0]
    for max_1 in items :
        if max_1[1] > max_[1]:
            max_ = max_1
    del tickers_hodings[max_[0]]
    print(max_)
print([name for name ,value in market_value.items() if value > 50000])











# ====================================================
# 今天学到的
# ====================================================
# ✅ list:创建,索引,切片,方法,推导式
# ✅ dict:创建,访问,遍历,推导式
# ✅ range / enumerate / zip 遍历技巧
# ✅ 综合运用:用列表+字典处理持仓数据
#
# 明天预告:函数 -- 把代码封装成可复用的模块
#
#
# ════════════════════════════════════════════════════
# 阶段进度  (6阶段路线图)
# ════════════════════════════════════════════════════
#  阶段1 Python基础  ███████░░░░░  正在当前阶段
#   ├─ day01 变量与类型 ✅
#   ├─ day02 列表与字典 ✅   ← 你在这里
#   ├─ day03 函数         ⏳
#   ├─ day04 文件与异常   ⏳
#   ├─ day05 模块与包     ⏳
#   ├─ day06-07 综合项目  ⏳
#  阶段2 C++核心      ░░░░░░░░░░░░  下一阶段
#  阶段3 数据结构与算法 ░░░░░░░░░░░░
#  阶段4 数据库与网络  ░░░░░░░░░░░░
#  阶段5 量化入门项目  ░░░░░░░░░░░░
#  阶段6 进阶与面试    ░░░░░░░░░░░░
# ════════════════════════════════════════════════════
