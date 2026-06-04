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
interet_set = set()
print(set(tickers))


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
portfolio_set.add("平安")
portfolio_set.discard("万科")
# 我自己的测试
# portfolio_set.remove("万科")
print("茅台" in portfolio_set)
print(len(portfolio_set))




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
print(sector_A | sector_B)
print(sector_A & sector_B)
print(sector_A - sector_B)
print("茅台" in sector_B)


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
data = {s[0] for s in raw_data}
data_high = { s[0] for s in raw_data if s[1] > 100 }
print(data_high)


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
def safe_divide(a:float,b:float)->float:
    try:
        result = a /b
        return result
    except ZeroDivisionError:
        print("除数为零")
        return 0
def get_stock_price(data ,name : str):
    try:
        return data[name]
    except KeyError :
        return 0

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
try:
    print(data["宁德"])
except KeyError as e:
    print(f"缺少键{e}")
try:
    print(prices_list[5])
except IndexError :
    print("下标不存在")

# ═══════════════════════════════════════════════════
# 三, 文件 I/O -- 读写数据
# ═══════════════════════════════════════════════════

# --- 3.1 写文件 ---
# C++对比: ofstream f("output.txt"); f << "data" << endl; f.close();
# Python: with open(...) as f: auto-manages file lifecycle, no manual close

# ── open() 参数拆解 ──
# open(文件路径, 模式, encoding=编码)
#   1. 第一个参数 'output.txt'  -> 文件名(不存在会创建)
#   2. 第二个参数 'w'           -> 模式: w=写入(清空重写) a=追加 r=读取
#   3. encoding='utf-8'         -> 指定UTF-8编码存中文, Windows默认gbk会乱码
#   -> 返回值是一个文件对象, 用 as f 绑定给变量名 f

# ── with 语句拆解 ──
# with open(...) as f:
#     f.write(...)
#   with 块结束时 -> 自动调用 f.close() 关文件
#   就算里面代码报错了, 文件也会被关掉, 不会漏关

"# 写文件(w = write, 清空重写)"
"with open('output.txt', 'w', encoding='utf-8') as f:"
"    # f.write('字符串') -> 把字符串写进文件"
"    # 注意: '\\n' 是换行符, 不写的话所有内容会粘在一行"
"    f.write('股票名称,价格,数量\\n')"
"    f.write('茅台,1800,100\\n')"
"    f.write('招行,35,500\\n')"

"# 追加(a = append, 在末尾续写, 不清空)"
"with open('output.txt', 'a', encoding='utf-8') as f:"
"    f.write('宁德,225,200\\n')"

# ── w vs a 区别 ──
# 第一次 with('w'): 创建/清空文件, 写3行
# 第二次 with('a'): 打开已有文件, 在末尾加1行, 原来3行还在
# 最终文件内容:
#   股票名称,价格,数量
#   茅台,1800,100
#   招行,35,500
#   宁德,225,200


print("\n" + "=" * 40 + "\n练习 3.1")

# ■ 练习 3.1: 写文件
# 1. 用 w 模式创建 portfolio.txt, 写入三行你喜欢的股票数据
#    (股票名,价格,数量 格式, 每行一条)
# 2. 再用 a 模式追加一行新股票

# 提示:
# - 第一个 with 用 'w' -> 文件不存在会新建, 存在就清空
# - 第二个 with 用 'a' -> 保留原有内容, 末尾加一行
# - 每行结尾别忘了 \n
# - 写完后去文件管理器看看 portfolio.txt 是不是长这样

# ↓ 你的代码 ↓
with open("projects\python\projects\study_resources\portfolio.txt" , "w", encoding="utf-8") as f:
    f.write("股票名,价格,数量\n")
    f.write("腾讯,100,500\n")
    f.write("中芯国际,200,300\n")
    f.write("工商银行,100,10000\n")
with open("projects\python\projects\study_resources\portfolio.txt",'a',encoding="utf-8") as f:
    f.write("长江电力,300,200\n")


# --- 3.2 读文件 ---
# C++对比: ifstream f("output.txt"); f >> line; f.close();

# ── f.read() 读取全部内容 ──
"# .read() -> 一次性读取整个文件内容, 返回字符串"
"with open('output.txt', 'r', encoding='utf-8') as f:"
"    content = f.read()     # 整个文件变成一个字符串"
"    print(content)         # 直接打印出来"

# ── for line in f 逐行读取(推荐, 省内存) ──
"# for line in f -> 逐行读取, 一次只读一行, 大文件也不怕"
"with open('output.txt', 'r', encoding='utf-8') as f:"
"    for line in f:              # 每次循环读一行"
"        line = line.strip()     # strip() 去掉行尾的 \\n 和前后空格"
"        print(f'行: {line}')"

# ── .read() vs for 循环 区别 ──
# .read()     -> 一口气读完, 适合小文件(一次性读完再处理)
# for line in f -> 逐行读, 适合大文件(读一行处理一行, 不占内存)

# ── .strip() 的作用 ──
# .read() 读出来的 '茅台,1800,100\n'
# .strip() 去掉末尾 \n -> '茅台,1800,100' 干净了
# 不然打印出来会多空行

# ── next() 跳过表头 ──
# next(迭代器) -> 跳过第一行(表头), 从第二行开始循环
# 读 CSV 时第一行往往是 '名称,价格,数量' 这种表头, 不是数据
"with open('stocks.csv', 'r', encoding='utf-8') as f:"
"    reader = csv.reader(f)"
"    next(reader)              # 跳过第一行表头"
"    for row in reader:        # 从第二行开始读"
"        print(row)"


print("\n" + "=" * 40 + "\n练习 3.2")

# ■ 练习 3.2: 读文件
# 1. 用 r 模式打开刚才写的 portfolio.txt
# 2. 逐行读取并打印(记得 strip 掉换行符)
# 3. 在循环里加个计数器, 统计总行数

# 提示:
# - 模式用 'r'(只读), 不指定默认也是 'r'
# - for line in f: 时 line 末尾有 '\n', 用 strip() 去掉
# - 计数: 在 for 外面设 count = 0, 每读一行 count += 1

# ↓ 你的代码 ↓
with open("projects\python\projects\study_resources\portfolio.txt", 'r',encoding='utf-8') as f:
    count = 0
    for line in f:
        line = line.strip()
        count +=1
        print(f"{line}")
    print(f"总行数{count}")


# --- 3.3 CSV 文件处理(标准库) ---
# CSV = Comma-Separated Values, 逗号分隔值, 股票数据常用格式
# import csv -> 标准库, 不需要 pip install

import csv

# ── 写 CSV ──
"# csv.writer(f) -> 创建一个 CSV 写入器, 绑定到文件 f"
"# newline=''    -> 防止 csv 模块在 Windows 上多写空行(固定写法)"
"with open('stocks.csv', 'w', newline='', encoding='utf-8') as f:"
"    writer = csv.writer(f)"  # 创建写入器
"    # .writerow([列表]) -> 把列表写成一行的各列"
"    writer.writerow(['名称', '价格', '数量'])  # 表头"
"    writer.writerow(['茅台', 1800, 100])      # 数据行"
"    writer.writerow(['招行', 35, 500])"

# ── 读 CSV ──
"# csv.reader(f) -> 创建一个 CSV 读取器, 逐行返回列表"
"with open('stocks.csv', 'r', encoding='utf-8') as f:"
"    reader = csv.reader(f)"  # 创建读取器"
"    for row in reader:       # 每行是一个列表"
"        print(row)           # ['茅台', '1800', '100']"

# ── csv.writer 和普通 f.write 的区别 ──
# f.write('茅台,1800,100\n')            -> 自己拼逗号和换行
# writer.writerow(['茅台', 1800, 100])  -> csv 模块帮你加逗号和换行
# 而且 csv 遇到值里有逗号时会自动加引号, 比如 '价格,1' -> "价格,1"
# 所以推荐用 csv 模块, 比自己拼字符串可靠


print("\n" + "=" * 40 + "\n练习 3.3")

# ■ 练习 3.3: CSV 读写
# 1. 创建 stocks.csv, 包含 5 只股票(名称, 价格, 数量)
# 2. 读取 stocks.csv, 计算每只股票的市值 = 价格 * 数量
# 3. 把结果(名称, 市值)写入 market_value.csv

# 提示:
# - 写 CSV 用 csv.writer + writerow, 记得 newline=''
# - 读 CSV 用 csv.reader, row[1] 是价格, row[2] 是数量
# - 注意: 读出来的数字是字符串, 用 int() 转整数再计算
# - 计算后写 market_value.csv, 含表头: ['名称', '市值']

# ↓ 你的代码 ↓
with open('stocks.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['名称', '价格', '数量'])
    writer.writerow(['贵州茅台', 1800, 100])
    writer.writerow(['招商银行', 35, 500])
    writer.writerow(['宁德时代', 225, 200])
    writer.writerow(['中信证券', 20, 1000])
    writer.writerow(['长江电力', 28, 800])
# with open('market_value.csv','w',newline='',encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['名称','市值'])
results = [['名称', '市值']]
with open('stocks.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        market_value = int(row[1]) * int(row[2])
        # with open("market_value.csv",'a',newline='',encoding='utf-8') as h:
        #     writer = csv.writer(h)
        #     writer.writerow([row[0], market_value])
        results.append([row[0], str(market_value)])
with open('market_value.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(results)




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
# 运行: python projects/python/setup_day04_data.py
# 这会生成以下三个 CSV 文件:
"""
white_wine.csv          finance.csv           tech.csv
名称,代码               名称,代码             名称,代码
茅台,600519             招行,600036           腾讯,00700
五粮液,000858           平安,601318           阿里,09988
泸州老窖,000568         兴业,601166           海康威视,002415
洋河股份,002304         茅台,600519           中兴通讯,000063
"""


# ↓ 你的综合代码 ↓
def load_stocks(filename):
    stock_set = set()
    try:
        with open(filename,'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                stock_set.add(row[1])
        return stock_set
    except FileNotFoundError :
        return set()
stock_set_1 = load_stocks('white_wine.csv')
stock_set_2 = load_stocks('tech.csv')
stock_set_3 = load_stocks('finance.csv')

# 计算
sets = {'白酒': stock_set_1, '科技': stock_set_2, '金融': stock_set_3}

all_stocks   = stock_set_1 | stock_set_2 | stock_set_3  # 并集
common       = stock_set_1 & stock_set_2 & stock_set_3  # 三板块交集
only_wine    = stock_set_1 - stock_set_2 - stock_set_3  # 只属于白酒
wine_finance = stock_set_1 & stock_set_3                # 白酒 ∩ 金融

# 写 report.txt
with open('report.txt','w',newline='',encoding='utf-8') as f :
    for name ,s in sets.items():
        f.write(f"{name}板块{len(s)}只股票\n")
    f.write(f"一共有{len(all_stocks)}只股票\n")
    f.write(f"交集是{common}\n")
    f.write(f"只在白酒{only_wine}\n")
    f.write(f"白酒和金融{wine_finance}\n")
print('报告已写入 report.txt')






# ═══════════════════════════════════════════════════
# 今天学到的
# ═══════════════════════════════════════════════════
# ✅ set: 创建, 增删, 交并差运算, 推导式
# ✅ 异常: try/except/else/finally
# ✅ 文件: open/with/close, 读/写/追加, CSV
# ✅ 四大基础类型全部覆盖: list/dict/tuple/set
#
# 明天预告: 模块与包 -- 组织多文件项目
#
# 🔗 AI 工程参考: Day 08 学 NumPy 时, 翻 _ai_ref
#    Phase 1 线性代数/向量/矩阵运算的 code/ 配合理解
#    _ai_ref/phases/01-math-foundations/
