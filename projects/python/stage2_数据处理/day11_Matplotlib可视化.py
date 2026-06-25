"""
====================================================
 Day 11 | Matplotlib 可视化 -- 让行情和策略看得见
====================================================

 目标: 用 Figure / Axes 把价格、成交量、收益分布和买卖点画出来

 参考源:
   - Matplotlib Quick start guide
     https://matplotlib.org/stable/users/explain/quick_start.html
   - Introduction to Axes
     https://matplotlib.org/stable/users/explain/axes/axes_intro.html
   - Annotate plots
     https://matplotlib.org/stable/gallery/text_labels_and_annotations/annotation_demo.html
   - whale-quant ch07 量化回测评估
   - 2026保姆级数据分析系统教程 / Matplotlib实战 1h入门

 三线:
   量化主线 (80%): 价格曲线、成交量、收益分布、买卖点标注
   AI辅线 (10%): 图表是后续特征分析和报告展示的基础
   考研 (10%): 图像表达和统计直觉

====================================================
"""

# ═══════════════════════════════════════════════════
# 进度: 阶段1 Python基础 -- Part 2 数据处理 (Day 08~14)
#   Day 08 NumPy 数组运算   ✅
#   Day 08R NumPy 强化      ✅
#   Day 09 Pandas 入门      ✅
#   Day 10 Pandas 进阶      ✅
#   Day 11 ▶ Matplotlib 可视化 (今天)
#   Day 12 R2 复习日       (下一课)
#   Day 13-14 数据采集+综合
# ═══════════════════════════════════════════════════

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def build_market_frame(seed: int = 42) -> pd.DataFrame:
    """生成一份可复现的量化练习数据。"""
    np.random.seed(seed)
    dates = pd.date_range("2024-01-02", periods=30, freq="B")
    base = np.concatenate(
        [
            np.linspace(100, 108, 10),
            np.linspace(108, 96, 10),
            np.linspace(96, 112, 10),
        ]
    )
    noise = np.random.randn(len(dates)) * 0.8
    close = base + noise
    volume = np.random.randint(8_000, 15_000, size=len(dates))

    frame = pd.DataFrame({"close": close, "volume": volume}, index=dates)
    frame["sma_5"] = frame["close"].rolling(5).mean()
    frame["sma_10"] = frame["close"].rolling(10).mean()
    frame["ret"] = frame["close"].pct_change()
    frame["buy_signal"] = (
        (frame["sma_5"] > frame["sma_10"])
        & (frame["sma_5"].shift(1) <= frame["sma_10"].shift(1))
    )
    frame["sell_signal"] = (
        (frame["sma_5"] < frame["sma_10"])
        & (frame["sma_5"].shift(1) >= frame["sma_10"].shift(1))
    )
    return frame


market = build_market_frame()

print("\n" + "=" * 50)
print("Day 11 | Matplotlib 可视化")
print("=" * 50)
print(market[["close", "volume", "sma_5", "sma_10"]].head(3))


# ═══════════════════════════════════════════════════
# 复习环节 -- Day 10 回顾
# ═══════════════════════════════════════════════════
# Day 10 核心: 时间序列、rolling、resample、groupby、merge。

print("\n" + "=" * 40 + "\n复习环节")

# 练习 R1: 把字符串日期转成 DatetimeIndex, 再取出 1 月中旬的数据。
review_df_1 = pd.DataFrame(
    {
        "date": ["2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
        "close": [100, 102, 101, 103],
    }
)

# ↓ 你的代码 ↓


# 练习 R2: 计算 5 日均线, 并看看前几行的 NaN。
review_df_2 = pd.DataFrame({"close": [100, 101, 103, 102, 104, 106, 105]})

# ↓ 你的代码 ↓


# 练习 R3: 把日频数据重采样成周频, 取最后一个收盘价。
review_df_3 = pd.DataFrame(
    {"close": [100, 101, 102, 103, 104, 105, 106]},
    index=pd.date_range("2024-01-01", periods=7, freq="D"),
)

# ↓ 你的代码 ↓


# 练习 R4: 按月份分组, 计算每月平均收盘价。
review_df_4 = pd.DataFrame(
    {
        "date": pd.to_datetime(
            ["2024-01-03", "2024-01-18", "2024-02-02", "2024-02-20"]
        ),
        "close": [100, 102, 104, 106],
    }
)

# ↓ 你的代码 ↓


# 练习 R5: 合并两张表, 一个是价格, 一个是基准收益率。
review_left = pd.DataFrame(
    {"date": pd.date_range("2024-01-02", periods=3, freq="B"), "close": [100, 101, 102]}
)
review_right = pd.DataFrame(
    {"date": pd.date_range("2024-01-02", periods=3, freq="B"), "bench_ret": [0.01, -0.02, 0.03]}
)

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 知识块1: Figure / Axes / 折线图
# ═══════════════════════════════════════════════════
# 量化场景: 一张价格线比一堆数字更容易看趋势和拐点。

print("\n" + "=" * 40 + "\n知识块1: Figure / Axes / 折线图")

# --- 知识点1.1: plt.subplots() ---
# Matplotlib 最常用的入口是 plt.subplots().
# 它一次返回 Figure 和 Axes, 比先 figure 再 add_subplot 更直接。

fig1, ax1 = plt.subplots(figsize=(9, 4))
ax1.plot(market.index, market["close"], label="Close", color="tab:blue", linewidth=2)
ax1.set_title("Close Price")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price")
ax1.grid(True, alpha=0.3)
ax1.legend()
fig1.tight_layout()
plt.close(fig1)

print("figure/axes 折线图已生成并关闭")

print("\n--- 练习 1.1.1: 画收盘价折线 ---")

# 给定 market 数据, 画出 close 折线, 并设置标题、x 轴、y 轴。
# 提示: 先拿到 fig, ax, 再用 ax.plot()

# ↓ 你的代码 ↓


# --- 知识点1.2: 叠加均线、图例和标注 ---
# 量化场景: close + SMA + 买卖点标注, 就是一张最基础的策略观察图。

buy_points = market.loc[market["buy_signal"], "close"]
sell_points = market.loc[market["sell_signal"], "close"]

fig2, ax2 = plt.subplots(figsize=(9, 4))
ax2.plot(market.index, market["close"], label="Close", color="tab:blue", linewidth=1.8)
ax2.plot(market.index, market["sma_5"], label="SMA 5", color="tab:orange", linestyle="--")
if not buy_points.empty:
    ax2.scatter(buy_points.index, buy_points.values, color="green", label="Buy", zorder=3)
    for ts, price in buy_points.items():
        ax2.annotate("Buy", xy=(ts, price), xytext=(0, 10), textcoords="offset points", ha="center")
if not sell_points.empty:
    ax2.scatter(sell_points.index, sell_points.values, color="red", label="Sell", zorder=3)
    for ts, price in sell_points.items():
        ax2.annotate("Sell", xy=(ts, price), xytext=(0, -14), textcoords="offset points", ha="center")
ax2.set_title("Close with SMA and Signals")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price")
ax2.grid(True, alpha=0.25)
ax2.legend()
fig2.tight_layout()
plt.close(fig2)

print("均线和信号标注图已生成并关闭")

print("\n--- 练习 1.2.1: 叠加均线和信号 ---")

# 在上一题的基础上, 叠加 SMA 10, 并把 buy / sell 点标出来。

# ↓ 你的代码 ↓


# 知识块1总练习: 画出 close + SMA_5 + SMA_10 的完整折线图, 并标出买卖点。

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# 知识块2: 柱状图 / 直方图 / 多子图
# ═══════════════════════════════════════════════════
# 量化场景: 成交量看活跃度, 直方图看收益分布, 多子图看全局。

print("\n" + "=" * 40 + "\n知识块2: 柱状图 / 直方图 / 多子图")

# --- 知识点2.1: bar 和 hist ---
# bar 适合成交量、行业收益、持仓权重。
# hist 适合看收益率分布, 判断偏态和极端波动。

fig3, (ax3, ax4) = plt.subplots(1, 2, figsize=(11, 4))
ax3.bar(market.index, market["volume"], color="tab:gray", width=0.8)
ax3.set_title("Volume")
ax3.set_xlabel("Date")
ax3.set_ylabel("Shares")
ax3.tick_params(axis="x", rotation=45)

ax4.hist(market["ret"].dropna(), bins=12, color="tab:purple", alpha=0.8)
ax4.set_title("Return Distribution")
ax4.set_xlabel("Return")
ax4.set_ylabel("Count")
fig3.tight_layout()
plt.close(fig3)

print("柱状图和直方图已生成并关闭")

print("\n--- 练习 2.1.1: 画成交量和收益分布 ---")

# 用成交量画 bar 图, 再对日收益率画 hist 图。

# ↓ 你的代码 ↓


# --- 知识点2.2: 多子图和简易K线 ---
# 量化场景: 一个窗口里同时看价格和成交量, 比单图更像真实日报。
# 选修: 用 vlines / hlines 可以画出简易 K 线, 但今天只做够用版。

fig4, (ax5, ax6) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
ax5.plot(market.index, market["close"], color="tab:blue", label="Close")
ax5.plot(market.index, market["sma_5"], color="tab:orange", linestyle="--", label="SMA 5")
ax5.legend()
ax5.set_ylabel("Price")
ax5.grid(True, alpha=0.25)

ax6.bar(market.index, market["volume"], color="tab:gray")
ax6.set_xlabel("Date")
ax6.set_ylabel("Volume")
ax6.tick_params(axis="x", rotation=45)
fig4.tight_layout()
plt.close(fig4)

print("多子图价格/成交量图已生成并关闭")

print("\n--- 练习 2.2.1: 画双子图报表 ---")

# 画一个上下两栏图:
#   上面是 close + SMA_5
#   下面是 volume

# ↓ 你的代码 ↓


# 知识块2总练习: 用现有数据再做一张收益率图, 检查波动是不是偏右尾。

# ↓ 你的代码 ↓


# ═══════════════════════════════════════════════════
# Day 综合练习
# ═══════════════════════════════════════════════════
# 目标: 做出一张完整的交易观察图, 能给别人讲清楚趋势和信号。

print("\n" + "=" * 40 + "\nDay 综合练习")

# 用一个 2x1 图完成:
#   1. 上图: close + SMA_5 + SMA_10 + 买卖点标注
#   2. 下图: volume
# 这张图就是后面策略日报的最小版本。

# ↓ 你的代码 ↓

