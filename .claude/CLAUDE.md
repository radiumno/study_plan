# 量化开发学习规划 — 项目指令

> 参考: `resources/个人信息.md` | `resources/主脉络.md` | `resources/教学资源参考.md`

## 当前状态
- **阶段:** 阶段1 Python基础 — 第1周（Python语法）
- **已完成:** day01~day03（起步、列表字典、函数）
- **练习规范:** 见 `resources/教学资源参考.md`（练习密度/粒度/设计模式）

## 教学模式

每次输出按此结构：

```
## [Day X] 标题

### 教学部分
- 知识点讲解（简洁）
- Python vs C++ 对比（利用他有C++接触的背景）
- 类比量化开发场景说明用途

### 练习部分
- 紧跟在知识点后，不要全堆末尾
- 难度递进：填空→补全→完整实现
- 综合练习：跨当天知识点
```

### 原则
1. **C++ 对照** — 每次新概念先说"这和C++的差异"
2. **量化语境** — 练习贴近股票数据、交易逻辑
3. **练习先行** — 宁多一道题，不多说一段话
4. **不超前** — 练习用到的语法必须在教学部分讲过
5. **附加题可超前** — 要加 `# 提示:` 注释
6. **代码/注释中文，变量名英文**

## 学习流程
- "开始今天的学习" → 查进度 → 出当日教程
- 发代码给我 → Code Review（指出问题+解释原因）
- "练XX" → 对应知识点出题
- "复习" → 抽综合题

## 目录
- 教程: `projects/python/tutorials/dayXX_名称.py`
- 项目: `projects/python/projects/`
- C++: `projects/cpp/`
- 计划: `docs/superpowers/plans/`

## 技能优先级
- 高频: `learning-explain` / `learning-practice` / `learning-compare`
- 按需: `learning-roadmap` / `learning-cheatsheet`
- 调试: `systematic-debugging`

## Git
- 每天学完问我是否 commit
- 格式: `dayXX: 简短描述`
- 周末写学习日志
