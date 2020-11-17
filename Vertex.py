class Vertex:
    '''This is the class for Vertex objects'''

    def __init__(self, vertex_id, debug = False):
        '''This method is called to initialize the vertex parameters when a vertex object is instantiated'''

        self.__vertex_id = vertex_id
        self.__head_of = []
        self.__tail_of = []
        self.__shortest_path_dist = float('inf')
        self.__shortestPath = list()
        if debug:
            print("New vertex created with id {}.\n".format(self.__vertex_id))

    def getVertexId(self, debug = False):
        return self.__vertex_id

    def updateHeadOf(self, new_head_of, debug = False):
        self.__head_of.append(new_head_of)
        if debug:
            print("Adding edge {} to the list of edges meeting at vertex {}.\n".format(new_head_of, self.__vertex_id))

    def updateTailOf(self, new_tail_of, debug = False):
        self.__tail_of.append(new_tail_of)
        if debug:
            print("Adding edge {} to the list of edges originating at vertex {}.\n".format(new_tail_of, self.__vertex_id))

    def getHeadOf(self):
        return self.__head_of

    def getTailOf(self):
        return self.__tail_of

    def getShortestPathDist(self):
        return self.__shortest_path_dist

    def setShortestPathDist(self, shortestPathDist, debug = False):
        self.__shortest_path_dist = shortestPathDist
        if debug:
            print("The shortestPathDist of vertex {} is set to {}".format(self.__vertex_id, shortestPathDist))

    def getShortestPath(self):
        return self.__shortestPath

    def setShortestPath(self, prePath):
        self.__shortestPath.extend(prePath)
        self.__shortestPath.append(self.__vertex_id)

    def initSourcePath(self):
        self.__shortestPath.append(self.__vertex_id)
