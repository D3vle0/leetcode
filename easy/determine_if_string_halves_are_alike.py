class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        cnt1=0
        cnt2=0
        word=["a","e","i","o","u"]
        for i in range(len(s)//2):
            if s[i] in word:
                cnt1+=1
            if s[i+len(s)//2] in word:
                cnt2+=1
        return cnt1==cnt2