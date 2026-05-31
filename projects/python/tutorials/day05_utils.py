"""
day05_utils.py — Day 5 配套模块
供 day05_模块与包.py 练习 import 使用
"""

from statistics import mean, stdev


def calculate_sharpe(returns, rf=0.02, periods_per_year=252):
    """计算夏普比率

    参数:
        returns: list[float], 日收益率序列
        rf: float, 无风险利率(年化), 默认 2%
        periods_per_year: int, 年化期数, 默认 252(交易日)

    返回:
        float, 年化夏普比率
    """
    if len(returns) < 2:
        return 0.0

    avg_return = mean(returns)                # 日均收益率
    excess_return = avg_return - rf / periods_per_year  # 日均超额收益
    vol = stdev(returns)                      # 日收益率标准差

    if vol == 0:
        return 0.0

    # 年化: 超额收益 * 252, 波动率 * sqrt(252)
    annualized_excess = excess_return * periods_per_year
    annualized_vol = vol * (periods_per_year ** 0.5)

    return annualized_excess / annualized_vol


def filter_stocks(prices_dict, threshold=50):
    """过滤出价格低于阈值的股票

    参数:
        prices_dict: dict[str, float], {股票名: 价格}
        threshold: float, 价格阈值

    返回:
        list[str], 低于阈值的股票名列表
    """
    return [name for name, price in prices_dict.items()
            if price <= threshold]
