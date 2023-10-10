import heapq


class HeapItem:
    def __init__(self, name, importance, order):
        self.name = name
        self.importance = importance
        self.order = order

    def __lt__(self, heap_item):
        if self.importance > heap_item.importance:
            return True
        elif self.importance < heap_item.importance:
            return False
        else:
            return True if self.order < heap_item.order else False

    def __repr__(self):
        return f"Name: {self.name} Imp: {self.importance} Order: {self.order}"


class SkiResort:
    def __init__(self):
        self.pq = []
        self.order = 0

    def add_skier(self, name, importance):
        heapq.heappush(self.pq, HeapItem(name, importance, self.order))
        self.order += 1

    def get_skier(self):
        return heapq.heappop(self.pq).name


if __name__ == "__main__":
    resort = SkiResort()
    resort.add_skier("Bob", 1)
    resort.add_skier("Jacob", 1)
    resort.add_skier("Maggie", 5)
    print(resort.get_skier())
    resort.add_skier("Prasid", 7)
    print(resort.get_skier())
    print(resort.get_skier())
    print(resort.get_skier())
