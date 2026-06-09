---
name: lessons-learned
description: 搭建过程中踩过的坑和关键经验总结
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 20815c7c-9874-4c5f-88b8-e6f60a8f03aa
---

## 搭建经验总结

### 1. 先验证再规划
- 最初花大量时间做文档（`docs/自建外贸VPN完全指南.md` 等），但实际动手后发现 Reality 连连不上
- **教训**：对新手来说，先跑通一个简单的（Hysteria2），再折腾复杂的（Reality）

### 2. Reality vs Hysteria2 的真实差距
- 网上的教程都推 Reality 是"最强"，但事实是 Reality 配置容错率极低
- Hysteria2 配置简单太多了（一个密码搞定），且实际速度不差
- **结论**：不一定选"最强的"，选"最能跑通的"

### 3. 3X-UI 面板的双刃剑
- 方便是真方便，Web界面点点点就行
- 坑也是真坑：会从数据库覆盖 config.json，手动改的全白干
- **解决方案**：停止面板，用独立 systemd 服务管理

### 4. v2rayN 的 Reality 兼容性问题
- v2rayN 是 Windows 上最知名的客户端，但 Reality 支持并不完美
- 7.22.3 版本建立连接后页面不加载
- **替代方案**：Hiddify（跨平台、协议支持全、免费）

### 5. Windows 工具链限制
- sshpass 没有 Windows 版
- pexpect 在 Windows 上不可用
- **解决方案**：用 Python paramiko 做 SSH 操作

### 6. 错误信息误导性
- "REALITY: received real certificate" 看着像错误，其实是走到 Spider 模式的正常日志
- 真正的错误原因往往需要结合多个日志一起看
