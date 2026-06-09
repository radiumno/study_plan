---
name: vps-racknerd-details
description: RackNerd VPS的具体配置、费用、维护和升级方案
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**RackNerd VPS 详情** — 当前测试用节点

## 当前配置
```
提供商:   RackNerd
机房:     Los Angeles DC-03
IP:       69.12.65.74
配置:     1 vCPU, 1GB RAM, 25GB SSD
流量:     2TB/月 @ 1Gbps
费用:     ~$10.6/年 (年付)
状态:     ✅ 运行中
```

## SSH 连接
```
ssh root@69.12.65.74
```
密码见 RackNerd 后台 my.racknerd.com

## 已安装服务
- **3X-UI** (Web面板，已停止，避免覆盖配置)
- **Hysteria2** (systemd 服务，运行中)
- **Xray-core** (独立 vless-xray 服务，可单独启停)
- **BBR** 拥塞控制 (需确认是否启用)

## 升级方案
当前至多支持4个人轻度使用。如果后期不够：
- **方案A**: 同配置续费 $10.6/年，够用就保持
- **方案B**: 升级到 $21.99/年 (2 vCPU, 2GB, 40GB SSD, 4TB)
- **方案C**: 不够用但不想换机器 → 加第二台 RackNerd 分摊流量

## 换IP政策
购买后72小时内可免费换IP一次（需联系客服）。
超过72小时需付费 $3/次。

## 注意事项
- LA到中国延迟约160-310ms，属于正常范围
- 机房IP（非住宅IP）数据中心段，自用4人不影响外贸业务
- 高峰期可能降速，此时切换 Hysteria2 可缓解

**Why:** 记录 VPS 具体信息方便续费、升级、故障排查。

**How to apply:** 每年到期前续费，如需升级去 my.racknerd.com 操作。
