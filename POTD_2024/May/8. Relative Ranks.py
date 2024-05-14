class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse= True)

        answer = []
        rank_map = {}

        for i , s in enumerate(sorted_score):
            if i == 0:
                rank_map[s] = 'Gold Medal'
            elif i ==1:
                rank_map[s] = 'Silver Medal'
            elif i == 2:
                rank_map[s] = 'Bronze Medal'
            else:
                rank_map[s] = str(i+1)
        for s in score:
            answer.append(rank_map[s])
        return answer