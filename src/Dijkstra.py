from queue import PriorityQueue
from Graph import *

def DijkstraSearch(G: Graph,nodesrc : str , nodedst : str):
    if nodesrc not in G.nodes.keys() or nodedst not in G.nodes.keys():
        return "ERROR" 
    
    pq = PriorityQueue()
    NodeRoot = G.getnode(nodesrc)
    pq.put((0,NodeRoot,[NodeRoot.name]))

    # print("put", NodeRoot.name ,"with weight",0)

    while(not pq.empty()):
        weight, node,path = pq.get()
        if node.name == nodedst:    #found
            return path

        if (node.isExplored()):     #check if nodetarget already explored
            continue
        

        print("processed node",node.name,path)
        for edge in node.edges:
            nodetargetname = edge[0] 
            nodeweight = weight + int(edge[1])
            node = G.getnode(nodetargetname)

            newpath = path + [edge[0]]
            pq.put((nodeweight,node,newpath))
            # print("put", node.name ,"with weight",nodeweight)

def main():
    g = Graph()
    g.read("test1.txt")
    g.printgraph()
    g.printedge()

    print(DijkstraSearch(g,"A","D"))

if __name__ == '__main__':
    main()
    