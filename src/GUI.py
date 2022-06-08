import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from Dijkstra import *
import networkx as nx
import matplotlib.pyplot as plt
import time


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
        
    if filenames :    
        loadfileintograph(filenames[0])

def loadfileintograph(filenames):
        global g
        global Loaded
        global myLabelStats 
        g = Graph()
        if(not g.read(filenames)):
                stats = "FAILED TO LOAD"
                Loaded = False
                myLabelStats["text"] = stats
                return
        else:   
                stats = "Loaded"
                Loaded = True  
                myLabelStats["text"] = stats      

        displaygraph([])

def SolveButton():
        src = myEntryFrom.get()
        dest = myEntryTo.get()
        global Loaded
        if (Loaded and src and dest):
                global g

                start_time = time.time()
                queued_nodes_amount,explored_nodes_amount,path,weight = DijkstraSearch(g,src,dest)
                curtime = time.time()
                searchtime = (curtime - start_time) * 1000

                print("START TIME: "+ str(start_time))
                print("END TIME: "+str(curtime))

                global myLabelStats
                if (path == "ERROR"):
                        stats = "Invalid Input"
                elif(path == "FAIL"):
                        stats = "No Path Found\nSearch Time: "+str(searchtime)+"ms \nQueued Nodes: "+str(queued_nodes_amount)+"\nExplored Nodes: "+str(explored_nodes_amount)
                else:   
                        betterpath = path[0]
                        for nodename in path[1:]:
                                betterpath += "-"+nodename

                        stats = "Search Successful\nSearch Time: "+str(searchtime)+"ms \nQueued Nodes: "+str(queued_nodes_amount)+"\nExplored Nodes: "+str(explored_nodes_amount)+"\nPath: "+str(betterpath)+"\nWeight: "+str(weight)
                myLabelStats["text"] = stats
                displaygraph(path)

def displaygraph(path):
        global g
        net = nx.DiGraph()
        for key in g.nodes.keys():
                node = g.getnode(key)
                net.add_node(node.name)

        for key in g.nodes.keys():
                node = g.getnode(key)
                for edge in node.edges:
                        net.add_edge(node.name,edge[0],weight = edge[1])
        
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in net.edges(data=True)])

        if path == "FAIL" and path!= "ERROR" and path!= []:
                nodecolors = ['blue' for _ in range(len(net))]
                edgecolors = ['blue' for _ in range(len(net.edges()))]

        else:
                nodecolors = []
                for netnode in net:
                        if netnode in path:
                                nodecolors.append('yellow')
                        else:
                                nodecolors.append('blue')
                edgecolors = []
                for u,v in net.edges():
                        if isEdgeinPath(u,v,path):
                                edgecolors.append('yellow')
                        else:
                                edgecolors.append('blue')
                

        pos = nx.spring_layout(net, k=2, iterations=50,seed=1)
        plt.cla() 
        plt.clf() 
        nx.draw_networkx_edge_labels(net,pos,edge_labels=edge_labels)
        nx.draw(net,pos,with_labels=True,node_color = nodecolors,edge_color=edgecolors,arrows=True)
        plt.show()

def isEdgeinPath(u,v,path):
        for i in range(len(path)-1):
                if path[i] == u and path[i+1] == v:
                        return True
        return False
g = Graph()
root = tk.Tk()
root.title("15-Puzzle")
# root.geometry('1000x600')

open_button = ttk.Button(
    root,
    text='Upload File',
    command=select_files
)
open_button.grid(row=0,column=0,pady=10)

myEntryFrom = tk.Entry(root,text ="From",width=10)
myEntryFrom.grid(row=1,column=0,pady=10,padx=10)

myEntryTo = tk.Entry(root,text ="To",width=10)
myEntryTo.grid(row=1,column=1,padx=10,pady=10)

myButton = tk.Button(root,text = "Solve",command=SolveButton)
myButton.grid(row=1,column=3,pady=10)

Loaded = False
stats = "Not Yet Loaded"
myLabelStats = tk.Label(root,text = stats)
myLabelStats.grid(row = 7,column=0,pady=10,padx=20,columnspan=3)

root.mainloop()
