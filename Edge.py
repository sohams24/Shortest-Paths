class Edge:
    '''This is the class for edge objects'''

    def __init__(self, edge_id, length, tail_vertex, head_vertex, debug = False):
        '''This method is called to initialize the edge parameters when an edge object is instantiated'''

        self.__edge_id = edge_id
        self.__edge_length = length
        self.__tail_vertex = tail_vertex
        self.__head_vertex = head_vertex
        self.__greedy_score = 1000000
        if debug:
            print("New edge created with id {} and length {}.\n".format(self.__edge_id, self.__edge_length))

    def getEdgeLength(self):
        return self.__edge_length

    def getTailVertex(self):
        return self.__tail_vertex

    def getHeadVertex(self):
        return self.__head_vertex

    def getGreedyScore(self):
        return self.__greedy_score

    def setGreedyScore(self, greedyScore, debug = False):
        self.__greedy_score = greedyScore
        if debug:
            print("Greedy score of edge {} is set to {}".format(self.__edge_id, greedyScore))
