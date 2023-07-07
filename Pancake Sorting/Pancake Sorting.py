class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        rotate = []  
        def reverse(arr, end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1    
        for i in range(len(arr)-1, 0, -1):            
            large_idx = arr.index(i+1)          
            if large_idx == i:
                continue           
            if large_idx != 0:
                reverse(arr, large_idx)
                rotate.append(large_idx+1)            
            reverse(arr, i)
            rotate.append(i+1)
        
        return rotate
