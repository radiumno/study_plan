# Git 基础 — 量化开发必备

> 岗位要求: Git 出现频率 80%+
> 量化场景: 代码版本管理、回测结果追溯、团队协作

---

## 核心命令速查

### 初始化与克隆

```bash
git init                    # 把当前目录变成 Git 仓库
git clone <url>             # 从远程下载整个仓库
```

### 日常三连 (最常用)

```bash
git status                  # 看改了哪些文件 (红色=未暂存, 绿色=待提交)
git add <文件>               # 把改动加入暂存区
git add -A                  # 加入所有改动

git commit -m "消息"         # 把暂存区内容提交成一个版本
git log --oneline           # 看提交历史 (一行一个)
```

### 分支

```bash
git branch                  # 看当前在哪个分支
git checkout -b <新分支名>   # 创建并切换到新分支
git checkout <分支名>        # 切换到已有分支
git merge <分支名>           # 把指定分支合并到当前分支
```

### 远程

```bash
git push                    # 把本地提交推送到远程
git pull                    # 把远程更新拉到本地
```

---

## 量化开发实际场景

### 场景1: 每天提交

```bash
# 写了一天代码后
git status                  # 确认改了哪些文件
git add -A                  # 全部加入
git commit -m "feat: 添加移动平均线策略"
git push                    # 推送到 GitHub
```

### 场景2: 实验分支

```bash
# 想试一个新策略, 不影响主线
git checkout -b test_new_strategy
# ...改代码, 跑回测...
git add -A && git commit -m "wip: 测试双均线参数"

# 切回主线继续开发
git checkout main
```

### 场景3: 回滚

```bash
# 发现刚提交的代码有 bug
git log --oneline           # 找到上一个正常版本的 commit ID
git revert <commit-id>      # 撤销那个提交 (生成一个新提交)
```

---

## 本阶段要求

| 阶段 | Git 能力 | 达标标准 |
|------|---------|---------|
| 阶段1 | 能 commit / push / pull | 每天学完自己 commit |
| 阶段2 | 能分支开发 | 用分支做算法练习 |
| 阶段3+ | 能 rebase / 解决冲突 | 团队协作场景 |
