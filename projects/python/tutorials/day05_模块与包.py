"""
====================================================
 Day 5 | 模块与包 + pip + datetime -- 站在巨人的肩膀上
====================================================

 目标: 学会 import 他人代码、自己写模块、安装第三方库、
       处理时间数据、操作文件路径

 对比 C++:
   - C++ 用 #include 引入头文件, Python 用 import 导入模块
   - Python 的 import 更灵活: 可以只导入需要的部分, 可以起别名
   - pip 相当于 C++ 的 vcpkg/conan, 但更简单好用
   - datetime 相当于 C++ 的 <chrono> + <ctime>

 结构: 讲一个知识点 -> 练一个 -> 再讲下一个 -> 综合

====================================================
"""

# ═══════════════════════════════════════════════════
# Day 5 依赖清单
# ═══════════════════════════════════════════════════
#
# | 依赖项 | 类型 | 首次出现 | 确认覆盖 |
# |--------|------|----------|----------|
# | list | 基础类型 | Day 02 | ✅ 列表操作 |
# | dict | 基础类型 | Day 02 | ✅ .get(), .items() |
# | str | 基础类型 | Day 01 | ✅ 字符串方法 |
# | f-string | 语法 | Day 01 | ✅ 格式化输出 |
# | def/return | 语法 | Day 03 | ✅ 函数定义 |
# | try/except | 语法 | Day 04 | ✅ 异常处理 |
# | open/with | 语法 | Day 04 | ✅ 文件操作 |
# | set | 基础类型 | Day 04 | ✅ 集合运算 |
#

# ═══════════════════════════════════════════════════
# 一, import --- 引入别人写好的功能
# ═══════════════════════════════════════════════════

# Python 自带了大量标准库(标准模块), 用 import 就能用

# --- 1.1 四种 import 写法 ---

# 写法 1: import 模块名  (最常用)
"import math"
"print(math.sqrt(16))   # 4.0"
"print(math.pi)          # 3.14159..."

# C++: #include <cmath> -> std::sqrt(16)
# Python: import math -> math.sqrt(16)

# 写法 2: from 模块名 import 具体功能  (省去模块名前缀)
"from math import sqrt, pi"
"print(sqrt(25))         # 5.0 (不用写 math.sqrt)"

# 写法 3: import 模块名 as 别名  (处理长名字)
"import math as m"
"print(m.floor(3.7))     # 3"

# 写法 4: from 模块名 import *  (不推荐! 容易名字冲突)
"# from math import *   -- 不推荐这样写"

# --- 1.2 import 的搜索路径 ---

# Python 按这个顺序找模块:
# 1. 当前脚本所在目录
# 2. PYTHONPATH 环境变量
# 3. Python 安装路径下的 site-packages
"import sys"
"print(sys.path)          # 打印搜索路径列表(很长)"


print("\n" + "=" * 40 + "\n练习 1.1")

# ■ 练习 1.1: 用 random 模块
# random 是 Python 标准库, 提供随机数功能
# 需求: 用 import random, 然后:
#   1. random.randint(1, 100) --> 随机整数
#   2. random.choice(['茅台', '招行', '腾讯']) --> 随机选一个
#   3. random.sample([...], 3) --> 随机选3个不重复的

# ↓ 你的代码 ↓


print("\n" + "=" * 40 + "\n练习 1.2")

# ■ 练习 1.2: 用 statistics 算均值
# statistics 是 Python 标准库, 提供 mean/median/stdev 等
# 需求: 给定一组收益率, 算均值和中位数

returns = [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.01]

# 用 from ... import ... 写法导入 mean 和 median
# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 二, 自定义模块 --- 把你的代码分到不同文件
# ═══════════════════════════════════════════════════

# 当代码多了(超过200行), 应该拆到多个 .py 文件里
# 任何一个 .py 文件都可以被别的 .py 文件 import

# 配套文件 day05_utils.py 里有: calculate_sharpe(), filter_stocks()

# --- 2.1 if __name__ == '__main__' ---

# 这是一个重要写法:
#   当直接运行这个 .py 时, __name__ 是 '__main__'
#   当被 import 时, __name__ 是 文件名(不含.py)
# 用途: 写测试代码在 if 块里, 被 import 时不会执行


print("\n" + "=" * 40 + "\n练习 2.1")

# ■ 练习 2.1: import 自定义模块
# 用 import day05_utils as utils 导入
# 然后:
#   1. 用 utils.calculate_sharpe(returns, rf=0.02) 算夏普比率
#   2. 用 utils.filter_stocks(prices_dict, threshold) 过滤低价股

returns = [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.01]
prices = {"茅台": 180, "招行": 35, "平安": 45, "宁德": 220, "万科": 15}

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 三, pip --- Python 的"应用商店"
# ═══════════════════════════════════════════════════

# pip 是 Python 的包管理器, 从 PyPI 下载第三方库
# 这些命令在 终端/cmd 里运行:

# 常用命令:
#   pip install 包名        安装
#   pip install 包名==版本  安装指定版本
#   pip list               查看已安装
#   pip uninstall 包名     卸载

# 后面会用到的第三方库: requests, numpy, pandas, matplotlib

# --- 3.1 查看已安装的包 ---

"from importlib.metadata import distributions"
"installed = [dist.metadata['Name'] for dist in distributions()]"
"print(f'已安装 {len(installed)} 个包')"
"print(sorted(installed)[:10])  # 前10个"


print("\n" + "=" * 40 + "\n练习 3.1")

# ■ 练习 3.1: 检查包是否已安装
# 用 try/except ImportError 检测包是否存在
# 遍历 packages_to_check, 逐个尝试 import
# 已安装 -> 打印 "[OK] xxx 已安装"
# 未安装 -> 打印 "[..] xxx 未安装, 请运行: pip install xxx"

packages_to_check = ['requests', 'numpy', 'pandas', 'matplotlib', 'flask']

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 四, datetime --- 处理时间数据
# ═══════════════════════════════════════════════════

# 量化场景: 交易日判断, 时间戳转换, 日期差计算
# C++: #include <chrono>  /  Python: from datetime import datetime

# --- 4.1 获取当前时间 ---

from datetime import datetime

"now = datetime.now()"
"print(now)                # 2026-05-31 14:30:00.123456"
"print(now.year)           # 2026"
"print(now.month)          # 5"
"print(now.day)            # 31"
"print(now.hour)           # 14"

# --- 4.2 创建指定时间 ---

"dt = datetime(2026, 6, 1, 9, 30, 0)"
"print(dt)                 # 2026-06-01 09:30:00"
"# 参数: year, month, day, hour, minute, second(可省略)"

# --- 4.3 格式化时间 (strftime) ---

"print(now.strftime('%Y-%m-%d'))          # 2026-05-31"
"print(now.strftime('%H:%M:%S'))          # 14:30:00"
"print(now.strftime('%Y年%m月%d日 %A'))    # 2026年05月31日 Sunday"

# 常用格式化符号:
# %Y - 4位年份  %m - 2位月份  %d - 2位日
# %H - 24时     %M - 分钟    %S - 秒
# %A - 星期全名  %a - 星期缩写

# --- 4.4 解析字符串 (strptime) ---

"date_str = '2026-06-01'"
"dt = datetime.strptime(date_str, '%Y-%m-%d')"
"print(dt)                 # 2026-06-01 00:00:00"

"# strptime(待解析字符串, 格式) -- 格式必须和字符串匹配"


print("\n" + "=" * 40 + "\n练习 4.1")

# ■ 练习 4.1: 时间格式化练习
# 用 now.strftime() 打印:
#   1. "今天是 2026年05月31日"
#   2. "当前时间 14:30"
#   3. "今天是 Sunday"

now = datetime.now()

# ↓ 你的代码 ↓


print("\n" + "=" * 40 + "\n练习 4.2")

# ■ 练习 4.2: 解析日期字符串
# 把 date_strings 里的字符串转成 datetime 对象, 存入列表
# 然后打印每个日期是星期几
# 提示: datetime.strptime(s, '%Y-%m-%d')

date_strings = ['2026-05-26', '2026-05-27', '2026-05-28', '2026-05-29', '2026-05-30']

# ↓ 你的代码 ↓


# --- 4.5 timedelta --- 时间差计算

"from datetime import timedelta"

"today = datetime.now()"
"one_day = timedelta(days=1)"
"yesterday = today - one_day"
"tomorrow = today + one_day"
"print(f'昨天: {yesterday.strftime(\"%Y-%m-%d\")}')"
"print(f'明天: {tomorrow.strftime(\"%Y-%m-%d\")}')"

"# 创建 timedelta"
"delta = timedelta(days=5, hours=3, minutes=30)"
"print(delta)              # 5 days, 3:30:00"

"# 两个 datetime 相减得 timedelta"
"dt1 = datetime(2026, 6, 1)"
"dt2 = datetime(2026, 5, 25)"
"diff = dt1 - dt2"
"print(diff.days)          # 7"


print("\n" + "=" * 40 + "\n练习 4.3")

# ■ 练习 4.3: 计算持股天数
# 给定买入日期和卖出日期, 算持股天数
# 1. 把字符串转成 datetime
# 2. 算日期差
# 3. 打印 "持股 X 天"

buy_date_str = '2026-05-15'
sell_date_str = '2026-05-28'

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 五, os + pathlib --- 文件和路径操作
# ═══════════════════════════════════════════════════

# --- 5.1 os 模块(传统方式) ---

import os

"print(os.getcwd())        # 当前工作目录"

"# 拼接路径"
"data_path = os.path.join('data', 'finance.csv')"
"print(data_path)          # data\\finance.csv (Windows)"

"# 检查文件是否存在"
"print(os.path.exists(data_path))   # True/False"

# --- 5.2 pathlib (现代方式, Python 3.4+) ---

# pathlib 比 os.path 更直观, 推荐使用
from pathlib import Path

"p = Path('data/finance.csv')"
"print(p.exists())         # True"
"print(p.suffix)           # .csv"
"print(p.stem)             # finance (文件名不含后缀)"
"print(p.parent)           # data (父目录)"

"# 路径拼接 -- 用 / 不是 os.path.join!"
"data_dir = Path('data')"
"csv_file = data_dir / 'finance.csv'"
"print(csv_file)           # data\\finance.csv"

"# 创建目录"
"Path('output').mkdir(exist_ok=True)"

"# 遍历目录"
"for f in Path('.').iterdir():"
"    if f.suffix == '.csv':"
"        print(f.name)     # 所有 .csv 文件"


print("\n" + "=" * 40 + "\n练习 5.1")

# ■ 练习 5.1: pathlib 实战
# 1. 检查 data/tech.csv 是否存在
# 2. 如果存在, 打印后缀名、文件大小、父目录
# 3. 创建 output/ 目录(如果不存在)
# 提示: Path('data/tech.csv') -> .exists() / .suffix / .stat().st_size / .parent

# ↓ 你的代码 ↓


print("\n" + "=" * 40 + "\n练习 5.2")

# ■ 练习 5.2: datetime + pathlib 组合
# 遍历 data/ 目录下所有 .csv 文件, 打印每个文件的最后修改时间
# 提示: p.stat().st_mtime 是时间戳, 用 datetime.fromtimestamp() 转

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 综合练习: 交易日历工具
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n综合练习")

# 综合应用: import + datetime + pathlib
#
# 背景: A 股交易规则
#   - 周一到周五交易
#   - 周末不交易
#   - 不考虑法定节假日(简化)

from datetime import datetime as dt, timedelta
from pathlib import Path

def is_trading_day(date):
    """判断某天是不是交易日(简化版: 周一~周五)"""
    return date.weekday() < 5  # 0=周一, 4=周五, 5=周六, 6=周日

def next_trading_day(date):
    """返回下一个交易日"""
    current = date + timedelta(days=1)
    while not is_trading_day(current):
        current += timedelta(days=1)
    return current

def trading_days_between(start, end):
    """返回两个日期之间的所有交易日(含start, 不含end)"""
    days = []
    current = start
    while current < end:
        if is_trading_day(current):
            days.append(current)
        current += timedelta(days=1)
    return days

# --- 教学演示 ---
today = dt.now()
print(f"今天: {today.strftime('%Y-%m-%d %A')}")
print(f"是交易日吗? {is_trading_day(today)}")
print(f"下一个交易日: {next_trading_day(today).strftime('%Y-%m-%d')}")

may_start = dt(2026, 5, 1)
may_end   = dt(2026, 6, 1)
may_trading_days = trading_days_between(may_start, may_end)
print(f"2026年5月交易日数: {len(may_trading_days)}")


# ■ 你的任务:
# 基于上面三个函数, 实现:
#
# 1. prev_trading_day(date) -- 返回上一个交易日
#
# 2. count_trading_days_until(target_date) -- 今天到目标日期还有几个交易日
#    提示: 用 dt.now().replace(hour=0, minute=0, second=0, microsecond=0) 去掉时间部分
#
# 3. 把从今天起未来60天的交易日历保存到 output/trading_calendar.txt
#    格式: "2026-06-01 (Monday)"

# ↓ 你的代码 ↓
