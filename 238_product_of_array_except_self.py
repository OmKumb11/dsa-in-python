class Solution(object):
    def productExceptSelf(self, nums):
        
        count = len(nums)
        answer = [1] * count
        left = 1
        for i in range(count):
            answer[i] = left
            left *= nums[i]
        
        right  = 1
        for i in range(count -1, -1, -1):
            answer[i] *= right
            right *= nums[i]      
            
        return answer