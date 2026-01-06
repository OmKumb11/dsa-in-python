class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}

        for n in nums:
            count[n]= count.get(n,0) + 1

        freq = [[] for i in range(len(nums)+ 1)]
        
        for n, c in count.items():
            freq[c].append(n)
        
        r = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                r.append(n)
                if len(r) == k:
                    return r