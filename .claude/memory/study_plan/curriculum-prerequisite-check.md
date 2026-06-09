---
name: curriculum-prerequisite-check
description: 课程设计必须做前置依赖检查，新知识点所用到的类型/概念必须在之前教过
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

每个教学 day 用到的基础类型和概念，必须在当前 day 或之前 day 教过。不能出现 Day 03 用元组但 Day 02 没讲的情况。

具体规则:
1. 写教程前，列出当天会用到的所有 Python 类型和语法，逐条核对是否已教
2. 如果某个概念是前置依赖但漏了，先补到对应 day，再往后推进
3. 答疑时必须遵守教学模式（知识点→C++对比→量化场景→练习），不能因为"只是回答一个问题"就跳过格式

**Why:** Day 03 `*args` 返回元组，但 Day 02 列表/字典里漏了元组。用户问"*是数组吗"暴露了两个问题：(1) 课程设计漏了元组这个前置知识，(2) 答疑时直接用表格简化回答，没按教学模式来。

**How to apply:** 每次写新 day 教程前，列一张"本 day 依赖清单"，和已教清单做 diff。已教清单从历史教程文件头部或 git log 获取。答疑时就算只是一个小问题，也按知识点→C++对比→量化场景的结构回答。
