class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        ptr1, ptr2 = 0,0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] > nums2[ptr2]:
                res.append(nums2[ptr2])
                ptr2 += 1
            else:
                res.append(nums1[ptr1])
                ptr1 += 1

        while ptr1 < len(nums1):
            res.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < len(nums2):
            res.append(nums2[ptr2])
            ptr2 += 1

        median = 0
        total = len(res)
        if total % 2 == 0:
            no1 = res[int(total/2)]
            no2 = res[int(total/2 - 1)]
            median = (no1 + no2) / 2
        else:
            ind = total // 2
            median = res[ind]

        return median



            

        





            
        