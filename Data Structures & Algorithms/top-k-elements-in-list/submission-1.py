class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []

        for num in nums:
            seen[num] = seen.get(num,0) + 1
        
        sorted_pairs = sorted(seen.items(),key=lambda item:item[1],reverse=True)

        for i in range(k):
            output.append(sorted_pairs[i][0])
        
        return output

