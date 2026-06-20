"""
====================================================
 Day 6 | 综合项目: 股票数据管理器
====================================================

 目标: 综合运用 Days 01-05 所学,
      构建一个完整的股票数据处理工具

 功能: 读取CSV -> 概览统计 -> 筛选计算 -> 导出结果

 无 C++ 对比

====================================================
"""

# ═══════════════════════════════════════════════════
# 阶段1: Python 基础 (5周)
# Part 1: Python 核心 (Days 01-06, 2周)
#
# Day 01 ✅ 变量, 类型, 字符串, I/O
# Day 02 ✅ 列表, 字典, 元组, 推导式
# Day 03 ✅ 函数, 作用域, lambda
# Day 04 ✅ set, 文件 I/O, 异常处理, CSV 读写
# Day 05 ✅ 模块与包, pip, datetime, 路径操作
# Day 06 ▶ 综合项目: 股票数据管理器 (今天!)
#
# Part 2: 数据处理 (Days 07-11)
# 接下来 → NumPy 数组运算、Pandas 数据分析、可视化
# ═══════════════════════════════════════════════════

# ═══════════════════════════════════════════════════
# Day 6 依赖清单 (全部来自已教内容)
# ═══════════════════════════════════════════════════
#
# | 依赖项 | 类型 | 首次出现 | 确认覆盖 |
# |--------|------|----------|----------|
# | str/int/float | 基础类型 | Day 01 | 数值运算 |
# | f-string | 语法 | Day 01 | 格式化输出 |
# | list | 基础类型 | Day 02 | 列表操作 |
# | dict | 基础类型 | Day 02 | dict 访问 |
# | set | 基础类型 | Day 04 | 集合去重 |
# | def/return | 语法 | Day 03 | 函数定义 |
# | lambda | 语法 | Day 03 | 匿名函数 |
# | open/with | 语法 | Day 04 | 文件读写 |
# | csv.reader/writer | 标准库 | Day 04 | CSV 读写 |
# | import | 语法 | Day 05 | 模块导入 |
# | datetime | 标准库 | Day 05 | 日期处理 |
#

# 教学示例代码放字符串里, 不重复执行

import csv


# ═══════════════════════════════════════════════════
# 一, 项目介绍
# ═══════════════════════════════════════════════════

# 这个项目把 Days 01-05 学的零散知识点串起来
# 目标: 构建一个"读取 -> 分析 -> 导出"的数据处理流水线
#
# 项目中的函数:
#   prepare_data()      创建示例数据  (已写好, 直接调用)
#   read_csv()          读取 CSV      (你来写)
#   show_overview()     打印概览      (你来写)
#   filter_by_volume()  筛选数据      (你来写)
#   export_csv()        导出结果      (你来写)
#
# 数据格式 (stock_data.csv):
#   code   -> 股票代码   e.g. '000001' (平安银行)
#   date   -> 交易日期   e.g. '2026-01-05'
#   open   -> 开盘价     e.g. 12.50
#   high   -> 最高价     e.g. 12.80
#   low    -> 最低价     e.g. 12.40
#   close  -> 收盘价     e.g. 12.75
#   volume -> 交易量(股) e.g. 1580000 (158 万股)


# ═══════════════════════════════════════════════════
# 二, 准备数据 (已提供, 直接运行)
# ═══════════════════════════════════════════════════

# prepare_data() 创建 stock_data.csv
# 包含 3 只 A 股 x 5 个交易日 = 15 行行情数据
# 使用 csv.writer (Day 04 学过)

def prepare_data():
    """创建示例股票行情 CSV 文件"""
    with open('stock_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['code', 'date', 'open', 'high', 'low', 'close', 'volume'])
        # 000001 平安银行 (股价 ~12-13)
        writer.writerow(['000001', '2026-01-05', 12.50, 12.80, 12.40, 12.75, 1580000])
        writer.writerow(['000001', '2026-01-06', 12.75, 12.90, 12.55, 12.68, 1320000])
        writer.writerow(['000001', '2026-01-07', 12.68, 13.00, 12.60, 12.95, 1860000])
        writer.writerow(['000001', '2026-01-08', 12.95, 13.10, 12.80, 13.05, 2100000])
        writer.writerow(['000001', '2026-01-09', 13.05, 13.20, 12.90, 13.15, 1950000])
        # 000002 万科A (股价 ~8-9)
        writer.writerow(['000002', '2026-01-05', 8.20, 8.35, 8.15, 8.28, 2200000])
        writer.writerow(['000002', '2026-01-06', 8.28, 8.40, 8.20, 8.35, 1850000])
        writer.writerow(['000002', '2026-01-07', 8.35, 8.50, 8.30, 8.42, 2400000])
        writer.writerow(['000002', '2026-01-08', 8.42, 8.55, 8.35, 8.50, 1980000])
        writer.writerow(['000002', '2026-01-09', 8.50, 8.60, 8.40, 8.55, 2600000])
        # 000651 格力电器 (股价 ~35-37)
        writer.writerow(['000651', '2026-01-05', 35.20, 35.80, 35.00, 35.60, 890000])
        writer.writerow(['000651', '2026-01-06', 35.60, 36.20, 35.40, 36.10, 950000])
        writer.writerow(['000651', '2026-01-07', 36.10, 36.50, 35.80, 36.30, 1100000])
        writer.writerow(['000651', '2026-01-08', 36.30, 36.80, 36.10, 36.60, 1020000])
        writer.writerow(['000651', '2026-01-09', 36.60, 37.00, 36.40, 36.80, 1250000])


# ═══════════════════════════════════════════════════
# 三, 分步实现 --- 4 个练习
# ═══════════════════════════════════════════════════

# --- 3.1 用 csv.DictReader 读取 CSV ---

# csv.reader (Day 04 学的): 每行返回列表, 用下标访问
#   row[0] -> '000001', row[4] -> '12.75'
# 列一多 row[4] 容易搞混——哪个是 close 哪个是 high?
#
# csv.DictReader: 每行返回字典, 用列名访问, 不会弄混
#   row['code']  -> '000001'
#   row['close'] -> '12.75'
#
# csv.DictReader(f, fieldnames=None, delimiter=','):
#   f           -> 文件对象 (open() 返回的)
#   fieldnames  -> 列名列表; 默认 None 表示用 CSV 第一行当列名
#   delimiter   -> 分隔符, 默认 ','
#   返回        -> 迭代器, 每次 yield 一个 dict
#   量化场景: 股票数据列多(open/high/low/close/volume),
#            用列名比用下标可靠得多
#
"with open('stock_data.csv', 'r', encoding='utf-8') as f:"
"    reader = csv.DictReader(f)"
"    for row in reader:"
"        print(row['code'], row['close'])"


print("\n" + "=" * 40 + "\n练习 3.1: 读取 CSV")

# ■ 练习 3.1: 读取 CSV
# 实现 read_csv(filepath) 函数, 读取 CSV 返回 list[dict].
#
# 参数:
#   filepath: str, CSV 文件路径
# 返回:
#   list[dict], 每行一个 dict, 列名是 dict 的 key
#
# 步骤:
#   1. with open(filepath, 'r') 打开
#   2. csv.DictReader(f) 创建读取器
#   3. list(reader) 把迭代器转成列表, 返回

# ↓ 你的代码 ↓
def read_csv(filepath):
    with open(filepath , 'r' ,encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)




# --- 3.2 数据概览 ---

# 拿到数据第一件事: 看数据长什么样
#
# len(data)   -> 总记录数
# set + for/推导式 -> 不重复的股票代码
# min/max     -> 日期范围 (字符串可以直接比大小)
# sum / len   -> 计算平均值
#   (close 是字符串, 需要先转成 float)
#
"total = len(data)  # 15 行"
"codes = {row['code'] for row in data}  # {'000001', '000002', '000651'}"

print("\n" + "=" * 40 + "\n练习 3.2: 数据概览")

# ■ 练习 3.2: 数据概览
# 实现 show_overview(data) 函数, 打印数据概览, 不返回.
#
# 参数:
#   data: list[dict], 股票数据
#
# 打印内容 (用 f-string):
#   "总记录数: 15"
#   "股票种类: 3"
#   "日期范围: 2026-01-05 ~ 2026-01-09"
#   "平均收盘价: xx.xx"
#
# 提示:
#   - 种类: {row['code'] for row in data} 取 set, 然后 len()
#   - 日期范围: [row['date'] for row in data] 取全部日期, min/max
#   - 平均收盘价: sum(float(row['close']) for row in data) / len(data)
#     保留 2 位小数: f"{avg:.2f}"

# ↓ 你的代码 ↓
def show_overview(data):
    print(f"总共记录数:{len(data)}")
    stock_set = set(row['code'] for row in data)
    print(f'股票种类:{len(stock_set)}')
    time_set = set(row['date'] for row in data)
    print(f"日期范围:{min(time_set)}~{max(time_set)}")
    close_price_avg = sum(float(row['close']) for row in data)/len(data)
    print(f"平均收盘价{close_price_avg:.2f}")


# --- 3.3 按交易量筛选 ---

# 筛选是数据处理核心操作.
# 例如: 只看交易量大的股票 —— 流动性好, 适合量化策略.
#
# 列表推导式筛选 (复习):
"filtered = [row for row in data if int(row['volume']) > 2000000]"
# volume 是字符串, 转 int 再比较

print("\n" + "=" * 40 + "\n练习 3.3: 按交易量筛选")

# ■ 练习 3.3: 按交易量筛选
# 实现 filter_by_volume(data, min_vol) 函数.
#
# 参数:
#   data:    list[dict], 股票数据
#   min_vol: int, 最小交易量 (股)
# 返回:
#   list[dict], 交易量 > min_vol 的记录
#
# 用列表推导式, volume 转 int 再比较

# ↓ 你的代码 ↓
def filter_by_volume(data, min_vol):
    stock_filtered = list(row for row in data if int(row['volume']) > min_vol)
    return stock_filtered


# --- 3.4 用 csv.DictWriter 导出 CSV ---

# csv.writer (Day 04): 用列表写, writerow(['000001', '12.75'])
# csv.DictWriter: 用字典写, 自动匹配列名, 更直观
#
# csv.DictWriter(f, fieldnames):
#   f           -> 文件对象
#   fieldnames  -> list[str], 指定列顺序和哪些列被写入
#   方法:
#     .writeheader()  -> 写表头行 (用 fieldnames 的内容)
#     .writerow(dict) -> 写一行数据 (dict 的 key 对应列名)
#
"with open('output.csv', 'w', newline='', encoding='utf-8') as f:"
"    fieldnames = ['code', 'date', 'close', 'volume']"
"    writer = csv.DictWriter(f, fieldnames=fieldnames)"
"    writer.writeheader()"
"    writer.writerow({'code': '000001', 'date': '2026-01-05',"
"                     'close': '12.75', 'volume': '1580000'})"

print("\n" + "=" * 40 + "\n练习 3.4: 导出 CSV")

# ■ 练习 3.4: 导出 CSV
# 实现 export_csv(data, filepath) 函数, 写入 CSV 文件, 不返回.
#
# 参数:
#   data:     list[dict], 要导出的数据
#   filepath: str, 输出文件路径
#
# 步骤:
#   1. data[0].keys() 拿到列名列表, 作为 fieldnames
#   2. with open(filepath, 'w', newline='') 打开文件
#   3. csv.DictWriter(f, fieldnames=fieldnames)
#   4. writeheader() 写表头
#   5. 遍历 data, 逐个 writerow(row)

# ↓ 你的代码 ↓
def export_csv(data,filepath):
    fieldnames = data[0].keys()
    with open(filepath,'w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


# ═══════════════════════════════════════════════════
# 综合练习: 完整工作流
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n综合练习")

# ■ 综合练习: 完整工作流
# 写一个 main() 函数完成整个数据处理流程:
#
#   1. 调用 prepare_data() 生成 stock_data.csv
#   2. 用 read_csv 读取 stock_data.csv
#   3. 用 show_overview 打印概览
#   4. 用 filter_by_volume 筛选交易量 > 2_000_000 的记录
#   5. 用 export_csv 将筛选结果写到 filtered_output.csv
#   6. 再 read_csv(filtered_output.csv) + show_overview 验证
#
# 最后调用 main() 启动.
#
# 提示:
#   - Python 里 2_000_000 是合法的写法, 等价于 2000000
#   - fieldnames 可以从 data[0].keys() 拿到

# ↓ 你的代码 ↓
def main():
    prepare_data()
    data = read_csv('stock_data.csv')
    show_overview(data)
    data_filtered = filter_by_volume(data, 2_000_000)
    export_csv(data_filtered,'filtered_output.csv')
    data_final = read_csv('filtered_output.csv')
    show_overview(data_final)
main()
