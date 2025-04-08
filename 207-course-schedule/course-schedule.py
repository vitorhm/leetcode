class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        indegree_nodes = [0] * numCourses

        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])
            indegree_nodes[pre[0]] += 1

        queue = deque()
        for i in range(len(indegree_nodes)):
            if indegree_nodes[i] == 0:
                queue.append(adj_list[i])

        visited = 0
        while queue:
            node = queue.popleft()
            for neighboor in node:
                indegree_nodes[neighboor] -= 1
                if indegree_nodes[neighboor] == 0:
                    queue.append(adj_list[neighboor])
                    
            visited += 1

        return visited == numCourses