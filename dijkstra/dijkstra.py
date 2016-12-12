def createGraph(edges):
	graph = {}
	for edge in edges: 
		start, end, weight = edge
		if(start not in graph):
			graph[start] = {}

		graph[start][end] = weight 
		
	return graph

nodes = ("A", "B", "C", "D", "E")
edges = (
	("A", "B", 4),
	("A", "C", 2),
	("B", "C", 3),
	("C", "B", 1),
	("B", "D", 2),
	("B", "E", 3),
	("C", "D", 4),
	("C", "E", 5),
	("E", "D", 1)
)
start = "A"
graph = createGraph(edges)
unvisitedNodes = ["A", "B", "C", "D", "E"]
distances = {
	"A": 0,
	"B": "inf",
	"C": "inf",
	"D": "inf",
	"E": "inf"
}
print distances
