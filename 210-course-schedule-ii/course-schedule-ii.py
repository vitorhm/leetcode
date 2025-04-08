class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(numCourses)]
        indegree_nodes = [0] * numCourses
        for pre in prerequisites:
            adj_list[pre[1]].append(pre[0])
            indegree_nodes[pre[0]] += 1

        queue = deque()
        res = []
        for i in indegree_nodes:
            if indegree_nodes[i] == 0:
                queue.append(adj_list[i])
                res.append(i)

        while queue:
            node = queue.popleft()
            for neigh in node:
                indegree_nodes[neigh] -=1
                if indegree_nodes[neigh] == 0:
                    queue.append(adj_list[neigh])
                    res.append(neigh)

        if len(res) == numCourses:
            return res

        return []