

class CTwoPointers:
    
    def normalisestr(self, s:str) -> str:
        if s.isalnum():
            return True
        else:
            return False
    
    def isPalindrome(self, s: str) -> bool:        
        res = True
        
        s = s.upper()
        normalised_list = list(filter(self.normalisestr, s))
        normalised_str = "".join(normalised_list)
        
        i,j = 0, len(normalised_str) -1
        
        while i < j:
            if(normalised_str[i] == normalised_str[j]):
                i += 1
                j -= 1
            else:
                res = False
                break
        
        return res
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        res = []
        i,j = 0, len(numbers)-1
        
        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if(curr_sum == target):
                res.append(i+1)
                res.append(j+1)
                break
            elif curr_sum < target:
                i += 1
            else:
                j -= 1
                
        return res        
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        result = []
        
        for index in range(len(nums)):

            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1
            
            while left < right:
                curr_sum = nums[left] + nums[right] + nums[index]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]]) # After a triplet is appended, we try our best to incease the numeric value of its first element or that of its second.
                    left += 1 # The other pairs and the one we were just looking at are either duplicates or smaller than the target.
                    right -= 1 # The other pairs are either duplicates or greater than the target.
                    # We must move on if there is less than or equal to one integer in between the two nums.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 # The pairs are either duplicates or smaller than the target.
        return result
    
    def maxArea(self, height: list[int]) -> int:
        
        def getArea(height, L, R):
            return min(height[L], height[R]) * (R - L)
        
        L,R = 0, len(height) - 1
        
        MaxArea = 0
        
        while L < R:
            MaxArea = max(MaxArea, getArea(height, L, R))
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return MaxArea
    
    def trap(self, height: list[int]) -> int:
        
        res = 0  
        L, R = 0, len(height) - 1
        
        if not height:
            return 0

        MaxL = height[0]
        MaxR = height[len(height) - 1]
        
        while L < R:
            MaxL = max(MaxL, height[L])
            MaxR = max(MaxR, height[R])
            
            if MaxL < MaxR:
                res += MaxL - height[L]
                L += 1
            else:
                res += MaxR - height[R]
                R -= 1
        
        return res
        
ins = CTwoPointers()
ans = ins.maxArea([1,8,6,2,5,4,8,3,7])

print(ans)