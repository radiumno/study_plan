"""
day05_utils.py — Day 5 配套模块
供 day05_模块与包.py 练习 import 使用

包含:
  - calculate_sharpe(): 算夏普比率
  - filter_stocks(): 过滤低价股
  - is_trading_day(): 判断交易日
  - next_trading_day(): 下一个交易日
  - trading_days_between(): 两个日期间的交易日列表
"""

from statistics import mean, stdev
from datetime import datetime, timedelta


def calculate_sharpe(returns, rf=0.02, periods_per_year=252):
    """计算年化夏普比率"""
    if len(returns) < 2:
        return 0.0
    avg_return = mean(returns)
    excess_return = avg_return - rf / periods_per_year
    vol = stdev(returns)
    if vol == 0:
        return 0.0
    annualized_excess = excess_return * periods_per_year
    annualized_vol = vol * (periods_per_year ** 0.5)
    return annualized_excess / annualized_vol


def filter_stocks(prices_dict, threshold=50):
    """过滤出价格低于阈值的股票"""
    return [name for name, price in prices_dict.items()
            if price <= threshold]


def is_trading_day(date):
    """判断某天是不是交易日(简化版: 周一~周五)"""
    return date.weekday() < 5


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
