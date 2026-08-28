class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math 
        heap = []
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            pair = (-dist, point)
            heapq.heappush(heap, pair)
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for (dist, point) in heap]
