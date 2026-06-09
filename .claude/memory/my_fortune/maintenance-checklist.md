---
name: maintenance-checklist
description: 自建VPN的定期维护和故障排查清单
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**维护清单** — 保持 VPN 稳定运行需要做的事

## 每月检查
- [ ] VPS 是否欠费/到期（RackNerd 年付，记得到期前续费）
- [ ] 服务是否运行：`systemctl status hysteria-server`
- [ ] 查看是否有异常日志：`journalctl -u hysteria-server -n 20 --no-pager`
- [ ] 检查流量使用情况（RackNerd 后台）

## 每季度
- [ ] 更新 Hysteria2 到最新版
- [ ] 检查 BBR 是否启用：`lsmod | grep bbr`
- [ ] 检查磁盘空间：`df -h`
- [ ] 检查系统更新：`apt update && apt upgrade -y`

## 故障排查流程

### Hysteria2 连不上
1. 检查服务状态：`systemctl status hysteria-server`
2. 检查端口监听：`ss -tulpn | grep 8443`
3. 检查防火墙：`ufw status` 或 `iptables -L -n`
4. 重启服务：`systemctl restart hysteria-server`
5. 查看实时日志：`journalctl -u hysteria-server -f`

### 速度变慢
1. 切换 Hiddify 节点试试
2. 检查 BBR：`sysctl net.ipv4.tcp_congestion_control`
3. 检查 CPU/内存：`htop` 或 `free -h`
4. 可能是晚高峰拥堵，正常现象

### IP 被封锁
1. 用 ping.pe 测试国内是否可达
2. 确认被墙 → 联系 RackNerd 客服换IP（$3/次）
3. 或加 Cloudflare CDN 中转恢复

## 关键命令速查
```bash
# 连服务器
ssh root@69.12.65.74

# Hysteria2
systemctl restart hysteria-server
journalctl -u hysteria-server -f

# Xray (Reality)
systemctl restart vless-xray
journalctl -u vless-xray -f

# 3X-UI 面板
x-ui
```

## 紧急情况
- 服务器宕机 → RackNerd 后台 SolusVM 面板重启
- 系统崩溃 → RackNerd 后台重装系统，然后重新装服务
- IP被墙 → 联系客服换IP或套CDN
