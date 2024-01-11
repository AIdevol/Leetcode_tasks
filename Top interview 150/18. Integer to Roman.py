import math

class Solution:
    def intToRoman(self, N: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        ans = ""
        for i in range(13):
            while N >= val[i]:
                ans += rom[i]
                N -= val[i]
        return ans

        '''rmap={
            1:"I",
            5:"v",
            10:"x",
            50:"L",
            100:"C",
            500:"D",
            1000:"M"
        }
        seq=[1000,500,100,50,10,5,1]
        res = []
        while num >= 1000:
            res.append(rmap[900]) 
            res.append(rMap[1000])
            num -= 1000
        while num >= 900: 
            res.append(rMap[900])
            num -= 900
        while num>=500:
            res.append(rmap[500])
            num-=500
        while num>=100:
            res.append(rmap[100])
            num-=100
        while num>=50:
            res.append(rmap[50])
            num-=50
        while num>=10:
            res.append(rmap[10])
            num-=10
        while num>=1:
            res.append(rmap[1])
            num-=1
        return "".join(res)'''
        