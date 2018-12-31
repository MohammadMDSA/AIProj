import queue as Q

from p1_search import Search


class GBFSSearch(Search):

    def __init__(self, graph=None):
        super().__init__(graph)

    def search(self, start, goal):
        visited = {}
        for node in self.graph:
            visited[node] = False
        final_path = []

        pq = Q.PriorityQueue()
        pq.get()

        def greedyBFSUtil(v, visited, final_path, dest, gooal):
            if gooal == 1:
                return gooal
            visited[v] = True
            final_path.append(v)
            if v == dest:
                gooal = 1
            else:
                pq_list = []
                pq, size = getPriorityQueue(G[v])
                for i in range(size):
                    pq_list.append(pq.get().description)
                for i in pq_list:
                    if gooal != 1:
                        # print "current city:", i
                        if visited[i] == False:
                            gooal = greedyBFSUtil(i, visited, final_path, dest, gooal)
            return gooal

        gooal = greedyBFSUtil(start, visited, final_path, goal, 0)
