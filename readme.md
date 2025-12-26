# 📘 LeetCode 刷题笔记

**Status Guide:**
✔️ 已解决 (Solved) | 🔄 复习中 (Reviewing) | ❌ 未通过 (Failed)

---

## 🔍 Binary Search (二分查找)

### 1. 有序数组做二分 (Binary Search on Sorted Arrays)
最基础的二分，核心在于定义清晰的边界（左闭右闭 vs 左闭右开）。

| ID | Title | Difficulty | Status | Date | Notes |
|:---:|:---|:---:|:---:|:---:|:---|
| 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | ✔️ | 2025-02-01 | 标准二分模板 |
| 34 | [Find First and Last Position of Element](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | 🔄 | 2025-02-02 | 需处理边界条件 |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | | | 寻找第一个 >= target 的位置 |
| 702 | [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) | Medium | | | 倍增法确定边界 |
| 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | | | 视为一维数组或两次二分 |
| 278 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | | | 类似 lower_bound |

### 2. 无序数组做二分 (Binary Search on Unordered Arrays)
通常涉及旋转数组 (Rotated Arrays) 或寻找峰值 (Peak Element)，利用局部有序性。

| ID | Title | Difficulty | Status | Date | Notes |
|:---:|:---|:---:|:---:|:---:|:---|
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | | | 判断哪一半是有序的 |
| 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | | | 爬坡法 |

### 3. 二分答案 (Binary Search on Answers)
当题目要求“最大化最小值”或“最小化最大值”，且答案具有单调性时使用。

| ID | Title | Difficulty | Status | Date | Notes |
|:---:|:---|:---:|:---:|:---:|:---|
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | | | 数值二分 |
| 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | | | 典型的二分答案 |

---

## 🌲 Binary Tree (二叉树)
*(预留给下一个大类)*

| ID | Title | Difficulty | Status | Date | Notes |
|:---:|:---|:---:|:---:|:---:|:---|
| ... | ... | ... | ... | ... | ... |
