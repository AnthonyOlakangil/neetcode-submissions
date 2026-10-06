class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequencies = {}
        max_frequency = 0
        longest = 0

        for right in range(len(s)):
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            max_frequency = max(max_frequency, frequencies[s[right]])

            if (right - left + 1) - max_frequency > k:
                frequencies[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            
        return longest

