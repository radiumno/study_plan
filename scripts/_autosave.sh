#!/usr/bin/env bash
# 自动 git 保存脚本
# 用 Git Bash 运行: bash D:\Dev\AiProject\study_plan\_autosave.sh
# 会每5分钟自动commit一次

cd /d/Dev/AiProject/study_plan

while true; do
  # 检查有没有未提交的改动
  has_changes=$(git status --porcelain)
  if [ -n "$has_changes" ]; then
    git add -A
    git commit -m "auto-save $(date +'%Y-%m-%d %H:%M')"
    git push origin main 2>/dev/null
    echo "[$(date '+%H:%M')] 已自动保存并推送"
  fi
  sleep 300  # 5分钟
done
