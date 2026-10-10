from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()  # Stores indices, not values

        for right in range(len(nums)):
            left = right - k + 1

            # Remove indices outside the current window
            if window and window[0] < left:
                window.popleft()

            # Remove smaller values; they cannot be the maximum
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            # Window has reached size k
            if right >= k - 1:
                result.append(nums[window[0]])

        return result