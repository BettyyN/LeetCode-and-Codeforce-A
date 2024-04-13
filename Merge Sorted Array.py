class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        for i in range(len(nums2)):
            while second < n and first < m + second:
                if nums2[second] <= nums1[first]:
                    nums1.insert(first, nums2[second])
                    second += 1
                elif first == m + second - 1:
                    nums1[first + 1] = nums2[second]
                    second += 1
                first += 1
        while second < n:
            nums1[first] = nums2[second]
            first += 1
            second += 1
        nums1[:] = nums1[:m+n] 
                    
        
