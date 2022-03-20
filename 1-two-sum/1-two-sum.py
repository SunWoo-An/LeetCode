class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        result = []
        for i in nums:
            sum = target - i
            if i in list:
                result.append(list.index(i))
                if list.index(i) == nums.index(i):
                    result.append(nums.index(i, nums.index(i)+1))
                else:
                    result.append(nums.index(i))
                break
            list.append(sum)
        return result