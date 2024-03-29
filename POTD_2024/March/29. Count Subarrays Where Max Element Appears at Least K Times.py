class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        a,n,cur,i=max(nums),len(nums),0,0
        res = 0
        for j in range(0,n):
            cur += (nums[j] == a)
            while cur >= k:
                cur -= nums[i] == a
                i+=1
            res += i
        return res
