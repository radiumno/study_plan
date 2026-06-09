---
name: protocol-decision-log
description: VLESS Reality vs Hysteria2的决策记录和实际验证结果
metadata: 
  node_type: memory
  type: project
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**协议决策记录** — 为什么从 Reality 转向 Hysteria2 作为主力

## 最终结论
| 协议 | 当前状态 | 建议 |
|------|---------|------|
| **Hysteria2** | ✅ 完全可用 | **主力方案**，优先使用 |
| **VLESS Reality** | ⚠️ 服务端配置完成，客户端未通 | 备选方案，后续修复 |

## 为什么最开始选了 Reality？
最初调研全网资料，所有指南都推荐 Reality 作为"抗封锁最强协议"：
- 不需要域名和证书
- 伪装成正常 HTTPS 流量，借用大站 TLS 指纹
- 理论上是 2025-2026 年最安全的协议

## 实际遇到了什么坑？
1. **配置极其敏感** — shortId、publicKey、serverName 任何一个字符不对就连不上
2. **v2rayN 兼容性** — 7.22.3 版本 Reality 连接建立后页面不加载，日志显示 "REALITY: received real certificate"
3. **3X-UI 覆盖问题** — 面板每次重启会重新生成 config.json，覆盖手动修改
4. **调试困难** — 错误信息不够直观，反复试错效率低

## Hysteria2 为什么更合适当前场景？
1. **配置简单** — 一个密码搞定，没有密钥对、shortId 等复杂参数
2. **跨平台支持好** — Hiddify / Shadowrocket 都原生支持
3. **弱网优势** — 基于 QUIC，跨太平洋丢包环境下比 TCP 协议更稳定
4. **抗封锁够用** — 4人自用，流量不大，salamander 混淆足够绕过大网检测

## 未来方向
- Reality 可以继续调，但优先级低（Hysteria2 已经能正常工作）
- 如果未来 Hysteria2 被封锁，再启用 Reality 作为备用
- 最佳实践是双协议共存，客户端自动切换
