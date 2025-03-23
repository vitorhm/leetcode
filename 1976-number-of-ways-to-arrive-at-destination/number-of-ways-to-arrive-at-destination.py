class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for road in roads:
            adjacency_list[road[0]].append((road[1], road[2]))
            adjacency_list[road[1]].append((road[0], road[2]))

        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        path_count = [0] * n
        path_count[0] = 1

        min_heap = [(0, 0)]

        while len(min_heap) > 0:
            time, node = heapq.heappop(min_heap)

            if time > shortest_time[node]:
                continue

            for next_node, next_time in adjacency_list[node]:
                if time + next_time < shortest_time[next_node]:
                    shortest_time[next_node] = time + next_time
                    path_count[next_node] = path_count[node]
                    heapq.heappush(min_heap, (shortest_time[next_node], next_node))
                elif time + next_time == shortest_time[next_node]:
                    path_count[next_node] = (path_count[next_node] + path_count[node]) % 1_000_000_007

        return path_count[n-1]