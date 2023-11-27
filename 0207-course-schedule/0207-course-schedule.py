from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        stack = []
        graph = defaultdict(list)
    
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        def hasCycle(course):
            visited[course] = 1
            stack.append(course)
            
            for neighbor in graph[course]:
                if (visited[neighbor] == 0 and hasCycle(neighbor)) or visited[neighbor] == 1:
                    return True

            visited[course] = 2
            stack.pop()
            return False

        for course in range(numCourses):
            if visited[course] == 0 and hasCycle(course):
                return False
        
        return True