from aI_fall2018_p1.search.p1_search import Search
from aI_fall2018_p1.search.p1_DFS import DFSSearch
import aI_fall2018_p1 as algorithm

search = Search()
search.add_edge("Oradea", "Zerind", 71)
search.add_edge("Oradea", "Sibiu", 151)
search.add_edge("Zerind", "Arad", 75)
search.add_edge("Arad", "Timisoara", 118)
search.add_edge("Timisoara", "Lugoj", 111)
search.add_edge("Lugoj", "Mehadia", 70)
search.add_edge("Mehadia", "Dobreta", 75)
search.add_edge("Dobreta", "Craiova", 120)
search.add_edge("Arad", "Sibiu", 140)
search.add_edge("Sibiu", "Fagaras", 99)
search.add_edge("Sibiu", "Rimnicu Vilcea", 80)
search.add_edge("Rimnicu Vilcea", "Craiova", 146)
search.add_edge("Rimnicu Vilcea", "Pitesti", 97)
search.add_edge("Craiova", "Pitesti", 138)
search.add_edge("Pitesti", "Bucharest", 101)
search.add_edge("Fagaras", "Bucharest", 211)
search.add_edge("Bucharest", "Giurgiu", 90)
search.add_edge("Bucharest", "Urziceni", 85)
search.add_edge("Hirsova", "Urziceni", 98)
search.add_edge("Hirsova", "Eforie", 86)
search.add_edge("Urziceni", "Vaslui", 142)
search.add_edge("Vaslui", "Iasi", 92)
search.add_edge("Iasi", "Neamt", 87)

heuristic = {
    "Lugoj": 244,
    "Pitesti": 98,
    "Neamt": 234,
    "Timisoara":329,
    "Vaslui": 199,
    "Hirsova": 151,
    "Mehadia": 241,
    "Rimnicu Vilcea": 193,
    "Craiova": 160,
    "Fagaras": 178,
    "Giurgiu": 77,
    "Arad": 336,
    "Oradea": 380,
    "Dobreta": 242,
    "Iasi": 226,
    "Zerind": 374,
    "Sibiu": 253,
    "Bucharest": 0,
    "Urziceni": 80,
    "Eforie": 161
}

graph = search.graph
for city in graph:
    print(city, graph[city])

dfs = DFSSearch(graph=graph)
print(dfs.search("Arad", "Bucharest"))
dfs_limited = DFSSearch(graph=graph, limitation=3)
print(dfs.search("Arad", "Bucharest"))
dfs_limited = DFSSearch(graph=graph, iterative=True)
print(dfs.search("Arad", "Bucharest"))

a_start = algorithm.AStarSearch(graph= graph, heuristic=heuristic)
print(a_start.search("Arad", "Bucharest"))