class Graph():
    def __init__(self):
        self.nodes = {}

    def read(self,filename):
        f = open("test/"+filename,"r")

        nodeamount = int(f.readline())
        for _ in range(nodeamount):
            nodeinfo = f.readline()
            nodename,x,y = nodeinfo.split()
            if nodename not in self.nodes.keys():
                node = Node(nodename,x,y)
                self.nodes[nodename] = node

        edgeamount = int(f.readline())
        for _ in range(edgeamount):
            edge = f.readline()
            nodesrcname,nodedestname,weight = edge.split()
            self.nodes[nodesrcname].insertedge(nodedestname,weight)



    def printgraph(self):
        for key in self.nodes.keys():
            print(key, '->', self.nodes[key].name)

    def printedge(self):
        for key in self.nodes.keys():
            node = self.nodes[key]
            for edge in node.edges:
                print(key, '->', edge)

class Node():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x 
        self.y = y
        self.edges = []

    def insertedge(self,nodename,weight):
        self.edges.append([nodename,weight])

def main():
    g = Graph()
    g.read("test1.txt")
    g.printgraph()
    g.printedge()

if __name__ == '__main__':
    main()
    