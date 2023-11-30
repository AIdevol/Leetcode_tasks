class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0]))
        mergedIntervals = []
        mergedIntervalIndex = 0
        mergedIntervals.append(intervals[0])
        for i in range(1,len(intervals)):
            currentInterval = intervals[i]
            currentMergedInterval = mergedIntervals[mergedIntervalIndex]
            if currentInterval[0] <= currentMergedInterval[1] and currentInterval[1] >= currentMergedInterval[0]:
                mergedIntervals[mergedIntervalIndex] = [min(currentMergedInterval[0], currentInterval[0]), max(currentInterval[1], currentMergedInterval[1])]
            else:
                mergedIntervals.append(currentInterval)
                mergedIntervalIndex += 1
        return mergedIntervals
                
        
        