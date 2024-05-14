class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        return sum(max(h-i, 0) for i, h in enumerate(happiness[:k]))