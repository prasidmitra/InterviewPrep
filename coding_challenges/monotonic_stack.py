"""
https://www.geeksforgeeks.org/next-greater-element/
"""


def find_next_greater_element(arr: list[int]) -> list[int]:
    result = [-1 for _ in arr]
    stack = [0]
    for i in range(1, len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result


inputs = [
    [13, 7, 6, 12],
    [4, 5, 2, 25]
]

for inp in inputs:
    print(find_next_greater_element(inp))
