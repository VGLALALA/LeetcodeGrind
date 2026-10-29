from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lp, hp = 0, 0
        d = Counter(t)
        out = []
        missing = len(t)

        while hp < len(s):
            char = s[hp]

            if d[char] > 0:
                missing -= 1

            d[char] -= 1
            hp += 1

            while missing == 0:
                if not out or hp - lp < out[1] - out[0]:
                    out = [lp, hp]

                char = s[lp]
                d[char] += 1

                if d[char] > 0:
                    missing += 1

                lp += 1

        if not out:
            return ""

        return s[out[0]:out[1]]