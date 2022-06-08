from queue import PriorityQueue
from Graph import *

def DijkstraSearch(G: Graph,nodesrc : str , nodedst : str):
    if nodesrc not in G.nodes.keys() or nodedst not in G.nodes.keys():
        return 0,0, "ERROR",0
    
    pq = PriorityQueue()

    queuednodes = 0
    explorednodes = []

    NodeRoot = G.getnode(nodesrc)
    pq.put((0,NodeRoot,[NodeRoot.name]))

    while(not pq.empty()):
        weight, node,path = pq.get()
        if node.name == nodedst:    #found
            return queuednodes,len(explorednodes),path,weight

        if (node.name in (explorednodes)):     #check if nodetarget already explored
            continue

        explorednodes.append(node.name)
        for edge in node.edges:
            nodetargetname = edge[0] 
            nodeweight = weight + int(edge[1])
            node = G.getnode(nodetargetname)

            newpath = path + [edge[0]]
            pq.put((nodeweight,node,newpath))
            queuednodes+=1

    return queuednodes,len(explorednodes),"FAIL",0
def main():
    g = Graph()
    g.read("test/test1.txt")
    print(g.getgraphnodesname())
    g.printedge()

    print(DijkstraSearch(g,"A","D"))

if __name__ == '__main__':
    main()
    