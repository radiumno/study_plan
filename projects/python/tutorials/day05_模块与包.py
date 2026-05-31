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

# 写 Python 不需要从零造轮子. 标准库(随 Python 安装自带)提供了大量现成的功能.
# 别人写好的叫"模块(module)", 用 import 就能拿来用.
# 这跟 C++ 的 #include 是一个思想: 把别人写好的代码拉进来.

# --- 1.1 四种 import 写法 ---

# 【写法 1: import 模块名】
# 最常用, 最推荐的写法. 导入整个模块, 用"模块名.函数名"调用.
# C++ 类比: #include <cmath> 之后用 std::sqrt(16)
# Python 类比: import math 之后用 math.sqrt(16)

"import math"

# math.sqrt(16):
#   math   -> 模块名, 告诉 Python 去 math 模块里找
#   .      -> 点号, Python 的成员访问符, 跟 C++ 的 :: 作用一样
#   sqrt   -> 函数名, square root 的缩写, 算平方根
#   16     -> 参数, 求 16 的平方根
#   返回   -> 4.0 (float 类型)
# 量化场景: 算波动率时需要对方差开根号, sqrt 就是干这个的
"print(math.sqrt(16))   # 4.0"

# math.pi:
#   这是 math 模块里的一个常量(float), 圆周率 π = 3.1415926...
#   量化场景: 期权定价(Black-Scholes 公式)要用到 π
"print(math.pi)          # 3.14159..."

# 【写法 2: from 模块名 import 具体功能】
# 只导入你需要的函数/变量, 调用时不用写模块名前缀.
# C++ 类比: using std::sqrt; 之后可以直接写 sqrt(25)
# 什么时候用: 当你反复调用同一个函数时, 省去前缀写起来更方便

"from math import sqrt, pi"
"print(sqrt(25))         # 5.0 (不用写 math.sqrt)"

# 【写法 3: import 模块名 as 别名】
# 给模块起个短名字. 常用标准库缩写:
#   import numpy as np
#   import pandas as pd
#   import matplotlib.pyplot as plt
# 什么时候用: 模块名太长, 或者有命名冲突

"import math as m"
"print(m.floor(3.7))     # 3"

# math.floor(3.7):
#   floor -> 向下取整(地板除), 不管小数多少都往小取整
#   3.7   -> 返回 3
#   C++ 类比: std::floor(3.7)

# 【写法 4: from 模块名 import *  (不推荐!)】
# 导入模块里所有内容, 你就不用写模块名前缀了.
# 为什么不推荐: 如果有两个模块都有同名函数, 后面的会覆盖前面的, 很难排查 bug
"# from math import *   -- 不推荐这样写"

# --- 1.2 import 的搜索路径 ---

# 当你写 import xxx 时, Python 按这个顺序找 xxx 模块:
# 1. 当前脚本所在目录(最先找到就用它)
# 2. PYTHONPATH 环境变量指定的目录
# 3. Python 安装路径下的 site-packages (pip 安装的第三方库在这)
# 这就是为什么我们后面要 cd 到 tutorials/ 目录再运行: 确保 Python 能找到我们的 day05_utils.py

"import sys"
"print(sys.path)          # 打印搜索路径列表(很长)"


print("\n" + "=" * 40 + "\n练习 1.1")

# ■ 练习 1.1: 用 random 模块
# random 是 Python 标准库, 提供随机数功能.
# 量化场景: 蒙特卡洛模拟、随机抽样、回测时随机选择时间段都需要随机数.
#
# 需求: 用 import random, 然后:
#   1. random.randint(1, 100) --> 随机整数(1到100之间)
#       randint(a, b): 返回 a <= N <= b 的随机整数, 包含两边
#   2. random.choice(['茅台', '招行', '腾讯']) --> 从列表里随机选一个
#       choice(seq): 从非空序列里随机选一个元素
#   3. random.sample([...], 3) --> 随机选3个不重复的
#       sample(population, k): 从总体里抽取 k 个不重复的样本

# ↓ 你的代码 ↓
import random
print(random.randint(1,100))
print(random.choice(['茅台','招行','腾讯']))
print(random.sample(['1','2','3','4'],2))

# statistics 模块提供统计计算函数.
# 量化场景: 分析策略表现时, 第一件事就是看平均收益率.
#
# mean(数据列表):
#   mean    -> 函数名, 算数平均数(加起来除个数)
#   参数    -> 一个列表/可迭代对象, 里面是数字
#   返回    -> float, 平均值
#   量化意义: 告诉你"策略平均每天赚多少"
#
# median(数据列表):
#   median  -> 函数名, 中位数(排序后中间那个)
#   参数    -> 同上
#   返回    -> float, 中位数
#   量化意义: 比 mean 更抗极端值(比如某天暴涨暴跌), 反映"典型"收益

print("\n" + "=" * 40 + "\n练习 1.2")

# ■ 练习 1.2: 用 statistics 算均值/中位数
# 从 statistics 模块导入 mean 和 median 两个函数,
# 分别用它们算 returns 的平均收益率和中位数.

returns = [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.01]

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 二, 自定义模块 --- 把你的代码分到不同文件
# ═══════════════════════════════════════════════════

# 一个 .py 文件就是一个模块. 当你的代码超过 200 行, 就应该拆到多个文件里.
# 好处:
#   - 每个文件职责明确(一个文件只做一类事)
#   - 可以复用: 多个脚本共享同一个模块
#   - 容易维护: 改一个模块不影响其他

# 我帮你创建了配套文件 day05_utils.py, 里面有两个函数:
#   calculate_sharpe()   -> 计算夏普比率(量化核心指标)
#   filter_stocks()      -> 过滤低价股

# --- 2.1 if __name__ == '__main__' ---

# 这是一个重要但容易困惑的写法. 先理解背景:
#   每个 .py 文件都有一个内置变量 __name__
#   当直接运行这个文件时: __name__ 被设为 '__main__'
#   当被 import 时: __name__ 被设为文件名(不含 .py)
#
# 所以这个 if 语句的意思是:
#   "只有当我是被直接运行(而不是被 import)时, 才执行下面的代码"
#
# 用途:
#   在 if 块里写测试代码 / 演示代码,
#   别人 import 这个模块时不会意外执行它们


print("\n" + "=" * 40 + "\n练习 2.1")

# ■ 练习 2.1: import 自定义模块
# 配套 day05_utils.py 提供了两个函数:
#
# 1. calculate_sharpe(returns, rf=0.02):
#    returns      -> list[float], 日收益率序列
#    rf           -> float, 无风险利率(年化), 默认 2%
#    返回 float, 夏普比率越大说明策略风险调整后收益越好
#    夏普比率是量化面试必考题, 公式: (策略收益 - 无风险利率) / 波动率
#
# 2. filter_stocks(prices_dict, threshold=50):
#    prices_dict  -> dict[str, float], {股票名: 价格}
#    threshold    -> float, 价格阈值, 低于此值被选出
#    返回 list[str], 符合条件的股票名列表

# 先用 import day05_utils as utils 导入
# 然后分别调用这两个函数

returns = [0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.01]
prices = {"茅台": 180, "招行": 35, "平安": 45, "宁德": 220, "万科": 15}

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 三, pip --- Python 的"应用商店"
# ═══════════════════════════════════════════════════

# pip 是 Python 的包管理器, 从 PyPI(python 包索引)下载第三方库.
# C++ 类比: vcpkg install 或 conan install
# 区别: pip 更简单, 一行命令就行.
#
# 常用命令(在终端/cmd 里运行, 不能在 .py 文件里写):
#   pip install 包名           安装最新版
#   pip install 包名==1.2.3    安装指定版本
#   pip list                   查看所有已安装的包
#   pip uninstall 包名         卸载

# 后面会用到的第三方库:
#   - numpy:    数值计算, 比 Python 自带快 100 倍
#   - pandas:   数据分析, 处理表格数据
#   - requests: 发 HTTP 请求, 爬取数据
#   - matplotlib: 画图

# 注意: 安装前先激活 .venv 虚拟环境(独立环境, 不影响系统 Python)
# 我们的 .venv 已经准备好, 可以直接 pip install

# --- 3.1 查看已安装的包 ---

# importlib.metadata.distributions() 可以列出当前环境所有已安装的包
"from importlib.metadata import distributions"
"installed = [dist.metadata['Name'] for dist in distributions()]"
"print(f'已安装 {len(installed)} 个包')"
"print(sorted(installed)[:10])  # 前10个"


print("\n" + "=" * 40 + "\n练习 3.1")

# ■ 练习 3.1: 检查包是否已安装
# 用 try/except ImportError 检测包是否存在.
# ImportError 是 Python 在 import 失败时抛出的异常.
#
# 遍历 packages_to_check, 逐个尝试 import:
#   成功 -> 打印 "[OK] xxx 已安装"
#   失败(ImportError) -> 打印 "[..] xxx 未安装, 请运行: pip install xxx"
#
# 提示: 用 __import__(pkg) 可以动态 import 一个字符串名字的包

packages_to_check = ['requests', 'numpy', 'pandas', 'matplotlib', 'flask']

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 四, datetime --- 处理时间数据
# ═══════════════════════════════════════════════════

# 量化开发最频繁的操作之一就是处理时间.
# 股票数据天然是时间序列: 每天一个价格, 每分钟一个 tick.
# C++: #include <chrono> + std::chrono::system_clock
# Python: from datetime import datetime (一行搞定)

# --- 4.1 获取当前时间 ---

# datetime.now():
#   datetime -> 类名, 代表一个具体的时间点(年/月/日/时/分/秒/微秒)
#   now()    -> 类方法, 返回当前本地时间
#   返回     -> datetime 对象
from datetime import datetime

"now = datetime.now()"
"print(now)                # 2026-05-31 14:30:00.123456"

# from datetime import datetime 之后:
#   第一个 datetime 是 模块名(文件夹)
#   第二个 datetime 是 类名(文件夹里的一个类)
#   所以写 datetime.now() 用的是类, 不是模块

# datetime 对象可以直接访问年/月/日/时/分/秒:
"print(now.year)           # 2026"
"print(now.month)          # 5"
"print(now.day)            # 31"
"print(now.hour)           # 14"

# --- 4.2 创建指定时间 ---

# 你也可以手动"组装"一个时间.
# datetime(年, 月, 日, 时, 分, 秒):
#   参数按顺序: year, month, day, hour, minute, second
#   hour/minute/second 可以省略, 默认为 0
"dt = datetime(2026, 6, 1, 9, 30, 0)"
"print(dt)                 # 2026-06-01 09:30:00"

# --- 4.3 格式化时间 (strftime) ---

# strftime = "string format time", 把时间转成你想要的字符串格式.
# C++ 类比: std::put_time(std::localtime(&t), "%Y-%m-%d")
#
# 常用格式化符号(需要记忆):
#   %Y  -> 4位年份 (2026)
#   %m  -> 2位月份 (01-12)
#   %d  -> 2位日   (01-31)
#   %H  -> 24小时制 (00-23)
#   %M  -> 分钟     (00-59)
#   %S  -> 秒       (00-59)
#   %A  -> 星期全名 (Sunday)
#   %a  -> 星期缩写 (Sun)

"print(now.strftime('%Y-%m-%d'))          # 2026-05-31"
"print(now.strftime('%H:%M:%S'))          # 14:30:00"

# 中文也是可以用的(操作系统支持即可):
"print(now.strftime('%Y年%m月%d日 %A'))    # 2026年05月31日 Sunday"

# --- 4.4 解析字符串 (strptime) ---

# strptime = "string parse time", strftime 的反向操作.
# 把字符串转成 datetime 对象, 这样你才能做日期计算.
# 量化场景: CSV 文件里的日期是字符串 '2026-06-01', 需要转成 datetime 才能算间隔.
#
# datetime.strptime(待解析字符串, 格式):
#   第一个参数: 日期字符串
#   第二个参数: 字符串的格式, 必须跟字符串匹配
#   返回: datetime 对象
#
# 容易踩坑: 格式不匹配会报错 ValueError
#   '2026-06-01' 必须用 '%Y-%m-%d'
#   '2026/06/01' 必须用 '%Y/%m/%d'
"date_str = '2026-06-01'"
"dt = datetime.strptime(date_str, '%Y-%m-%d')"
"print(dt)                 # 2026-06-01 00:00:00"


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
# 你有 5 个日期字符串, 需要转成 datetime 对象.
# 然后打印每个日期是星期几.
# 提示: datetime.strptime(s, '%Y-%m-%d') 把字符串转 datetime
#       然后用 .strftime('%A') 获取星期

date_strings = ['2026-05-26', '2026-05-27', '2026-05-28', '2026-05-29', '2026-05-30']

# ↓ 你的代码 ↓


# --- 4.5 timedelta --- 时间差计算

# timedelta = "time delta", 表示两个时间之间的差值.
# C++ 类比: std::chrono::duration

"from datetime import timedelta"

"today = datetime.now()"

# timedelta(days=1) 创建一个"1天"的时间差
# 你可以加/减到 datetime 上:
"one_day = timedelta(days=1)"
"yesterday = today - one_day"    # 当前时间 - 1天 = 昨天
"tomorrow = today + one_day"     # 当前时间 + 1天 = 明天

"print(f'昨天: {yesterday.strftime(\"%Y-%m-%d\")}')"
"print(f'明天: {tomorrow.strftime(\"%Y-%m-%d\")}')"

# timedelta 支持更多参数:
#   timedelta(days=5, hours=3, minutes=30)
#   这会创建一个"5天3小时30分"的时间差
"delta = timedelta(days=5, hours=3, minutes=30)"
"print(delta)              # 5 days, 3:30:00"

# 两个 datetime 相减自动得到一个 timedelta:
#   dt1 - dt2  -> timedelta
#   .days 属性 -> 相差的天数(整数)
# 量化场景: 计算持股天数、回测周期长度
"dt1 = datetime(2026, 6, 1)"
"dt2 = datetime(2026, 5, 25)"
"diff = dt1 - dt2"
"print(diff.days)          # 7"


print("\n" + "=" * 40 + "\n练习 4.3")

# ■ 练习 4.3: 计算持股天数
# 你在 2026-05-15 买入, 2026-05-28 卖出.
# 1. 把 buy_date_str 和 sell_date_str 转成 datetime
# 2. 用减法算日期差: sell_dt - buy_dt
# 3. 用 .days 提取天数
# 4. 打印 "持股 X 天"

buy_date_str = '2026-05-15'
sell_date_str = '2026-05-28'

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 五, os + pathlib --- 文件和路径操作
# ═══════════════════════════════════════════════════

# 量化开发经常要: 检查数据文件是否存在、拼接路径、遍历目录(找所有 .csv)

# --- 5.1 os 模块(传统方式) ---

# os 模块提供操作系统相关功能.
import os

# os.getcwd(): get current working directory, 获取当前工作目录
"print(os.getcwd())        # 当前工作目录"

# os.path.join(路径1, 路径2, ...):
#   拼接路径, 自动处理操作系统的路径分隔符
#   Windows -> data\\finance.csv
#   Linux/Mac -> data/finance.csv
#   永远用 os.path.join, 不要自己拼字符串
"data_path = os.path.join('data', 'finance.csv')"
"print(data_path)          # data\\finance.csv (Windows)"

# os.path.exists(路径):
#   检查文件/目录是否存在, 返回 True/False
"print(os.path.exists(data_path))   # True/False"

# --- 5.2 pathlib (现代方式, Python 3.4+) ---

# pathlib 是 Python 3.4 引入的新一代路径操作库.
# 比 os.path 更直观, 推荐在新代码中使用.
from pathlib import Path

# Path(路径字符串): 创建一个 Path 对象, 代表一个文件/目录
"p = Path('data/finance.csv')"

# Path 对象的方法:
#   .exists() -> 是否存在 (True/False)
#   .suffix   -> 扩展名 (.csv)
#   .stem     -> 文件名(不含后缀) (finance)
#   .parent   -> 父目录 (data)
"print(p.exists())         # True"
"print(p.suffix)           # .csv"
"print(p.stem)             # finance"
"print(p.parent)           # data"

# pathlib 最大的优势: 可以用 / 拼接路径, 不用 os.path.join
"data_dir = Path('data')"
"csv_file = data_dir / 'finance.csv'"   # 直接用 / 拼接!
"print(csv_file)           # data\\finance.csv"

# Path('output').mkdir(exist_ok=True):
#   创建目录. exist_ok=True 表示目录已存在也不会报错
"Path('output').mkdir(exist_ok=True)"

# Path('.').iterdir():
#   遍历当前目录下的所有条目(文件/文件夹)
#   配合 .suffix 可以筛选指定类型
"for f in Path('.').iterdir():"
"    if f.suffix == '.csv':"
"        print(f.name)     # 只打印 .csv 文件"


print("\n" + "=" * 40 + "\n练习 5.1")

# ■ 练习 5.1: pathlib 实战
# 1. 用 Path('data/tech.csv') 创建路径对象
# 2. 用 .exists() 检查文件是否存在
# 3. 如果存在:
#    - 打印文件名(.name)
#    - 打印后缀(.suffix)
#    - 打印文件大小(.stat().st_size, 单位字节)
#    - 打印父目录(.parent)
# 4. 用 Path('output').mkdir(exist_ok=True) 确保 output 目录存在

# ↓ 你的代码 ↓


print("\n" + "=" * 40 + "\n练习 5.2")

# ■ 练习 5.2: datetime + pathlib 组合
# 遍历 data/ 目录下所有 .csv 文件, 打印每个文件的最后修改时间.
#
# 步骤:
#   1. Path('data').iterdir() 遍历 data 目录
#   2. 筛选 .suffix == '.csv' 的文件
#   3. f.stat().st_mtime 获取修改时间戳(秒数, 从1970年算起)
#   4. datetime.fromtimestamp(时间戳) 把时间戳转成可读的 datetime
#   5. 用 .strftime() 格式化为 "2026-05-30 14:30"

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 综合练习: 交易日历工具
# ═══════════════════════════════════════════════════

print("\n" + "=" * 40 + "\n综合练习")

# 综合应用: import + datetime + pathlib + 自定义模块
#
# 背景: A 股交易规则
#   - 周一到周五交易
#   - 周末不交易
#   - 不考虑法定节假日(简化)
#
# 配套模块 day05_utils.py 已经实现了三个函数:
#   - is_trading_day(date) -> bool
#     date.weekday() 返回 0-6(周一到周日), <5 就是交易日
#
#   - next_trading_day(date) -> datetime
#     从 date+1 开始逐天检查, 直到找到交易日
#
#   - trading_days_between(start, end) -> list[datetime]
#     遍历 start 到 end 的每一天, 收集所有交易日
#
# 你的任务:
#
# 1. import day05_utils as utils
#    然后调用 utils.trading_days_between() 看看 2026 年 5 月有多少交易日
#
# 2. 实现 prev_trading_day(date) -> datetime
#    思路: 从 date-1 开始, 逐天往前检查 is_trading_day
#
# 3. 实现 count_trading_days_until(target_date) -> int
#    思路: 用 datetime.now() 获取今天, 去掉时间部分(hour=0...)
#        然后用 trading_days_between(today, target_date) 算天数
#        提示: .replace(hour=0, minute=0, second=0, microsecond=0)
#
# 4. 把从今天起未来60天的交易日历保存到 output/trading_calendar.txt
#    每行格式: "2026-06-01 (Monday)"
#    提示: 用 trading_days_between(today, today + timedelta(days=60))
#        再用 open + write 写文件

# ↓ 你的代码 ↓
