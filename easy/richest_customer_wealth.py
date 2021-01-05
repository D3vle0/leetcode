class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr=[]
        for i in range(len(accounts)):
            arr.append(sum(accounts[i]))
        arr.sort()
        return arr[len(accounts)-1]