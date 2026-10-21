from heapq import nlargest

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)

        self.tweet_cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_cnt, tweetId))
        self.tweet_cnt += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant_tweets = list(self.tweets[userId])

        for followee in self.follows[userId]:
            relevant_tweets += self.tweets[followee]

        return [x[1] for x in nlargest(10, relevant_tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return

        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
