from Vertex import Vertex
from Edge import Edge

class Graph:
    '''This is the class for the graph object'''

    def __init__(self, filename, debug = False):

        self.__vertices = {}
        self.__edges = {}
        self.__edge_id_count = 1
        # self.__source_vertex_id = source_vertex
        # self.__known_dist = {source_vertex}

        if debug:
            print("Parsing graph from file {}\n".format(filename))

        fo = open(filename, 'r')
        for line in fo:
            line = line.strip()
            line_arr = line.split('\t')
            tail_vertex = line_arr.pop(0)
            if tail_vertex not in self.__vertices.keys():
                self.__vertices.update({tail_vertex:Vertex(tail_vertex, debug)})
                if debug:
                    print("Added vertex {} to the vertices dictonary.\n".format(tail_vertex))
            for head_vertex in line_arr:
                head_vertex = head_vertex.split(",")
                edge_length = int(head_vertex[1])
                head_vertex = head_vertex[0]
                if head_vertex not in self.__vertices:
                    self.__vertices.update({head_vertex:Vertex(head_vertex, debug)})
                    if debug:
                        print("Added vertex {} to the vertices dictonary\n".format(head_vertex))
                self.__edges.update({self.__edge_id_count:Edge(self.__edge_id_count, edge_length, tail_vertex, head_vertex, debug)})
                if debug:
                    print("Added edge {} to the edges dictonary\n".format(self.__edge_id_count))
                self.__vertices[tail_vertex].updateTailOf(self.__edge_id_count, debug)
                self.__vertices[head_vertex].updateHeadOf(self.__edge_id_count, debug)
                self.__edge_id_count += 1


    def getVertices(self):
        return self.__vertices

    def dijkstra(self, source_vertex, debug = False):
        '''The method that implements the Dikstra's algorithm'''

        completed_vertices = {source_vertex}
        remaining_vertices = set(self.__vertices.keys()) - completed_vertices

        if debug:
            print("Vertex {} is the source vertex.".format(source_vertex))

        self.__vertices[source_vertex].setShortestPathDist(0, debug)
        self.__vertices[source_vertex].initSourcePath()

        while len(remaining_vertices) > 0:
            qualified_edges = []
            for edge_id in self.__edges.keys():
                if (self.__edges[edge_id].getTailVertex() in completed_vertices) and (self.__edges[edge_id].getHeadVertex() in remaining_vertices):
                    edge = self.__edges[edge_id]
                    qualified_edges.append(edge)
                    tail_vertex_id = edge.getTailVertex()
                    tail_vertex = self.__vertices[tail_vertex_id]
                    edge.setGreedyScore(tail_vertex.getShortestPathDist() + edge.getEdgeLength(), debug)

            qualified_edges.sort(key = lambda x:x.getGreedyScore(), reverse = False)
            chosen_edge = qualified_edges[0]
            chosen_vertex = chosen_edge.getHeadVertex()
            preceding_vertex = chosen_edge.getTailVertex()
            self.__vertices[chosen_vertex].setShortestPathDist(chosen_edge.getGreedyScore(), debug)
            self.__vertices[chosen_vertex].setShortestPath(self.__vertices[preceding_vertex].getShortestPath())
            completed_vertices.add(chosen_vertex)
            remaining_vertices.remove(chosen_vertex)
            if debug:
                print("Vertex {} added to the set of completed_vertices.".format(chosen_vertex))
                print("Set of completed_vertices:")
                print("{}\n".format(completed_vertices))


    def __str__(self):

        str1 = format("\nThe graph is as follows\n")
        str1 += "-"*30 + "\n"

        str1 += "List of all edges:\n"
        for edge_id in self.__edges.keys():
            str1 += "ID: "+format(edge_id) + "\t\t"
            str1 += "Tail: " + format(self.__edges[edge_id].getTailVertex()) + "\t\tHead: " + format(self.__edges[edge_id].getHeadVertex()) +"\t\t"
            str1 += "Length = " + format(self.__edges[edge_id].getEdgeLength()) +"\n\n"

        str1 += "List of all vertices:\n"
        for vertex_id in self.__vertices.keys():
            str1 += "vertex "+format(vertex_id) + " is " + "\n\t"
            str1 += "tail of edges " + format(self.__vertices[vertex_id].getTailOf()) + " \n\t"
            str1 += "head of edges " + format(self.__vertices[vertex_id].getHeadOf()) +"\n"
            str1 += "Shortest path distance: {}\n\n".format(self.__vertices[vertex_id].getShortestPathDist())
        str1 += "\n"

        return str1

    def printShortestPathDistances(self, vertexList):
        print("Vertices\t|\tShortest Path Distances")
        print("---------------------------------------")
        for vertex_id in vertexList:
            print("{}\t\t\t|\t\t{}".format(vertex_id, self.__vertices[vertex_id].getShortestPathDist()))
        print("\n")
