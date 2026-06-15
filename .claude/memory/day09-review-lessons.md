---
date: 2026-06-16
source: "Hermes Agent Code Review"
---

# Day 09 审查反馈 — 后续写课注意

## 1. yfinance A 股数据在国内不可用
- `600519.SS` 这类 A 股代码在 yfinance 上经常返回空
- 用户在国内需要开 WARP/VPN 才能连雅虎财经
- **后续：** yfinance 练习统一用美股（AAPL/MSFT/GOOGL/AMZN），A 股数据用 baostock 或 akshare

## 2. yfinance 多股票下载产生 MultiIndex
```python
portfolio = yf.download(['AAPL', 'MSFT', 'GOOGL'])
portfolio['Close']  # 列名是 ('Close', 'AAPL') 多级索引
```
Day 09 还没教 MultiIndex，学生看到会懵。
**后续：** 凡是用到 yfinance 多股票的地方，加一行注释解释多级列名，或者只用单只股票。

## 3. yfinance 数据有 NaN
yfinance 拉回来的数据节假日是 NaN，但 NaN 处理在 Day 09 没教。
**后续：** 涉及 yfinance 的练习要在前面先教 `.dropna()` 或 `.isna()`，或者在练习里加提示。

## 4. 练习不要超前教还没讲的知识点
综合练习里要求"计算月均价"，但 `resample` 和 `groupby` 都是 Day 10 才教的内容。
**后续：** 当天的综合练习只考当天教过的知识点。超前的知识标注为"选做"或移到对应 Day。

## 5. JSON 作为副线可以，但过渡要自然
Day 09 的主线是 Pandas，JSON 突然插在 CSV 和 yfinance 之间。
**后续：** 如果副线和主线跳跃太大，加一句过渡说明，比如"量化开发经常从 API 拿到 JSON 格式数据，Pandas 处理 JSON 有两种方式…"
