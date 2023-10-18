import heapq


class MaxHeapItem:
    def __init__(self, val):
        self.val = val

    def __lt__(self, heap_item):
        return True if self.val > heap_item.val else False


class MedianFinder:

    def __init__(self):
        self.median: int = 0
        self.max_heap: [MaxHeapItem] = []
        self.min_heap: [int] = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            if not self.max_heap or num < self.max_heap[0].val:
                heapq.heappush(self.max_heap, MaxHeapItem(num))
                self.median = self.max_heap[0].val
            else:
                heapq.heappush(self.min_heap, num)
                self.median = self.min_heap[0]
            return
        elif len(self.max_heap) > len(self.min_heap):
            if num < self.max_heap[0].val:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, MaxHeapItem(num))
                heapq.heappush(self.min_heap, self.median)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, MaxHeapItem(self.median))
            else:
                heapq.heappush(self.max_heap, MaxHeapItem(num))
        self.median = (self.max_heap[0].val + self.min_heap[0]) / 2

    def findMedian(self) -> float:
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()