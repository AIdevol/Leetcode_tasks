class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        p, n, z = [], [], []

        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)

        P, N = set(p), set(n)

        if z:
            for i in n:
                if -1 * i in P:
                    res.add((i, 0, -i))

        if len(z) >= 3:
            res.add((0, 0, 0))

        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        
        return res


        