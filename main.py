from Graph import Graph

filename = 'Graph.txt'
g1 = Graph(filename)
sourceVertexId = '1'
g1.dijkstra(sourceVertexId, debug = False)
# print(g1)
# g1.printShortestPathDistances(['7', '37', '59', '82', '99', '115', '133', '165', '188', '197'])
f = open("ShortestPaths.txt",'w')
for vertex in g1.getVertices():
    f.write("{}: ".format(vertex))
    for path_vertex in g1.getVertices()[vertex].getShortestPath():
        f.write("{} ".format(path_vertex))
    f.write("\tDistance: {}".format(g1.getVertices()[path_vertex].getShortestPathDist()))
    f.write("\n")
f.close()
print("Check file 'ShortestPaths.txt' for all the shortest paths from vertex {}".format(sourceVertexId))









