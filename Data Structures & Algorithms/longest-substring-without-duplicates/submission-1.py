class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = ""
        sequence = 0
        largest = 0

        for char in s:
            if char in seen:
                seen = seen[seen.index(char) + 1:]
                sequence = len(seen)
            seen += char
            sequence += 1
            largest = max(sequence, largest)
        return largest

