class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        mapping={}
        for num in nums2:
            while stack and num>stack[-1]:
                mapping[stack.pop()]=num
            stack.append(num)
        while stack:
            mapping[stack.pop()]=-1
        ans=[]
        for num in nums1:
            ans.append(mapping[num])
        return ans

            