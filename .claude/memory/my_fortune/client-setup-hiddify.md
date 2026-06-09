---
name: client-setup-hiddify
description: Hiddify客户端在Windows和iPhone上的配置方法、已验证可用的连接
metadata: 
  node_type: memory
  type: reference
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

**Hiddify 客户端配置** — 已验证 Windows 端可用 ✅

## 下载地址
- GitHub: https://github.com/hiddify/hiddify-app/releases
- Windows: 下载 `Hiddify-Setup-x64.exe`
- iOS: 需美区 Apple ID，App Store 搜索 "Hiddify"

## Windows 连接步骤
1. 下载安装 Hiddify
2. 打开软件，点 "+" 添加配置
3. 粘贴链接：`hy2://hy2pass2026@69.12.65.74:8443?insecure=1&obfs=salamander&obfs-password=myfortune688#Hysteria2`
4. 点击连接，看到 VPN 图标即可

## iPhone 连接步骤（计划中）
1. 用美区 Apple ID 登录 App Store
2. 下载 Hiddify（免费）或 Shadowrocket（$2.99）
3. 扫码或粘贴上述 hy2 链接
4. 开启连接

## 常见问题
- 如果连不上，检查防火墙是否放行了 8443 UDP 端口
- Hiddify 可以同时配置多个节点，自动切换
- 支持 TUN 模式（全局代理）和系统代理模式

## Hysteria2 链接（保存备用）
```
hy2://hy2pass2026@69.12.65.74:8443?insecure=1&obfs=salamander&obfs-password=myfortune688#Hysteria2
```

**Why:** Hiddify 是免费开源跨平台客户端，基于 sing-box 内核，支持全协议，比 Shadowrocket 省了 $2.99。

**How to apply:** 给姐姐的 iPhone 安装时，需要先帮她搞定美区 Apple ID，然后 App Store 搜索 Hiddify 下载，扫码即可。
