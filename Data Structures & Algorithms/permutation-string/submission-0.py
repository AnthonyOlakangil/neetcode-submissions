class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)

        window_size = len(s1)

        for i in range(len(s2) - window_size + 1):
            window = s2[i: i + window_size]

            if s1 == sorted(window):
                return True
        return False