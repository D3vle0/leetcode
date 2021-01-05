class Solution:
    def maxDepth(self, s: str) -> int:
        data = []
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1
                data.append(cnt)
            elif i == ")":
                cnt -= 1
        data.sort()
        try:
            return data[len(data)-1]
        except:
            return 1 if "(" in s else 0
