---
name: "unified-search"
description: "Unified search combining 16 direct engines (7 CN + 9 global) + optional AnySearch API for vertical/batch/domain search. Auto mode selection: direct engines for general queries, AnySearch for deep domain search. No API key required for basic use."
---

# Unified Search

将 multi-search-engine 的 16 个直连引擎与 AnySearch API 整合为一，根据查询类型自动选择最优搜索路径。

## 架构

```
用户查询
  ├── 简单/普通查询 ──→ 直连引擎模式 (16 engines, 无需 Key)
  │                     ├── 中文 → 7 个国内引擎
  │                     └── 英文 → 9 个国际引擎
  └── 深度/领域查询 ──→ AnySearch API 模式 (需配置 Key)
                        ├── 垂直领域搜索 (news/academic/social...)
                        ├── 批量并行搜索
                        └── URL 内容提取
```

## 快速开始

### 无需配置：直接使用 16 引擎

```
web_fetch({"url": "https://www.google.com/search?q=python+tutorial"})
web_fetch({"url": "https://www.baidu.com/s?wd=python教程"})
```

### 启用 AnySearch 增强（可选）

在 `config.json` 中配置 API Key：

```json
{
  "anysearch": {
    "api_key": "your-key-here",
    "endpoint": "https://api.anysearch.ai/v1"
  }
}
```

## 工作流

### Phase 1: 查询分析

1. **检测查询类型**：
   - **语言**: 中文 → 国内引擎优先；英文 → 国际引擎优先
   - **深度**: 是否需垂直领域搜索（学术、新闻、代码等）
   - **范围**: 简单关键词 vs 复杂多维度查询

2. **路由决策**：
   - 简单查询（1-2 个关键词、普通信息检索）→ **直连引擎模式**
   - 深度查询（需精确结果、特定领域、批量对比）→ **AnySearch 模式**（如已配置）
   - 无 AnySearch Key → **强制直连引擎模式**（全功能可用）

### Phase 2: 直连引擎模式（multi-search-engine 继承）

完整继承原有 16 引擎能力：

1. **引擎选择**：
   - 中文查询：Baidu, Bing CN, Bing INT, 360, Sogou, WeChat, Shenma
   - 英文查询：Google, Google HK, DuckDuckGo, Yahoo, Startpage, Brave, Ecosia, Qwant, WolframAlpha

2. **执行策略**：
   - 请求间添加 1-2 秒延迟
   - 每批 3-4 个引擎，批次间顺序执行
   - 标准浏览器 User-Agent
   - 遇 403/429 时自动获取 Cookie 后重试

3. **结果聚合**：去重、排序、总结

### Phase 3: AnySearch 模式（增强）

当 AnySearch 已配置且查询适合时启用：

1. **垂直领域搜索**（指定 domain 获得更精准结果）：
   - `news` — 新闻和最新事件
   - `academic` — 学术论文和研究
   - `social` — 社交媒体内容
   - `code` — 代码和技术文档
   - `shopping` — 产品与购物
   - `video` — 视频内容
   - `image` — 图片搜索

2. **批量并行搜索**（一个请求多个查询）：
   同时搜索多个相关关键词，适合复杂调研场景。

3. **URL 内容提取**：
   获取指定 URL 的正文内容，用于深度阅读。

4. **回退机制**：AnySearch 失败时自动降级到直连引擎。

### Phase 4: 结果整合

- 来自两种模式的结果统一格式输出
- 标记来源（Direct / AnySearch）
- 按相关性排序，去重

## 配置项

| 配置 | 路径 | 必需 | 说明 |
|------|------|------|------|
| `anysearch.api_key` | `config.json` | 否 | AnySearch API Key，不配则只用直连引擎 |
| `anysearch.endpoint` | `config.json` | 否 | API 端点，默认 `https://api.anysearch.ai/v1` |
| `anysearch.timeout` | `config.json` | 否 | 请求超时（毫秒），默认 15000 |
| `direct.delay_ms` | `config.json` | 否 | 直连引擎间隔，默认 1200 |
| `direct.batch_size` | `config.json` | 否 | 每批引擎数，默认 3 |

## 快速示例

### 直连引擎（无需 Key）

```javascript
// 普通搜索
web_fetch({"url": "https://www.google.com/search?q=rust+programming"})
web_fetch({"url": "https://cn.bing.com/search?q=机器学习"})

// 站点限定
web_fetch({"url": "https://www.google.com/search?q=site:github.com+deno"})

// 隐私搜索
web_fetch({"url": "https://duckduckgo.com/html/?q=private+search"})

// 知识计算
web_fetch({"url": "https://www.wolframalpha.com/input?i=integrate+x%5E2+dx"})

// 时间过滤（过去一周）
web_fetch({"url": "https://www.google.com/search?q=AI+news&tbs=qdr:w"})
```

### AnySearch API（需 Key）

当 `config.json` 中配置了 `api_key` 后，可使用增强搜索：

```javascript
// 垂直领域搜索（新闻）
// GET {endpoint}/search?q=keyword&domain=news

// 垂直领域搜索（学术）
// GET {endpoint}/search?q=machine+learning&domain=academic

// URL 内容提取
// GET {endpoint}/extract?url=https://example.com/article

// 批量搜索
// POST {endpoint}/batch
// Body: {"queries": ["query1", "query2"], "domain": "news"}
```

## 引擎列表

### 国内引擎（7）
| 引擎 | URL |
|------|-----|
| Baidu | `https://www.baidu.com/s?wd={keyword}` |
| Bing CN | `https://cn.bing.com/search?q={keyword}&ensearch=0` |
| Bing INT | `https://cn.bing.com/search?q={keyword}&ensearch=1` |
| 360 | `https://www.so.com/s?q={keyword}` |
| Sogou | `https://sogou.com/web?query={keyword}` |
| WeChat | `https://wx.sogou.com/weixin?type=2&query={keyword}` |
| Shenma | `https://m.sm.cn/s?q={keyword}` |

### 国际引擎（9）
| 引擎 | URL |
|------|-----|
| Google | `https://www.google.com/search?q={keyword}` |
| Google HK | `https://www.google.com.hk/search?q={keyword}` |
| DuckDuckGo | `https://duckduckgo.com/html/?q={keyword}` |
| Yahoo | `https://search.yahoo.com/search?p={keyword}` |
| Startpage | `https://www.startpage.com/sp/search?query={keyword}` |
| Brave | `https://search.brave.com/search?q={keyword}` |
| Ecosia | `https://www.ecosia.org/search?q={keyword}` |
| Qwant | `https://www.qwant.com/?q={keyword}` |
| WolframAlpha | `https://www.wolframalpha.com/input?i={keyword}` |

## AnySearch 垂直领域

| 领域 (domain) | 适用场景 |
|---------------|----------|
| `news` | 最新新闻、时事 |
| `academic` | 学术论文、研究 |
| `social` | 社交媒体、讨论 |
| `code` | 代码、技术文档 |
| `shopping` | 产品信息、比价 |
| `video` | 视频内容搜索 |
| `image` | 图片搜索 |

## 高级操作符（直连引擎）

| 操作符 | 示例 | 说明 |
|--------|------|------|
| `site:` | `site:github.com python` | 限定站点 |
| `filetype:` | `filetype:pdf report` | 文件类型 |
| `""` | `"machine learning"` | 精确匹配 |
| `-` | `python -snake` | 排除词 |
| `OR` | `cat OR dog` | 或逻辑 |

## 时间过滤（Google）

| 参数 | 说明 |
|------|------|
| `tbs=qdr:h` | 过去一小时 |
| `tbs=qdr:d` | 过去一天 |
| `tbs=qdr:w` | 过去一周 |
| `tbs=qdr:m` | 过去一月 |
| `tbs=qdr:y` | 过去一年 |

## 隐私引擎

- **DuckDuckGo**: 无追踪，支持 !bang 快捷指令
- **Startpage**: Google 结果 + 隐私保护
- **Brave**: 独立索引
- **Qwant**: EU GDPR 合规

## DuckDuckGo Bangs

| Bang | 目标 |
|------|------|
| `!g` | Google |
| `!gh` | GitHub |
| `!so` | Stack Overflow |
| `!w` | Wikipedia |
| `!yt` | YouTube |

## 模式选择指南

| 场景 | 推荐模式 | 原因 |
|------|----------|------|
| 快速查资料 | 直连引擎 | 无需配置，即时响应 |
| 中文内容 | 直连引擎（国内组） | 百度/360 覆盖更好 |
| 学术研究 | AnySearch academic | 更精准的论文结果 |
| 最新新闻 | AnySearch news | 实时新闻聚合 |
| 代码搜索 | AnySearch code | 技术内容优化 |
| 隐私敏感 | 直连引擎（DuckDuckGo/Brave） | 无追踪 |
| 数学/计算 | 直连引擎（WolframAlpha） | 知识计算引擎 |
| 多角度调研 | AnySearch batch | 批量并行搜索 |
| 深度阅读 | AnySearch extract | URL 内容提取 |

## 安全与隐私

### Cookie 处理
- Cookie 仅在运行时内存中维护
- 遇 403/429 时按需获取
- 搜索会话结束后立即清除
- 不持久化到磁盘

### 抓取伦理
- 请求间保持 1-2 秒延迟
- 遵守搜索引擎爬虫策略
- 用于合法搜索聚合，非批量数据抓取

### AnySearch API
- API Key 仅存储在本地 config.json
- 请求通过 HTTPS 加密传输
- 不保留查询历史

## 文档

- `references/advanced-search.md` — 国内搜索引擎使用指南
- `references/international-search.md` — 国际搜索引擎使用指南
- `config.json` — 引擎配置和 AnySearch 设置

## License

MIT
