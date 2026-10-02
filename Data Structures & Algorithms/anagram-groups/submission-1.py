class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        groups = {}

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - ord('a')] += 1

            key = tuple(counts)

            if key in groups:
                groups[key] += [word]
            else:
                groups[key] = [word]
            
        return list(groups.values())
