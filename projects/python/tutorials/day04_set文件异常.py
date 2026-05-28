"""
====================================================
 Day 4 | set + 文件I/O + 异常处理 -- 攻守兼备
====================================================

 目标: 掌握 set 集合运算, 文件读写, 异常保护

 对比 C++:
   - C++ 有 std::set (红黑树) 和 std::unordered_set (哈希表)
   - Python set 是哈希表实现, 增删查 O(1)
   - 文件操作 Python 比 C++ 简洁很多 (with 语句替代手动 fstream)
   - 异常处理 Python 的 try/except 比 C++ try/catch 更灵活

 结构: 讲一个知识点 -> 练一个 -> 综合

====================================================
"""

# ═══════════════════════════════════════════════════
# Day 4 依赖清单
# ═══════════════════════════════════════════════════
#
# | 依赖项 | 类型 | 首次出现 | 确认覆盖 |
# |--------|------|----------|----------|
# | list | 基础类型 | Day 02 | 列表推导式, 切片 |
# | dict | 基础类型 | Day 02 | .get(), .items() |
# | tuple | 基础类型 | Day 02 | 元组解包 |
# | set | 基础类型 | Day 04(本 day) | 交并差运算 |
# | len() | 内置函数 | Day 02 | 长度 |
# | in | 运算符 | Day 02 | 成员检查 |
# | open/with | 语法 | Day 04(本 day) | 文件读写 |
# | try/except | 语法 | Day 04(本 day) | 异常处理 |
# | csv | 标准库 | Day 04(本 day) | csv.reader/writer |
#

# ═══════════════════════════════════════════════════
# 一, set 集合 -- Python 的数学集合
# ═══════════════════════════════════════════════════

# --- 1.1 创建 set ---

# C++: std::set<int> s = {1, 2, 3};
"empty_set = set()          # 空集合(注意: {} 是空字典!)"
"stock_set = {'茅台', '招行', '宁德', '腾讯'}"
"print(stock_set)           # 无序"

# 从列表去重创建
"codes = ['000001', '600519', '000001', '600036', '600519']"
"unique_codes = set(codes)"
"print(unique_codes)        # 重复没了!"


print("\n" + "=" * 40 + "\n练习 1.1")

# ■ 练习 1.1: 创建股票集合
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AAPL', 'TSLA', 'GOOGL']
# 1. 创建一个 set, 包含 5 只你感兴趣的股票代码
# 2. 用 set(tickers) 去重

# ↓ 你的代码 ↓


# --- 1.2 set 基本操作(增删查) ---

"stock_set = {'茅台', '招行', '宁德', '腾讯'}"

"stock_set.add('药明')       # 添加"
"stock_set.remove('招行')    # 删除(不存在报错)"
"stock_set.discard('平安')   # 安全删除(不存在不报错)"

"print('茅台' in stock_set)  # True"
"print(len(stock_set))       # 大小"

"# 随机弹出"
"popped = stock_set.pop()"
"print(f'弹出了: {popped}')"

"stock_set.clear()"


print("\n" + "=" * 40 + "\n练习 1.2")

# ■ 练习 1.2: 管理股票池
portfolio_set = {'茅台', '招行', '宁德', '腾讯', '药明'}
# 1. 添加 '平安'
# 2. 用 discard 安全删除 '万科'
# 3. 检查 '茅台' 是否还在
# 4. 打印集合大小

# ↓ 你的代码 ↓


# --- 1.3 集合运算(核心!) ---

"A = {'茅台', '招行', '宁德', '腾讯'}"
"B = {'茅台', '药明', '恒瑞', '腾讯'}"

"print(A | B)   # 并集"
"print(A & B)   # 交集: {'茅台', '腾讯'}"
"print(A - B)   # 差集(在A不在B)"
"print(A ^ B)   # 对称差集"

"# 子集关系"
"C = {'茅台', '腾讯'}"
"print(C.issubset(A))    # True"
"print(A.issuperset(C))  # True"

"# 实战: 共同持仓"
"common = A & B"
"print(f'共同持仓: {common}')"


print("\n" + "=" * 40 + "\n练习 1.3")

# ■ 练习 1.3: 集合运算实战
sector_A = {'茅台', '五粮液', '泸州老窖', '洋河'}
sector_B = {'招行', '平安', '兴业', '茅台'}
# 1. 并集(所有股票)
# 2. 交集(同时属于两个板块)
# 3. 差集(只在白酒不在金融)
# 4. 检查 '茅台' 是否在 sector_B 中

# ↓ 你的代码 ↓


# --- 1.4 集合推导式 ---

"numbers = [10, 15, 20, 25, 30, 35, 40]"
"even_set = {n for n in numbers if n % 2 == 0}"
"print(even_set)  # {40, 10, 20, 30}"

"# 从列表提取代码到集合(自动去重)"
"stocks = [('茅台', 180), ('招行', 35), ('宁德', 220), ('茅台', 180)]"
"codes_set = {s[0] for s in stocks}"
"print(codes_set)"


print("\n" + "=" * 40 + "\n练习 1.4")

# ■ 练习 1.4: 推导式处理数据
raw_data = [
    ('茅台', 1820, 100), ('招行', 35, 500),
    ('宁德', 225, 200), ('茅台', 1820, 100),
    ('药明', 68, 300),
]
# 1. 用集合推导式提取所有股票名称(去重)
# 2. 找出价格 > 100 的股票名称

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 二, 异常处理 -- 程序的安全带
# ═══════════════════════════════════════════════════

# C++: try { ... } catch (const exception& e) { ... }
# Python: try: ... except Exception as e: ...

# --- 2.1 try/except 基础 ---

"try:"
"    num = int(input('请输入一个数字: '))"
"    result = 100 / num"
"    print(f'结果是: {result}')"
"except ValueError:"
"    print('输入的不是有效数字')"
"except ZeroDivisionError:"
"    print('不能除以零')"

# 捕获特定异常
"try:"
"    prices = {'茅台': 1800}"
"    print(prices['招商'])   # KeyError"
"except KeyError as e:"
"    print(f'缺少键: {e}')"

# else 和 finally
"try:"
"    f = open('data.csv', 'r')"
"except FileNotFoundError:"
"    print('文件不存在')"
"else:"
"    print('读取成功')"
"finally:"
"    print('清理完成')"


print("\n" + "=" * 40 + "\n练习 2")

# ■ 练习 2: 异常处理实战
# 1. 写 safe_divide(a, b), 除零返回 None
# 2. 写 get_stock_price(data, name), 键不存在返回 0

# ↓ 你的代码 ↓


# --- 2.2 常见异常类型 ---

"""
异常类型          | 什么时候发生
ValueError       | int('abc')
KeyError         | d['不存在的键']
IndexError       | lst[100]
FileNotFoundError| open('nope.csv')
ZeroDivisionError| 1/0
TypeError        | '1' + 1
"""


print("\n" + "=" * 40 + "\n练习 2.2")

# ■ 练习 2.2: 捕获多种异常
data = {'茅台': 1800, '招行': 35}
prices_list = [100, 200, 300]
# 1. try 从 data 获取 '宁德' 的价格, 捕获 KeyError
# 2. try 打印 prices_list[5], 捕获 IndexError

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 三, 文件 I/O -- 读写数据
# ═══════════════════════════════════════════════════

# --- 3.1 写文件 ---

"with open('output.txt', 'w', encoding='utf-8') as f:"
"    f.write('股票名称,价格,数量\n')"
"    f.write('茅台,1800,100\n')"
"    f.write('招行,35,500\n')"

"# 追加"
"with open('output.txt', 'a', encoding='utf-8') as f:"
"    f.write('宁德,225,200\n')"


print("\n" + "=" * 40 + "\n练习 3.1")

# ■ 练习 3.1: 写文件
# 1. 创建 portfolio.txt
# 2. 写入三行股票数据
# 3. 追加一行

# ↓ 你的代码 ↓


# --- 3.2 读文件 ---

"# 读取整个文件"
"with open('output.txt', 'r', encoding='utf-8') as f:"
"    content = f.read()"
"    print(content)"

"# 逐行读取"
"with open('output.txt', 'r', encoding='utf-8') as f:"
"    for line in f:"
"        line = line.strip()"
"        print(f'行: {line}')"


print("\n" + "=" * 40 + "\n练习 3.2")

# ■ 练习 3.2: 读文件
# 1. 读取 portfolio.txt
# 2. 逐行打印(去掉换行符)
# 3. 统计总行数

# ↓ 你的代码 ↓


# --- 3.3 CSV 文件处理 ---

import csv

# 写 CSV
"with open('stocks.csv', 'w', newline='', encoding='utf-8') as f:"
"    writer = csv.writer(f)"
"    writer.writerow(['名称', '价格', '数量'])"
"    writer.writerow(['茅台', 1800, 100])"
"    writer.writerow(['招行', 35, 500])"

# 读 CSV
"with open('stocks.csv', 'r', encoding='utf-8') as f:"
"    reader = csv.reader(f)"
"    for row in reader:"
"        print(row)"


print("\n" + "=" * 40 + "\n练习 3.3")

# ■ 练习 3.3: CSV 读写
# 1. 创建 stocks.csv (5只股票)
# 2. 读取并计算每只股票市值
# 3. 结果写入 market_value.csv

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 四, 综合练习 -- 股票池分析工具
# ═══════════════════════════════════════════════════

print("\n" + "=" * 50)
print("综合练习: 股票池分析工具")
print("=" * 50)

# 1. 写 load_stocks(filename), 返回股票代码 set
#    - 文件不存在时捕获异常, 返回空 set
# 2. 从三个板块文件读取到三个 set
# 3. 计算: 各板块数量, 并集, 交集, 差集
# 4. 结果写入 report.txt

# 先创建示例数据
with open('white_wine.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '代码'])
    writer.writerow(['茅台', '600519'])
    writer.writerow(['五粮液', '000858'])
    writer.writerow(['泸州老窖', '000568'])
    writer.writerow(['洋河', '002304'])

with open('finance.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '代码'])
    writer.writerow(['招行', '600036'])
    writer.writerow(['平安', '601318'])
    writer.writerow(['兴业', '601166'])
    writer.writerow(['茅台', '600519'])

with open('tech.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '代码'])
    writer.writerow(['腾讯', '00700'])
    writer.writerow(['阿里', '09988'])
    writer.writerow(['茅台', '600519'])


# ↓ 你的综合代码 ↓


# ═══════════════════════════════════════════════════
# 今天学到的
# ═══════════════════════════════════════════════════
# ✅ set: 创建, 增删, 交并差运算, 推导式
# ✅ 异常: try/except/else/finally
# ✅ 文件: open/with/close, 读/写/追加, CSV
# ✅ 四大基础类型全部覆盖: list/dict/tuple/set
#
# 明天预告: 模块与包 -- 组织多文件项目
