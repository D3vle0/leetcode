class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p=0
        res=[]
        for i in range(n):
            res.append(nums[p])
            p+=n
            res.append(nums[p])
            p=p+1-n
        return res