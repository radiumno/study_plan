---
name: teaching-explain-every-step
description: "teaching must explain every line/parameter step by step, not just dump code"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f41aebe1-38a0-4c6a-aaca-aa34fe64b2aa
---

Teaching must not just show code and say "this is how you do X". Every line, every parameter must be explained step by step.

**Why:** User needs to understand the reasoning behind each piece, not just copy-paste and move on.

**How to apply:**
1. For each code snippet, break it down parameter by parameter (e.g. `open('f.txt', 'w', encoding='utf-8')` -> explain filename / mode / encoding separately)
2. Compare similar concepts side by side (e.g. `'w'` vs `'a'` vs `'r'`)
3. No C++ comparison for Phase 1 (Python) — remove from template for Python days
4. Before each exercise, give step-by-step hints on what to do first, second, third
5. Mark memorization points (e.g. `newline=''` is a fixed idiom for csv) explicitly
6. When teaching content lives in a .py file, write the full explanation **in code comments**, not just in conversation
7. **Day 05 level of detail as minimum standard:**
   - Every parameter explained with parameter name / meaning / example value
   - Every function compared to its C++ equivalent
   - Every concept linked to a quant development use case
   - "This is a memorization point" explicitly marked when needed
   - Common pitfalls called out before the student hits them
