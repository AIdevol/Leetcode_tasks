import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        pq = []
        room = 0

        for interval in intervals:
            if not pq or interval[0] < pq[0]:
                room += 1
            else:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])

        return room
