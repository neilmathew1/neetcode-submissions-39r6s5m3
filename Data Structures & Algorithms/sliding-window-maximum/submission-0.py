class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        res = []
        heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, idx))
            while heap[0][1] <= idx - k:
                heapq.heappop(heap)
            if idx >= k - 1:
                res.append(-heap[0][0])
        return res
