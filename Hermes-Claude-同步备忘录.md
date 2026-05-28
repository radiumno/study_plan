---
title: Hermes ↔ Claude Code 同步备忘录
description: 给 Claude Code 的对接提示词，读完这个就算对齐了
date: 2026-05-28
---

# Hermes ↔ Claude Code 同步备忘录

> Claude Code 读这个文件，读完我们就对齐了。

---

## 1. 协作模式（最终版）

| 角色 | 职责 |
|------|------|
| **Hermes** | 写计划、出题、做依赖检查、维护文档 |
| **Claude Code** | 检查计划依赖、备课、等用户提问、答疑讲题、做 Code Review |

- Hermes 高半级——题是 Hermes 出的，Claude Code 负责讲
- 平级协作，不是谁指挥谁

详见根目录 `COLLEAGUES.md`

---

## 2. COLLEAGUES.md 的内容（新版）

如果你读的 COLLEAGUES.md 是旧的，关键变更：

- ~~Claude Code 写教程~~ → **Claude Code 只答疑讲题**，不写新教程
- ~~Hermes 听 Claude Code 指挥~~ → **平级协作，Hermes 高半级**
- 依赖清单表格有 4 列：依赖项 / 类型 / 首次出现 / 确认覆盖

请重新读一遍根目录的 `COLLEAGUES.md`。

---

## 3. 课程内容变更

### Day 02 已补：tuple + 内置函数

你的 mistakes log 说 Day 02 漏了 tuple 和内置函数。现在已经补了：

| 新增内容 | 位置 |
|---------|------|
| 1.5 tuple（创建/访问/不可变/解包/交换变量） | Day 02 第 135 行 |
| 1.6 内置函数（len/max/min/sum/sorted） | Day 02 第 185 行 |

Day 03 的 `*args`（返回元组）现在有前置知识了。`stock_stats` 练习可以直接用 `max()`/`min()`/`sum()`。

### Day 04 已写：set + 文件I/O + 异常处理

- 四大基础类型最后一块拼图：set 在 Day 04 教完
- 文件头顶嵌了完整依赖清单
- 练习之间有分割符，无中文符号

---

## 4. 写课程的两条铁规矩

2026-05-28 用户确认的两条规则，以后所有教程文件必须遵守：

### 规则一：练习分割符

每个练习前面必须有分割行，格式和 Day 01-03 一致：

```python
print("\n" + "=" * 40 + "\n练习 X.Y")
# ■ 练习 X.Y: 标题
```

不能出现两个练习之间没有分割的情况。

### 规则二：无中文标点

全文不能出现中文标点符号。以下中文符号必须替换为 ASCII 等价：

| 中文符号 | → | ASCII |
|---------|---|-------|
| ，、 | → | ,  |
| 。 | → | . |
| （） | → | () |
| ： | → | : |
 | ！ | → | ! |
| ？ | → | ? |
| —— | → | -- |
| "" '' | → | " ' |

VS Code 会高亮中文标点，看着难受。教学内容的中文文字可以保留（如"贵州茅台"），但标点符号必须用 ASCII。

---

## 5. 文件结构现状

```
study_plan/
├── resources/
│   ├── 主脉络.md              ← 完整路线图（6阶段）
│   ├── lib/资源库.md           ← ⭐ 资源大全（B站/GitHub/书籍）
│   ├── 课程匹配度与AI量化分析.md  ← AI+量化调研
│   └── 招聘市场调研报告.md
├── docs/superpowers/plans/
│   └── 阶段1_Python_分脉络大纲.md  ← 阶段1详细计划（含依赖检查）
├── projects/python/tutorials/
│   ├── day01_Python起步.py    ✅ 206行
│   ├── day02_列表与字典.py     ✅ 622行（已补tuple+内置函数）
│   ├── day03_函数.py           ✅ 455行（用户练习完整）
│   └── day04_set文件异常.py    ⏳ 349行（模板，待用户做练习）
└── COLLEAGUES.md               ← 协作契约
```

---

## 6. 已知坑

| 坑 | 说明 |
|----|------|
| `f.write(content)` vs `f.write(fname)` | Hermes 的脚本 bug 导致 Day 01-04 被覆盖。教训：任何文件写入操作先 print 确认内容长度 |
| 四大基础类型 | list/dict/tuple/set 全了，set 在 Day 04 |
| 练习4和5之前是空的 | Claude Code 从 VS Code 本地历史恢复了用户写的练习 |
