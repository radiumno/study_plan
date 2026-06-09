---
name: server-config-vless-reality
description: VLESS Reality服务端配置、已知问题和待修复项
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**VLESS Reality 服务器配置** — ⚠️ 服务端已部署，客户端连接未验证通过

## 连接信息
```
地址: 69.12.65.74
端口: 443 (TCP)
协议: VLESS
UUID: 9ad07c22-9428-48e9-8580-c8286c3c1c87
Flow: xtls-rprx-vision
加密: none
传输: tcp
安全: reality
Dest: dl.google.com:443
ServerNames: ["dl.google.com"]
PrivateKey: QLZ7XaiP4gMQ_9ujd_YApztsPu1adFImIWSJINbjd1A
PublicKey: McdR--DSeCIgaLrKhDRpGxW3YRhKUbj8ymgF-iHGlUk
ShortIds: ["", "4ea7556c8e67ef93"]
Fingerprint: chrome
```

## VLESS链接
```
vless://9ad07c22-9428-48e9-8580-c8286c3c1c87@69.12.65.74:443?security=reality&encryption=none&pbk=McdR--DSeCIgaLrKhDRpGxW3YRhKUbj8ymgF-iHGlUk&fp=chrome&type=tcp&flow=xtls-rprx-vision&sni=dl.google.com&sid=#VLESS-Reality
```

注意：链接中不含 sid 参数（之前 shortId 有兼容性问题）

## 服务端配置 (`/usr/local/x-ui/bin/config.json`)
```json
{
  "log": {"loglevel": "warning"},
  "inbounds": [{
    "tag": "vless-reality",
    "port": 443,
    "protocol": "vless",
    "settings": {
      "clients": [{"id": "9ad07c22-9428-48e9-8580-c8286c3c1c87", "flow": "xtls-rprx-vision", "email": "user@test.com"}],
      "decryption": "none"
    },
    "streamSettings": {
      "network": "tcp",
      "security": "reality",
      "realitySettings": {
        "dest": "dl.google.com:443",
        "serverNames": ["dl.google.com"],
        "privateKey": "QLZ7XaiP4gMQ_9ujd_YApztsPu1adFImIWSJINbjd1A",
        "shortIds": ["", "4ea7556c8e67ef93"],
        "fingerprint": "chrome",
        "publicKey": "McdR--DSeCIgaLrKhDRpGxW3YRhKUbj8ymgF-iHGlUk"
      },
      "sockopt": {"tcpFastOpen": 3, "tcpKeepAliveInterval": 90}
    },
    "sniffing": {"enabled": true, "destOverride": ["http", "tls"]}
  }],
  "outbounds": [
    {"protocol": "freedom", "tag": "direct"},
    {"protocol": "blackhole", "tag": "blocked"}
  ],
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      {"ip": ["geoip:private"], "outboundTag": "blocked", "type": "field"},
      {"protocol": ["bittorrent"], "outboundTag": "blocked", "type": "field"}
    ]
  }
}
```

## 已知问题
1. **v2rayN连接失败** — 客户端能与服务器建立TCP连接（log显示"accepted tcp"），但浏览器无法加载页面。疑似 Reality 认证握手或响应回传问题
2. **"REALITY: received real certificate"** — 客户端收到目标网站真实证书而非 Realm 临时证书，说明客户端配置（shortId/公钥/时间差）仍有问题
3. **3X-UI覆盖问题** — 3X-UI面板会从数据库重新生成 config.json，覆盖手动修改。已在 `/etc/systemd/system/vless-xray.service` 创建独立服务绕过此问题

## 独立服务
```
[Unit]
Description=VLESS Reality Xray Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/local/x-ui/bin/xray-linux-amd64 run -c /usr/local/x-ui/bin/config.json
Restart=on-failure
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

## 维护命令
```bash
# 启动/停止独立服务
systemctl start vless-xray
systemctl stop vless-xray
systemctl restart vless-xray

# 查看日志
journalctl -u vless-xray -n 50 --no-pager

# 如果要用3X-UI面板（会覆盖配置）
x-ui
```

**Why:** VLESS Reality 是当前抗封锁能力最强的协议，作为 Hysteria2 的 TCP 补充方案。

**How to apply:** 如需修复客户端连接问题，需检查：①服务器和客户端系统时间同步 ②publicKey/privateKey匹配 ③客户端 shortId 配置 ④尝试不同 dest 目标站
