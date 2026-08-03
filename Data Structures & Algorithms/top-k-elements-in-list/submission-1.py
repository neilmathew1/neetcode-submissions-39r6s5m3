class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        counts = Counter(nums)
        heap = []
        for count in counts:
            t = (counts[count], count)
            heapq.heappush(heap, t)
            if len(heap) > k:
                heapq.heappop(heap)
        return [y for (x,y) in heap]
        

        