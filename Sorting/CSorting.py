class CSorting:
    
    #Ref : https://www.bigocheatsheet.com/ for sorting time & space complexities
    
    """
        InsertionSOrt()
        
        //https://www.youtube.com/watch?v=JU767SDMDvA
	    //similar to a sorting way of card deck in hand
    """
    
    def InsertionSort(self, nums:list[int]) -> list[int]:
        
        for i in range(len(nums)):
            #Take one card in hand    
            curr_elm = nums[i]
            
            #Find until we find its crct position
            
            prev = i - 1
            while prev >= 0 and nums[prev] > curr_elm:
                #swap prev elem to nxt index
                nums[prev + 1] = nums[prev]
                prev -= 1
            
            nums[prev + 1] = curr_elm
        return nums
    
    """
        MergeSort()
        
        Divide & conquer
        +
        Merge Procedure() - 2way merge
    """
    
    def TwoWayMerge(self, nums:list[int], p:int, mid:int, r:int):
        
        range1 = nums[p:mid+1]
        range2 = nums[mid+1:r+1]
        result_list = []
        
        total_len = len(range1) + len(range2)

        i = 0; j = 0   
        while i < len(range1) and j < len(range2):
            
            if range1[i] < range2[j]:
                result_list.append(range1[i])
                i += 1
            else:
                result_list.append(range2[j])
                j += 1
        
        while i < len(range1):
            result_list.append(range1[i])
            i += 1
            
        while j < len(range2):
            result_list.append(range2[j])
            j += 1
        
        indx = 0
        for k in range(p,r+1):
            nums[k]  = result_list[indx]
            indx += 1
            
    
    def MergeSort(self, nums:list[int]):
        
        def ActualMergeSort(nums, p:int, r:int):
            
            if p < r:
                mid = (p+r)//2
                
                ActualMergeSort(nums, p, mid)
                ActualMergeSort(nums, mid+1, r)
                self.TwoWayMerge(nums, p, mid, r)
        
        ActualMergeSort(nums, 0, len(nums)-1)
        return nums
    
    def QSPartition(self, nums:list[int], low:int, high:int)->int:
        
        """
            Take the rear element & put it in a correct place
            So it will partition the list as follows:
            
            (elems_in_left) <= pivot < (elems_in_right)            
        """
        # choose the rightmost element as pivot
        pivot = nums[high]
        
        i = low -1
        
        for j in range(low, high):
            
            if nums[j] <= pivot:
                i = i+1   
                #found an element at j which is <= pivot. So we need to place it after i
                nums[i], nums[j] = nums[j], nums[i]
            
        #After the loop, i - will have elems which is <= pivot val
        #Now we can place pivot at i+1 (after smaller elems)
        nums[i+1], nums[high] = nums[high], nums[i+1]
        
        return i+1
    
    def QuickSort(self, nums:list[int], low:int, high:int)-> list[int]:
        
        if low < high:      
            p = self.QSPartition(nums, low, high)
            self.QuickSort(nums, low, p-1)
            self.QuickSort(nums, p+1, high)
        return nums
                
        
    
c = CSorting()
vals = [5,2,1,8,6,7]
print(c.QuickSort(vals, 0, len(vals)-1))
                