---
name: self-update
description: >
  Automatically check for new Claude Code skills, MCP servers, tools and tutorials
  from GitHub trending, community repos, and other sources. Keeps the setup current.
---

# Self-Update

定期扫描优质资源渠道，发现新的 Claude Code skills、MCP 服务器、学习资料和开发工具，并更新本地配置。

## Check Frequency

- **每次会话启动时** — 快速检查已知源是否有更新
- **每周** — 全面扫描所有源
- **用户触发 `/self-update`** — 立即执行完整扫描

## Sources

### Tier 1: 必须检查

| 源 | 内容 | 频率 |
|----|------|------|
| [GitHub Trending (monthly)](https://github.com/trending?since=monthly) | 当月热门仓库 | 每次 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 新 Claude Code skills | 每周 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Claude 官方插件 | 每周 |

### Tier 2: 定期检查

| 源 | 内容 | 频率 |
|----|------|------|
| GitHub Trending (weekly) | 当周热门 | 每周翻一次 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 新 MCP 服务器 | 每周 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP 服务器精选列表 | 每周 |
| PyPI / npm 上的新工具 | 开发工具链 | 每月 |

## Process

### Phase 1: 扫描 GitHub Trending

```bash
curl -s "https://api.github.com/search/repositories?q=created:>$(date -v-30d '+%Y-%m-%d')&sort=stars&order=desc&per_page=10"
```

筛选条件：
- 和 Python / TypeScript / AI / 量化 / 学习 相关
- Stars > 1000
- 不是纯玩具项目

### Phase 2: 检查已知源更新

对每个已安装的仓库运行 `git pull --ff-only`，看是否有更新。

### Phase 3: 比对本地技能列表

1. 列出 `~/.claude/skills/` 和 `~/Projects/study_plan/.claude/skills/` 中已有的 skills
2. 检查 mattpocock/skills 和 academic-research-skills 是否有新 skill 没装
3. 标记可安装的新 skill

### Phase 4: 报告

输出格式：

```
📡 Self-Update Report — 2026-06-11

🆕 新发现:
  - [库名] ⭐ 5k — 简短说明
  - [skill名] — 来源

📦 有更新的仓库:
  - mattpocock/skills: 3 个新 skill 可用

📌 建议安装:
  /install <name>
```

## Output

- 有重要更新时：主动向用户报告
- 常规更新（只有小改动）：记录到 memory，下次主动问用户
- 无更新：静默跳过

## Note

本 skill 本身也可以自我更新 — 如果发现更好的扫描策略或新源，更新自身 SKILL.md 并记录到 memory。
