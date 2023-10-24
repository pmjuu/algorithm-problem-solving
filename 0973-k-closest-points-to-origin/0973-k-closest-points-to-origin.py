import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        getDistance = lambda point: math.sqrt(point[0]**2 + point[1]**2)
        
        distances = [(getDistance(point), point) for point in points]
        
        distances.sort(key=lambda x: x[0])
        
        return [x[1] for x in distances[:k]]