---
name: study-plan-architecture
description: "量化开发学习规划项目结构,2026年5月精简后"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4c8c7dd9-54ff-47b6-aa8c-24f7f0fadc59
---

项目路径 D:\Dev\AiProject\study_plan，结构：
- resources/ — 个人信息.md + 招聘市场调研报告.md + 主脉络.md（核心规划文档）
- projects/教程/ — 每日 Python 教程文件（day01_Python起步, day02_列表与字典...）
- projects/.vscode/ — C++ 开发配置
- projects/cpp_test.cpp — C++水平测试

当前进度（2026.5.25）：
- 阶段1 Python 进行中，5月26日正式开始
- 教程系统：Part 1 Python核心（共7天），Part 2 数据处理（7天），Part 3 项目（3天）
- 已清理：删除 Obsidian/notes/docs/skills_disabled 等冗余文件和配置

用户环境：Windows 11, VS Code, Python 3.13.5
学习方式：每日教程 .py 文件，C++类比教学
课程结构约定（2026.5.25 确定）：
- 格式：每讲完一个知识点 → 紧跟一个练习 → 再讲下一个 → 全部讲完 + 综合大练习
- 即：知识点1 → 练习1 → 知识点2 → 练习2 → ... → 综合练习
- 教学代码用字符串包裹（不执行），只有练习是可运行代码
- 教学字符串中所有自然语言文本必须用中文，不能出现英文单词（代码语法关键词除外）
- 每个练习留空注释引导，用户自己填代码
- 练习场景贴近量化开发（股票、持仓、价格数据处理）
- day01/02 已按此格式重写，后续课程沿用
