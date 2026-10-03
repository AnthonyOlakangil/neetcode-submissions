class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        decoded = []
        curr = ""
        length = ""
        j = 0
        while j < len(s):
            while s[j] != "#":
                length += s[j]
                j += 1
            length = int(length)
            # move past #
            j += 1

            for i in range(length):
                curr += s[j]
                j += 1
            decoded.append(curr)
            curr = ""
            length = ""
        return decoded
            
