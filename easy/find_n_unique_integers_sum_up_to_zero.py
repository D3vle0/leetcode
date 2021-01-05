class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr=[]
        cnt=1
        for i in range(n//2):
            arr.append(cnt)
            arr.append(cnt*-1)
            cnt+=1
        if n%2:
            arr.append(0)
        return arr
        