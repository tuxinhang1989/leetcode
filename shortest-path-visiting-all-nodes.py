from collections import deque
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        mem = set()
        final = (1 << len(graph)) - 1
        q = deque()
        for i in range(len(graph)):
            q.append((1<<i, i, 0))

        while len(q) > 0:
            v = q.popleft()
            if v[0] == final:
                return v[2]
            neighbors = graph[v[1]]
            for n in neighbors:
                if (v[0]|(1<<n), n) not in mem:
                    mem.add((v[0]|(1<<n), n))
                    q.append((v[0]|(1<<n), n, v[2]+1))

        return -1


if __name__ == '__main__':
    graph = [[1,2,3],[0],[0],[0]]
    graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
    print Solution().shortestPathLength(graph)

