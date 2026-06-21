---
title: rolling 窗口 — 均线和波动率计算
type: concept
tags: [pandas, rolling, sma, volatility]
date: 2026-06-21
status: active
source: claude
---
# rolling 窗口 — 均线和波动率计算

**一句话：** `.rolling(window).mean()` 是 Pandas 算移动平均线的核心方法。

## 核心要点
- `df['close'].rolling(window=5).mean()` → 5 日均线 (SMA_5)
- `df['close'].rolling(window=20).mean()` → 20 日均线 (SMA_20)
- `df['close'].pct_change()` → 日收益率
- `df['daily_ret'].rolling(20).std() * np.sqrt(252)` → 年化波动率

## 常见坑
- rolling 窗口默认用末尾对齐，前 N-1 行是 NaN
- 金叉 = SMA_5 上穿 SMA_20，需要 shift 判断穿越
- 金叉信号: `(df['SMA_5'] > df['SMA_20']) & (df['SMA_5'].shift(1) <= df['SMA_20'].shift(1))`

## 关联
- [[知识点/tbd-时间序列基础]]
