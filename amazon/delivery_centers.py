"""https://leetcode.com/discuss/interview-question/3949864/Amazon-OA"""

def calculate(x, positions):
    return 2 * sum(abs(p - x) for p in positions)


def binary_search_left(positions, l, r, d):
    while l <= r:
        mid = l + (r - l) // 2
        v = calculate(mid, positions)
        if v <= d:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def binary_search_right(positions, l, r, d):
    while l <= r:
        mid = l + (r - l) // 2
        v = calculate(mid, positions)
        if v <= d:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


def binary_search(positions, d):
    positions.sort()
    max_deviation = d // (2 * len(positions))
    i, j = positions[0] - max_deviation, positions[-1] + max_deviation
    while i <= j:
        mid = i + (j - i) // 2
        v = calculate(mid, positions)
        if v <= d:
            break
        l, r = -1, -1
        if i < mid - 1:
            l = calculate(i + (mid - 1 - i) // 2, positions)
        if mid + 1 < j:
            r = calculate(j + (mid - 1 - j) // 2, positions)

        if l != -1 and r != -1:
            if l < r:
                j = mid - 1
            else:
                i = mid + 1
        elif l != -1:
            j = mid - 1
        else:
            i = mid + 1

    if j < i:
        return -1

    left = binary_search_left(positions, -1e10, mid, d)
    right = binary_search_right(positions, mid, 1e10, d)

    return abs(right - left) + 1


if __name__ == "__main__":
    centers = [-2, 1, 0]
    d = 8
    print(binary_search(centers, d))


# Example
