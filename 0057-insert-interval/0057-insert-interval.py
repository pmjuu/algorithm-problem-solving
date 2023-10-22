class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        new_start, new_end = newInterval
        
        for interval in intervals:
            current_start, current_end = interval
            
            if current_end < new_start:
                results.append(interval)
            else:
                if new_end < current_start:
                    results.append([new_start, new_end])
                    new_start, new_end = interval
                else:                                           # make new merged Interval
                    new_start = min(current_start, new_start)
                    new_end = max(current_end, new_end)
                    
        results.append([new_start, new_end])

        return results