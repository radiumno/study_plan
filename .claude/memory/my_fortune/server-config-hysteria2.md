---
name: server-config-hysteria2
description: Hysteria2服务端配置、部署方式和维护命令
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**Hysteria2 服务器配置** — 已验证可用 ✅

## 连接信息
```
地址: 69.12.65.74
端口: 8443 (UDP)
密码: hy2pass2026
混淆: salamander
混淆密码: myfortune688
TLS: 自签证书 (insecure=1)
```

## 链接（可直接导入客户端）
```
hy2://hy2pass2026@69.12.65.74:8443?insecure=1&obfs=salamander&obfs-password=myfortune688#Hysteria2
```

## 服务端配置 (`/etc/hysteria/config.yaml`)
```yaml
listen: :8443
auth:
  type: password
  password: hy2pass2026
obfs:
  type: salamander
  salamander:
    password: myfortune688
tls:
  cert: /etc/hysteria/cert.pem
  key: /etc/hysteria/key.pem
bandwidth:
  up: 100 mbps
  down: 200 mbps
```

## 维护命令
```bash
# 查看服务状态
systemctl status hysteria-server

# 重启服务
systemctl restart hysteria-server

# 查看日志
journalctl -u hysteria-server -n 50 --no-pager

# 查看实时日志
journalctl -u hysteria-server -f
```

## TLS证书说明
使用自签证书（`/etc/hysteria/cert.pem`、`/etc/hysteria/key.pem`），客户端需开启 `insecure=1`（跳过证书验证）。

## 服务文件
`/etc/systemd/system/hysteria-server.service`

**Why:** Hysteria2 基于 QUIC 协议，在跨太平洋高延迟弱网环境下表现优秀，是当前主力可用方案。

**How to apply:** 重启服务用 `systemctl restart hysteria-server`，修改配置后也需重启。
