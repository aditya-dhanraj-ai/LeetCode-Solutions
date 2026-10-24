class Solution:
    def dailyTemperatures(self, temp: list[int]) -> list[int]:
        n=len(temp)
        ans=[0]*n
        stack=[]
        for i in range (n):
            while stack and temp[i] > temp[stack[-1]]:
                prev_index=stack.pop()
                ans[prev_index]=i-prev_index

            stack.append(i)
        return ans