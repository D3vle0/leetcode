class Solution:
    def findLucky(self, arr: List[int]) -> int:
        data=[]
        data[::]=arr
        res=[]
        arr = list(set(arr))
        for i in arr:
            if data.count(i) == i:
                res.append(i)
        if res==[]:
            return -1
        res.sort()
        return res[-1]