#  Copyright (c) 2022. Generated by Gu.
#  coding=utf-8
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             if (target - nums[i]) in nums[i + 1:]:
#                 return [i, nums.index((target - nums[i]))]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i


if __name__ == '__main__':
    a = Solution()
    a.twoSum([3, 2, 4], 6)
