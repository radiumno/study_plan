---
name: vpn-guide-foreign-trade
description: 自建外贸VPN项目概览，当前状态和核心事实
metadata: 
  node_type: memory
  type: project
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

# 自建外贸VPN项目

**项目状态**: ✅ Hysteria2 已可用，Reality 待调试，姐姐未上线

## 核心事实
- VPS: RackNerd LA DC-03, 69.12.65.74, $10.6/年
- 主力协议: Hysteria2 (UDP 8443, 已可用)
- 备选协议: VLESS Reality (TCP 443, 服务端已配，客户端未通)
- Windows客户端: Hiddify (已验证可用)
- iPhone客户端: 计划用 Hiddify/Shadowrocket (需美区 Apple ID)
- 使用人数: 4人（姐姐 + 姐夫 + 哥哥 + 姐姐合伙人）
- 用途: Facebook, WhatsApp, Instagram 外贸业务

## 关键文档
- [server-config-hysteria2](server-config-hysteria2.md) — Hysteria2 配置
- [server-config-vless-reality](server-config-vless-reality.md) — Reality 配置
- [client-setup-hiddify](client-setup-hiddify.md) — 客户端设置
- [vps-racknerd-details](vps-racknerd-details.md) — VPS详情
- [protocol-decision-log](protocol-decision-log.md) — 协议决策记录
- [maintenance-checklist](maintenance-checklist.md) — 维护清单
- [sister-onboarding-plan](sister-onboarding-plan.md) — 姐姐上线计划
- [lessons-learned](lessons-learned.md) — 经验教训
