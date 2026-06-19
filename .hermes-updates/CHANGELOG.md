# Hermes 操作日志

> 仅记录与 study_plan 学习项目直接相关的操作，供 Claude Code 同步。

---

## 2026-06-15

### 1. 进度审计与修复
- **发现的问题：** Day 04 细脉络标记为"⚠️练习待续"，实际已全部完成；Day 08 实际已完成但三处进度文件都标记为"待续/预告"
- **修复文件：**
  - `resources/主脉络.md` — `Day08待续` → `Day08 ✅`，课程列表加 Day 08
  - `.claude/CLAUDE.md` — `Day 08 预告` → `Day 08 ✅`，"已完成"加 day08
  - `docs/plans/阶段1_Python_分脉络大纲.md` — `Day 04 ⚠️` → `Day 04 ✅`，Part 2 加 `Day 08 ✅`
- **清理：** 删除 `~/study_plan` 空文件（真实项目在 `~/Projects/study_plan/`）
- **提交：** `0c2b7c0 fix: 更新进度跟踪`

### 2. Day 08R (NumPy强化课) 修复
- **Bug 1:** `mask_not_both` 变量未定义 → 删除相关 print
- **Bug 2:** `returns[4:][signals==1]` 形状不匹配（96 vs 95）→ 改用 `signals[:-1]`
- **提交：** 随 `6802bf4` 一起提交

### 3. Day 09 审查与修复
- **问题 1:** 练习5.1 拉 `600519.SS`（A股），yfinance 国内用不了 → 改为 AAPL，加 WARP 提示
- **问题 2:** yfinance 多股票返回 MultiIndex，Day 09 没教 → 加注释解释多级列名
- **问题 3:** 无 NaN 处理提示 → 加 `.dropna()` 和 `.isna()` 教学
- **问题 4:** 综合练习步骤4要求"月均价"，但 `resample` 是 Day 10 内容 → 标为选做
- **提交：** `6802bf4 fix: Day 09 审查修复`

### 4. course-writing SKILL.md 优化（10项改进）
- Step 7「问 commit」vs CLAUDE.md「不再问」的矛盾 → 改为 Step 0/9 自动 commit
- 删除 Python vs C++ 对比要求（memory 已说不需要）
- 引用路径从旧 MEMORY.md 改为 `memory/` 目录
- 新增三层复习机制 Step 5、四层练习结构、yfinance 安全三原则、反向检查清单 Step 7（8项）
- 新增课前 checkpoint、技能交叉引用表
- 文件：`.claude/skills/course-writing/SKILL.md`

### 5. 其他修复
- `.claude/skills/self-update/SKILL.md` — 路径 `~/study_plan` → `~/Projects/study_plan`
- `.claude/memory/teaching-explain-every-step.md` — C++ 对比规则从"全部删除"改为"Python阶段不用，C++阶段再用"
- `.claude/memory/day09-review-lessons.md` — 新建，记录 Day 09 审查教训（5条）

---

## 2026-06-16

### 6. Agent-Reach 安装（增强 Claude Code 联网能力）
- 安装 `agent-reach v1.5.0` + 依赖（yt-dlp, feedparser, rich等）
- 激活 6/13 个渠道（GitHub/YouTube/RSS/网页搜索/B站/网页读取）
- 配置雪球 Cookie（A股行情直连，无需yfinance）
- 配置小宇宙播客转录脚本
- skill 已安装到 `~/.claude/skills/agent-reach/`，Claude Code 自动加载
- 安装 tmux（用于后续 Claude Code 协同写课）

---

## 2026-06-20

### 7. Day 10 (Pandas进阶) 审查
- 审查 `projects/python/tutorials/day10_Pandas进阶.py`（705行）
- 代码跑通无报错 ✅
- 金叉/死叉提示补全完整条件（第670-671行）
- 综合练习"最大回撤"标为选做（第689行）
- 注意：Day 10 已将 yfinance 替换为离线模拟数据

### 8. 免费A股数据源调研
- yfinance 在国内不可用
- 推荐替代：**AKShare**（`pip install akshare`，免费零注册）、**Baostock**、**腾讯财经直连**
- 详情见 `data_source_summary.md`（项目外，需另取）

### 9. 资源库优化
- 更新 `resources/lib/资源库.md`，新增7个2026年资源：

| 新增资源 | 方向 | 说明 |
|---------|------|------|
| Hello 算法 ⭐127k | C++数据结构 | 动画图解+12种语言，最适合入门 |
| AKShare ⭐19.8k | A股数据源 | 替代yfinance，国内直连 |
| Stoke (mootdx TCP) | A股数据源 | 通达信直连，不限流 |
| ai-agents-from-zero | AI Agent | 系统Agent速成+面试题库 |
| hello-agents ⭐40k | AI Agent | Datawhale出品，从零搭框架 |
| Vibe-Trading ⭐12.6k | AI+量化 | 港大2026，LLM驱动量化分析 |
| awesome-quant-interview | 面试准备 | 55道量化高频考点 |

- **提交：** `9ebb5fe chore: 更新资源库`，`03988cb docs: 新建CHANGELOG`
