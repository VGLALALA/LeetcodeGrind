class Solution:
    def minChanges(self, s: str) -> int:
        action = 0
        for i in range(int(len(s)/2)):
            acti = i * 2 
            if s[acti] != s[acti + 1]:
                action += 1
        return action
        