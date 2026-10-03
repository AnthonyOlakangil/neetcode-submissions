class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sequence = 1
        largest = sequence
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:

            if prev == num:
                continue

            if num == prev + 1:
                sequence += 1

            if sequence > largest:
                largest = sequence

            if num != prev + 1:
                sequence = 1
            
            prev = num
        return largest
            



                