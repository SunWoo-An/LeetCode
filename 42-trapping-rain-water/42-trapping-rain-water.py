class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        left = 1
        right = len(height)-2
        left_max = height[0]
        right_max = height[len(height)-1]
        while left <= right:
            if left_max > right_max:
                if height[right] > right_max:
                    right_max = height[right]
                    right -= 1
                else:
                    sum += right_max - height[right]
                    right -= 1
            else:
                if height[left] > left_max:
                    left_max = height[left]
                    left += 1
                else:
                    sum += left_max - height[left]
                    left += 1
        return sum