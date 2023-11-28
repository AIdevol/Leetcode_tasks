class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        end = -inf
        cnt = 0
        for s, e in sorted(intervals):
            if s>=end: 
                end = e
                cnt += 1
            elif e<=end: 
                end = e
        return len(intervals)-cnt