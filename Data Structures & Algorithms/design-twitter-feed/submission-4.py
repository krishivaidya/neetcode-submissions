class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.time = 0
        self.tweets = defaultdict(list)
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #append the users most recent tweet
        self.finalten = []
        mh = []
        
        if self.tweets[userId]:
            n = len(self.tweets[userId]) - 1
            time, tid = self.tweets[userId][n][0] * -1, self.tweets[userId][n][1]
            mh.append((time,tid, n, userId))

        for i in self.follows[userId]:
            if self.follows[userId]:
                m = len(self.tweets[i]) - 1
                time, tid = self.tweets[i][m][0] * -1, self.tweets[i][m][1]
                mh.append((time,tid, m , i))
        heapq.heapify(mh)
        c = 0
        while c < 10 and mh:
            time, tid, pos, uid = heapq.heappop(mh)
            self.finalten.append(tid)
            c+= 1
            if pos != 0:
                pos -= 1
                time, tid = self.tweets[uid][pos][0], self.tweets[uid][pos][1]
                heapq.heappush(mh,(time * -1, tid, pos, uid))

        return self.finalten
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
