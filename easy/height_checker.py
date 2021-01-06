class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort=[]
        sort[::]=heights
        cnt=0
        sort.sort()
        for i in range(len(sort)):
            if heights[i] != sort[i]:
                cnt+=1
        return cnt