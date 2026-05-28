紧急抢救：恢复 Day 03 丢失的练习代码

## 发生了什么

Hermes 运行了一个清除中文标点的脚本，但脚本有 bug（`f.write(content)` 写成了 `f.write(fname)`），导致 `day03_函数.py` 被覆盖成了文件名。

Hermes 从会话日志恢复了一版，但只恢复了教学字符串和练习题目标，**你手写的练习代码全部丢失**。具体丢了：

1. 练习4（作用域）：你写的 `analyze_stock` + `global call_count` 实现
2. 练习5（lambda）：你写的 lambda 排序/max/map/filter 实现
3. 综合练习（股票计算器工具箱）：你写的 `calc_market_value`、`calc_total`、`print_report` 实现
4. 你超预期加的：`sorted(portfolio, key=lambda x: calc_market_value(...))` 按市值排序展示
5. 你踩过并修好的 6 个坑（缩进、变量名覆盖 max/min、print 嵌套等）

## 文件路径

D:\Dev\AiProject\study_plan\projects\python\tutorials\day03_函数.py

## 抢救线索

去以下位置找你可能写过的代码：

1. **Claude Code 文件历史**（最可能找到）
   `C:\Users\30958\.claude\file-history\f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa\`
   这个目录有 Day 01/Day 02 的历史版本，但 Day 03 的 hash 不同。
   遍历所有子目录，找含有 "Day 3" 或 "day03" 或 "_函数" 且大小 > 5000 字节的文件。

2. **Claude Code 会话 JSONL**
   `C:\Users\30958\.claude\projects\D--Dev-AiProject-study-plan\f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa.jsonl`
   这个文件记录了这个 session 的所有 tool call 和结果。搜索：
   - 包含 "day03_函数.py" 的 write_file 调用
   - 包含 "toolUseResult" + "file" + "content" 且内容 > 5000 字节的记录
   - 用户的练习代码特征词：`calc_total`、`print_report`、`sorted(portfolio`

3. **VS Code 本地历史**
   Windows 上 VS Code 可能在 `C:\Users\30958\AppData\Roaming\Code\User\History\` 有备份
   或者用 `Ctrl+Shift+P` → "Local History: Show Local History" 查看

4. **Windows Previous Versions**
   在 `D:\Dev\AiProject\study_plan\projects\python\tutorials\` 文件夹上右键 → 属性 → 以前的版本
   或者用 PowerShell: `Get-ChildItem -Path "D:\Dev\AiProject\study_plan\projects\python\tutorials\day03_函数.py" | ForEach-Object { $_.VersionInfo }`

## 恢复后要做的

1. 写回 `D:\Dev\AiProject\study_plan\projects\python\tutorials\day03_函数.py`
2. 确认以下内容都在：
   - `stock_stats_right(prices_list)` — 用户自己发现的 max/min/sum 版本
   - 练习4 的 `analyze_stock` + `global call_count`
   - 练习5 的 lambda 四道题
   - 综合练习全部 5 道题（含 `sorted(portfolio, key=...)`）
3. `git add day03_函数.py && git commit -m "recover day03 from claude code session" && git push`
