# Graph Model Functions and Classes

class Node(object):
    def __init__(self, name):
        """Assumes name is a str"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self, src: Node, dst: Node, weight=0):
        """Assumes src and dest are Nodes"""
        self.src = src
        self.dst = dst
        self.weight = weight

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    # def getWeight(self):
    #     return self.weight

    def __str__(self):
        return str(self.src.getName()) + "->" + str(self.dst.getName())


class DiGraph(object):
    def __init__(self):
        """edges is a dict mapping each node to a list of its children"""
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError("Duplicate None")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dst = edge.getDestination()
        if not (src in self.edges and dst in self.edges):
            raise ValueError("Node not in graph")
        self.edges[src].append(dst)

    def getChildrenOf(self, node):
        return self.edges[node]

    def hadNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for i in self.edges:
            if i.getName() == name:
                return i
        raise NameError(name)

    def __str__(self):
        result = ""
        for src in self.edges:
            for dst in self.edges[src]:
                result += str(Edge(src, dst)) + "\n"
        return result[:-1]  # get rid of trailing newline


class Graph(DiGraph):
    def addEdge(self, edge):
        DiGraph.addEdge(self, edge)
        other_way = Edge(edge.getDestination(), edge.getSource())
        DiGraph.addEdge(self, other_way)


def buildCityGraph(graphType):
    g = graphType()
    for i in ["Bengaluru", "Mysore", "Hubli", "Chennai", "Kolkata",
              "Chandigarh", "Guwahati", "Bhubaneswar"]:  # 8 Nodes
        g.addNode(Node(i))
    g.addEdge(Edge(g.getNode("Bengaluru"), g.getNode("Hubli")))
    g.addEdge(Edge(g.getNode("Bengaluru"), g.getNode("Mysore")))
    g.addEdge(Edge(g.getNode("Bengaluru"), g.getNode("Chennai")))
    g.addEdge(Edge(g.getNode("Chennai"), g.getNode("Mysore")))
    g.addEdge(Edge(g.getNode("Chennai"), g.getNode("Chandigarh")))
    g.addEdge(Edge(g.getNode("Chennai"), g.getNode("Guwahati")))
    g.addEdge(Edge(g.getNode("Guwahati"), g.getNode("Kolkata")))
    g.addEdge(Edge(g.getNode("Hubli"), g.getNode("Chandigarh")))
    g.addEdge(Edge(g.getNode("Mysore"), g.getNode("Kolkata")))
    g.addEdge(Edge(g.getNode("Chandigarh"), g.getNode("Kolkata")))
    g.addEdge(Edge(g.getNode("Chandigarh"), g.getNode("Mysore")))
    g.addEdge(Edge(g.getNode("Hubli"), g.getNode("Bengaluru")))
    g.addEdge(Edge(g.getNode("Chennai"), g.getNode("Hubli")))
    g.addEdge(Edge(g.getNode("Kolkata"), g.getNode("Bhubaneswar")))
    return g


def printPath(path):
    result = ""
    for i in path:
        result += i.getName() + "->"
    return result[:-2]


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.getChildrenOf(start):
        if node not in path:  # avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    print("Depth First Search")
    return DFS(graph, start, end, [], None, toPrint)


def testSP(source, destination):
    g = buildCityGraph(DiGraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint=True)
    if sp is not None:
        print("Shortest path from", source, "to", destination,
              "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)


testSP("Bengaluru", "Bhubaneswar")
printQueue = True


def BFS(graph: DiGraph, start: Node, end: Node, dontGo: list, toPrint=False):
    print("Breadth First Search")
    nodesSearched = dontGo + [start]
    pathQueue = [[start]]
    while len(pathQueue) != 0:
        # Get and remove oldest element in pathQueue
        if printQueue:
            print('Queue:', len(pathQueue))
            for p in pathQueue:
                print(printPath(p))
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path:', printPath(tmpPath))
            # print()
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.getChildrenOf(lastNode):
            if nextNode not in nodesSearched:
                nodesSearched.append(nextNode)
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def testSP_BFS(source, destination, dontGo=None):
    g = buildCityGraph(DiGraph)
    if dontGo == None:
        dontGo = []
    elif dontGo != []:
        dontGo = [g.getNode(i) for i in dontGo]
    sp = BFS(g, g.getNode(source), g.getNode(destination), dontGo, toPrint=True)
    if sp is not None:
        print("Shortest path from", source, "to", destination,
              "is", printPath(sp))
    else:
        print("There is no path from", source, "to", destination)


print()
# testSP_BFS("Bengaluru", "Bhubaneswar", dontGo=["Chandigarh", "Mysore"])
testSP_BFS("Bengaluru", "Mysore")
testSP_BFS("Mysore", "Guwahati", dontGo=["Bengaluru"])
