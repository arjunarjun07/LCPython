from collections import Counter


class LCArrays:
   
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = Counter(nums)
        
        for k,val in hashmap.items():
            if(val > 1):
                return False
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = Counter(s)
        map2 = Counter(t)

        if(map1 == map2):
            return True

        return False
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
    
        umap = {}
        res_pair = []

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in umap:
                res_pair = [umap[diff], i]
                return res_pair
            else:
                umap[nums[i]] = i
                
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    
        res = []
        umap = {}

        for each_word in strs:
            sorted_str = ''.join(sorted(each_word))
            
            if sorted_str in umap:
                umap[sorted_str].append(each_word)
            else:
                umap[sorted_str] = [each_word] 
            
        for k,v in umap.items():
            res.append(v)
        return res
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = []
        resmap = Counter(nums)
        #build max heap based on the map
        #pop(k) items from the heap - to get most freq
        di = list(resmap.items())
            
        # converting into heap
        hq._heapify_max(di)

        print(di)

        for k in range(k,0,-1):
            item = hq.heappop(di)
            ans.append(item[1])
        return ans
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []

        prod = 1
        prefix_res = [1] * len(nums)

        for i,num in enumerate(nums):
            prefix_res[i] = prod
            prod *= num
            
        prod = 1
        postfix_res = [1] * len(nums)

        for j in range(len(nums)-1, -1, -1):
            postfix_res[j] = prod
            prod *= nums[j]
            
        ans = list(map(lambda x,y: x*y, prefix_res, postfix_res)) 
        return ans
    
    def IsValidListOfElements(self, curr_row: list[str])->bool:
        nums_freq = Counter(curr_row)
        
        for k,v in nums_freq.items():
            if(k != "." and v > 1):
                return False
            
        return True    
    
    def ValidateCube(self, board: list[list[str]], i:int)->bool:        
        
        res = True
        cube_nums = []
        k = 0
        for times in range(3):
            ind = i
            for ind in range(ind, ind+3, 1):
                for j in range(k, k+3, 1):
                    cube_nums.append(board[ind][j])
            
            if (self.IsValidListOfElements(cube_nums) == False):
                return False
            
            cube_nums.clear()
            k +=3        
        return True
        
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        res = True
        columns = list(zip(*board))
        j = 0
        
        for i in range(9):
            curr_row = board[i]
            curr_col = columns[i]
            if self.IsValidListOfElements(curr_row) and self.IsValidListOfElements(curr_col):  
                if i % 3 == 0:
                    if self.ValidateCube(board, i):
                        pass
                    else:
                        return False
            else:
                return False
        
        return res
    
    def longestConsecutive(self, nums: list[int]) -> int:        
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest