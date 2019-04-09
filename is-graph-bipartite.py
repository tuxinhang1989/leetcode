from collections import deque

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = [0] * len(graph)
        l = range(len(graph))
        while len(l) > 0:
            q = deque()
            start = l.pop()
            q.append((start, 1))
            while len(q) > 0:
                node, color = q.popleft()
                if colors[node] == 0:
                    colors[node] = color
                    for peer in graph[node]:
                        if colors[peer] == 0:
                            q.append((peer, -color))
                        else:
                            if colors[peer] != -color:
                                return False

        return True


if __name__ == '__main__':
    graph = [[1,3], [0,2], [1,3], [0,2]]
    #graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    #graph = [[3],[2,4],[1],[0,4],[1,3]]
    graph = [[4],[],[4],[4],[0,2,3]]
    print Solution().isBipartite(graph)
