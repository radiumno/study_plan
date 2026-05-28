# Day 03 学习汇报 — 2026-05-28

## 完成情况

**教学 + 练习，6/6 全部完成**

| 章节 | 内容 | 练习数 | 状态 |
|------|------|--------|------|
| 一、函数定义和调用 | def / return / None | 3 | ✅ |
| 二、参数进阶 | 默认参数、关键字参数、*args、**kwargs、混合顺序 | 4 | ✅ |
| 三、函数是一等公民 | 函数赋值、传参、多返回值 | 4 | ✅ |
| 四、作用域 | local / global / nonlocal | 3 | ✅ |
| 五、Lambda 表达式 | lambda + sorted/max/map/filter | 4 | ✅ |
| 六、综合练习 | 股票计算器工具箱（函数传函数、排序、筛选、格式化报告） | 5 | ✅ |

## 超预期表现

- 综合练习**超额完成**：题目没要求排序打印持仓，自己加了 `sorted(portfolio, key=lambda x: calc_market_value(...))` 按市值排序展示
- **自己发现 Python 内置函数**：手写 `find_max`/`find_min`/`avg_` 之后，主动意识到 `max()`/`min()`/`sum()` 的存在，并自己写了一个 `stock_stats_right` 版本对比
- 链式调用 `sorted + lambda + 自定义函数` 一次写对
- C++ 肌肉记忆持续打破——今天只打了一次 `int main() {}`，其余时间正确输出 `def/:/print`

## 遇到的问题

1. `avg_` 函数 `return` 缩进错误（在 for 循环里，第一轮就返回了）→ 已修复
2. `max`/`min` 变量名覆盖内置函数 → 已改名
3. `print_report` 拼写多次不一致 (`print_reoort` / `print_repotr`) → 持续提醒中
4. 外层 `print()` 套在已有 print 的函数调用上，输出多余 None → 已纠正
5. `map(key=lambda ...)` 错误使用了 key= → 已纠正
6. `sorted()` 没接返回值（以为会原地排序）→ 已讲清楚 sorted vs sort 区别

## 课程设计问题（Claude Code 暴露的）

- Day 02 **漏教 tuple**：Day 03 `*args` 返回元组时用户才第一次接触
- **内置函数**（max/min/sum/len）从未正式教学，练习中直接用了
- 这两个缺口已记录，后续会补

## 对 Hermes 的反馈

- Day 03 内容量适中，用户 2-3 小时完成
- **需要补的内容**：建议 Day 02 追加元组教学 + 内置函数速览（max/min/sum/len/sorted），或者合并在 Day 04 开篇
- 用户 C++ 背景转化顺利，函数传函数、lambda 等高阶概念接受很快
- 明天 Day 04（文件 I/O + 异常处理）准备好了

## 进度

```
阶段1 Python基础  ████████░░░░  3/17 天
 ├─ day01 变量与类型 ✅
 ├─ day02 列表与字典 ✅
 ├─ day03 函数         ✅  ← 刚完成
 ├─ day04 文件与异常   ⏳
 ├─ day05 模块与包      ⏳
 ├─ day06-07 综合项目   ⏳
```
