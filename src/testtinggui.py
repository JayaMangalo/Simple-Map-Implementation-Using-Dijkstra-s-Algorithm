import networkx as nx
import matplotlib.pyplot as plt
from Dijkstra import *

def main():
    net = nx.DiGraph()
    plt.ion()

    g = Graph()
    g.read("test1.txt")
    print(DijkstraSearch(g,"A","D"))

    for key in g.nodes.keys():
        node = g.getnode(key)
        print(node.name)
        net.add_node(node.name)

    for key in g.nodes.keys():
        node = g.getnode(key)
        for edge in node.edges:
            net.add_edge(node.name,edge[0],weight = edge[1])

    edge_labels=dict([((u,v,),d['weight'])
                    for u,v,d in net.edges(data=True)])
    pos=nx.spring_layout(net)
    nx.draw_networkx_edge_labels(net,pos,edge_labels=edge_labels)
    nx.draw(net,pos,with_labels=True,arrows=True)
    plt.show()
    print("ree")
    plt.waitforbuttonpress()



