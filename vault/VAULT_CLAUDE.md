# Vault 操作手册 (for Claude Code)

## 结构说明

```
00_OS/          系统文件 — vault 配置、模板、目录索引
10_RAW/         原始材料 — 会话记录、代码片段、未整理笔记
  会话记录/       每轮对话的时间线记录
  代码片段/       教学中的代码示例和技巧
20_WIKI/        编译知识 — 经整理的概念笔记、教训、进度
  量化知识点/     核心量化概念、代码模式、最佳实践
  坑与教训/      踩过的坑、错误代码、为什么出错
  课程进度/      学习进度、掌握程度、薄弱环节
30_OUTPUTS/     产出物 — 生成的回答、报告、可视化
```

## 目录结构 = 数据库 schema

- 每个文件夹是一个 collection
- 每个 .md 文件是一条 record
- YAML frontmatter 提供列 (tags/type/status/date)

## 命名规则

- 文件名: `YYYY-MM-DD_简短描述.md` (会话记录)
- 文件名: `英文或中英简短描述.md` (知识点/教训)
- 避免空格，用下划线

## Frontmatter 模板

```yaml
---
title: 标题
type: concept|lesson|mistake|progress|session|code
tags: []
date: YYYY-MM-DD
status: draft|active|reviewed
source: claude|user
---
```

## 规则

1. **source: claude** — 我写的笔记标记 source: claude
2. **source: user** — 用户说的内容标记 source: user
3. **20_WIKI/ 是活文档** — 可以修改、合并、补充
4. **10_RAW/ 不可变** — 原始记录不删不改，只追加
5. **一笔记一概念** — 一个知识点一个文件
6. **交接文件** — 每次会话结束更新 `会话交接.md`
