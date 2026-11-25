class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rashu = {}
        for i,n in enumerate(nums):
            need = target - n
            if need in rashu:
                return [rashu[need], i]
            rashu[n]=i
        return 