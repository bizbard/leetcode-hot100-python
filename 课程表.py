import collections
from typing import List

class Solution:
    """
    请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        edge = {i:[] for i in range(numCourses)}
        res = 0

        for cur, pre in prerequisites:
            indegree[cur] += 1
            edge[pre].append(cur)

        queue = collections.deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            course = queue.pop()
            res += 1
            for i in edge[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return res == numCourses
    

    """
    返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
    """
    def findOrder(self, numCourses, prerequisites):
        indegree = [0 for _ in range(numCourses)]
        edge = {i:[] for i in range(numCourses)}
        res = []

        for cur, pre in prerequisites:
            indegree[cur] += 1
            edge[pre].append(cur)

        queue = collections.deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            course = queue.pop()
            res.append(course)
            for i in edge[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return res
            

if __name__ == '__main__':
    # ======= Test Case =======
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.findOrder(numCourses, prerequisites)
    print(res)