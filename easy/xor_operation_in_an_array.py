class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        for i in range(n):
            arr.append(start)
            start+=2
        res=arr[0]
        for i in range(n-1):
            res^=arr[i+1]
        return res
    