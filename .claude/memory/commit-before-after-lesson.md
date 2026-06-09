---
name: commit-before-after-lesson
description: 写新课前先commit当前进度, 写完再commit一次
metadata:
  type: feedback
  originSessionId: current
---

写课前必须先 commit（记录当前已完成的状态），写完后再次 commit（记录新课内容）。

**Why:** 避免丢失进度，每次课都有独立的 commit 记录，方便回溯"写课前写了什么"和"这节课新增了什么"。

**How to apply:**
1. 用户说"开始学习"/"继续"/写新课 → 先 git add + commit（格式 `dayXX: 课前 checkpoint`）
2. 写完整节课 → 再 git add + commit（格式 `dayXX: 完整课程内容`）
3. 如果用户要求多次 commit 或特定消息格式，以用户要求为准

Related: [[course-and-roadmap-workflows]], [[daily-progress-display]]
