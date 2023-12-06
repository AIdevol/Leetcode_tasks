class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for string in strs:
            current=sorted(string)
            current="".join(current)
            if current in dic:
                dic[current].append(string)
            else:
                dic[current]=[string]
        ans=[]
        for string in dic:
            ans.append(dic[string])
        return ans        