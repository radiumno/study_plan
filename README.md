# Quant Developer Study Plan

面向数据科学本科生的量化开发学习仓库。

主线:

```
Python数据闭环
  -> 现代C++ + 数据结构算法
  -> Linux / 测试 / 调试 / 性能
  -> 并发 / 网络 / SQL / 市场微观结构
  -> 回测引擎
  -> 交易链路模拟器
  -> 实习与求职
```

AI作为工具和定向分支，不占固定学习比例。

## 当前状态

- 当前阶段: 阶段1 Python数据闭环
- 精确进度: 以 `vault/会话交接.md`、当前课程文件和Code Review结果为准
- 路线总览: `resources/主脉络.md`
- 阶段计划: `docs/plans/阶段1_Python_分脉络大纲.md`

## 项目层级

| 层级 | 目录/文件 | 作用 |
|------|-----------|------|
| 证据 | `resources/招聘市场调研报告.md`、`resources/核心学习资源清单.md` | 岗位与资源事实 |
| 战略 | `resources/主脉络.md` | 阶段顺序和里程碑 |
| 执行 | `docs/plans/` | 阶段计划和滚动日计划 |
| 课程 | `projects/python/` | 教学与练习主产物 |
| 状态 | `vault/会话交接.md` | 实时进度和下一步 |
| 展示 | `docs/resources/`、`docs/tutorials/` | 自动生成的文档站镜像 |

详细规则见 `docs/plans/规划层级与滚动执行规则.md`。

## 目录

| 路径 | 是否手改 |
|------|----------|
| `projects/python/` | 是 |
| `resources/` | 是 |
| `docs/plans/` | 是 |
| `docs/workflows/` | 是 |
| `docs/references/` | 是 |
| `vault/` | 是 |
| `docs/resources/` | 否，由脚本生成 |
| `docs/tutorials/` | 否，由脚本生成 |

## 六阶段路线

| 阶段 | 内容 | 核心产出 |
|------|------|----------|
| 1 | Python数据处理与工程基础 | 股票分析工具 |
| 2 | 现代C++、DSA、Linux/CMake/gtest | C++题解与交易数据结构 |
| 3 | 所有权、内存、并发、性能 | 市场数据回放项目 |
| 4 | 网络、SQL、微观结构、回测与交易链路 | 两个核心C++项目 |
| 5 | 实习或等价真实协作 | 可验证经历 |
| 6 | 定向补强、考研、求职 | 面试级项目集 |

## 课程规则

- 课程状态: `计划中 -> 课程已写 -> 学习中 -> 待Review -> Review通过/返工`
- 课程写完不等于用户学完。
- 每个Day先做学习量和依赖校准。
- 示例后练习必须发生迁移。
- 知识块总练习必须是新的完整场景。
- 用户已填写的练习不得自动覆盖或清空。

## 快速开始

```bash
git clone https://github.com/radiumno/study_plan.git
cd study_plan
python3 scripts/checks.py bootstrap
python3 scripts/checks.py status
```

## 统一检查

```bash
python3 scripts/checks.py list
python3 scripts/checks.py status
python3 scripts/checks.py plans
python3 scripts/checks.py docs
python3 scripts/checks.py course
python3 scripts/checks.py tests
python3 scripts/checks.py health
```

| 命令 | 用途 |
|------|------|
| `status` | 查看环境、镜像和工作树 |
| `plans` | 检查规划口径和必需章节 |
| `docs` | 同步并验证文档站 |
| `course` | 检查课程硬规则 |
| `tests` | 脚本回归测试 |
| `health` | 全量检查 |

## 文档站

```bash
pip install mkdocs mkdocs-material
python3 scripts/checks.py docs
mkdocs serve
```

`docs/resources/` 和 `docs/tutorials/` 只由 `scripts/sync_docs.py` 生成，不手改。

## Git Hooks

```bash
python3 scripts/checks.py install-hooks
```

- pre-commit: 脚本测试
- pre-push: 全量健康检查

## 课程答案归档

只有需要重新生成干净教学模板时才使用:

```bash
python3 scripts/archive_and_clear_filled_exercises.py stage1
python3 scripts/archive_and_clear_filled_exercises.py stage2
```

脚本会先把已填写版本归档到 `vault/10_RAW/代码片段/filled_course_snapshots/`。
