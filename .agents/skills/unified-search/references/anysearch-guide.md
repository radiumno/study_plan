# AnySearch API 使用指南

## 概述

AnySearch 是一个集中式搜索 API 服务，提供垂直领域搜索、批量搜索和 URL 内容提取功能。
将其与直连搜索引擎结合，可大幅提升特定场景的搜索质量。

## 启用方式

1. 获取 AnySearch API Key（从 https://anysearch.ai 或项目维护者）
2. 编辑 `config.json`，填入 Key：

```json
{
  "anysearch": {
    "api_key": "your-api-key-here",
    "endpoint": "https://api.anysearch.ai/v1"
  }
}
```

3. 配置后，Skill 会自动识别并使用 AnySearch 增强深度查询。

## 垂直领域搜索

针对特定领域获取更精准的结果：

| 领域 | 参数值 | 场景 |
|------|--------|------|
| 新闻 | `domain=news` | 最新事件、时事报道 |
| 学术 | `domain=academic` | 论文、研究、引用 |
| 社交 | `domain=social` | 论坛讨论、社交媒体 |
| 代码 | `domain=code` | GitHub、技术文档、API |
| 购物 | `domain=shopping` | 产品规格、价格比较 |
| 视频 | `domain=video` | 视频内容搜索 |
| 图片 | `domain=image` | 图片与视觉内容 |

### 请求格式

```
GET {endpoint}/search?q={keyword}&domain={domain}&limit={count}
```

### 参数说明

- `q` — 搜索关键词（必需）
- `domain` — 垂直领域（可选，默认 general）
- `limit` — 返回条数（可选，默认 10）
- `language` — 语言过滤（可选，如 zh, en）
- `time_range` — 时间范围（可选，如 7d, 30d, 1y）

## 批量并行搜索

同时搜索多个相关关键词，适合复杂调研。

### 请求格式

```
POST {endpoint}/batch
Content-Type: application/json

{
  "queries": ["query1", "query2", "query3"],
  "domain": "news",
  "limit": 5
}
```

## URL 内容提取

获取指定 URL 的正文内容，用于深度阅读。

### 请求格式

```
GET {endpoint}/extract?url=https://example.com/article
```

### 返回格式

```json
{
  "url": "https://example.com/article",
  "title": "Article Title",
  "content": "Article main text...",
  "author": "Author Name",
  "published": "2026-01-01",
  "domain": "example.com"
}
```

## 不使用 API Key 时的行为

如果 `api_key` 为空或未配置：
- Skill 完全以降级模式运行
- 所有查询只使用 16 个直连引擎
- 功能不受影响，只是没有垂直领域优化
- 在结果中会标注 "Direct Only" 模式

## 与直连引擎的配合

AnySearch 和直连引擎不是二选一，而是互补：

```
复杂调研流程：
1. 直连引擎快速初筛 → 找出可能相关的方向
2. AnySearch 垂直搜索 → 深入特定领域
3. 直连引擎补充 → 交叉验证结果
4. AnySearch URL 提取 → 深度阅读关键文章
```
