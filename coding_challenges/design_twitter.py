from collections import defaultdict, deque
import heapq


class Tweet:
    def __init__(self, tweetId, time):
        self.tweetId = tweetId
        self.time = time


class HeapItem(Tweet):
    def __init__(self, *args):
        super().__init__(*args)

    def __lt__(self, heap_item):
        return True if self.time > heap_item.time else False


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(deque)
        self.feed = defaultdict(deque)
        self.following = defaultdict(set)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        q = self.tweets[userId]
        if len(q) == 10:
            q.popleft()
        self.time += 1
        q.append(HeapItem(tweetId, self.time))

        for follower in self.followers[userId].union({userId}):
            q = self.feed[follower]
            if len(q) == 10:
                q.popleft()
            q.append(tweetId)

    def _rebuildFeedForUser(self, userId: int) -> None:
        heap = []
        for followee in self.following[userId].union({userId}):
            heap += list(self.tweets[followee])
        heapq.heapify(heap)
        self.feed[userId] = deque([heapq.heappop(heap).tweetId for _ in range(10) if heap])

    def getNewsFeed(self, userId: int) -> list[int]:
        return list(self.feed[userId])[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.followers[followeeId].add(followerId)
        self._rebuildFeedForUser(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId)
        self.followers[followeeId].remove(followerId)
        self._rebuildFeedForUser(followerId)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))
