class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        while k > 0:
            highest_count = max(counts.values())

            for num, count in counts.items():
                if count == highest_count:
                    res.append(num)
                    break
            del counts[res[-1]]
            k -= 1
        return res


        
            

