"""
https://leetcode.com/discuss/interview-question/3719223/amazon-sde-oa-2023-find-maximum-profitable-months/2065846
"""

def solution(stockPrice: list[int]) -> int:
    # stack = []
    # n, r = len(v), 0
    # e = [0] * n
    # for i in range(0, n):
    #     while len(stack) and v[stack[-1]] < v[i]:
    #         # [top..i - 1] is what we want. Note it may contain equal elements.
    #         r += i - stack.pop()
    #     if len(stack):
    #         e[i] = i - stack[-1] if v[stack[-1]] > v[i] else i - stack[-1] + e[stack[-1]] - 1
    #     else:
    #         e[i] = i + 1
    #     r += e[i]
    #     stack.append(i)
    # while len(stack):
    #     # [top..n - 1] is what we want
    #     r += n - stack.pop()
    # return r - n
    n = len(stockPrice)

    # First pass: count how many positions to the right (inclusive) are less than or equal to stockPrice[i]
    right_counts = [0] * n
    stack = []
    for i in range(n):
        while stack and stockPrice[i] >= stockPrice[stack[-1]]:
            stack.pop()
        # The length from the current position to the last larger element on the right
        right_counts[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    # Second pass: count how many positions to the left (exclusive) are less than stockPrice[i]
    left_counts = [0] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stockPrice[i] > stockPrice[stack[-1]]:
            stack.pop()
        # The length from the current position to the last larger element on the left
        left_counts[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    # Sum up the counts for each position
    ans = sum(right_counts[i] + left_counts[i] - 1 for i in range(n))

    return ans

print(solution([1, 1, 1, 1]))
print(solution([2, 3, 2]))
print(solution([5, 1, 6]))
print(solution([1, 4, 1, 2, 4, 5, 2, 3, 5,  7, 6, 7, 3, 2, 7, 1, 5, 4, 5, 1, 2, 5, 3, 5]))
