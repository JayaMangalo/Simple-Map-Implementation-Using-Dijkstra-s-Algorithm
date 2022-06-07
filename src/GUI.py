import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from Graph import *
import networkx as nx
import matplotlib.pyplot as plt

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
        g = Graph()
        if(not g.read(filenames)):
                return
        print("ree")
        global Loaded
        global myLabelStats 
        Loaded = True
        stats = "Loaded\n Available Nodes: " + str(g.getgraphnodesname())
        myLabelStats = tk.Label(root,text = stats)
        myLabelStats.grid(row = 7,column=0,pady=10,padx=20,columnspan=3)
def displaygraph(g: Graph):
        net = nx.DiGraph()
        for key in g.nodes.keys():
                node = g.getnode(key)
                print(node.name)
                net.add_node(node.name)

        for key in g.nodes.keys():
                node = g.getnode(key)
                for edge in node.edges:
                        net.add_edge(node.name,edge[0],weight = edge[1])
        
        edge_labels=dict([((u,v,),d['weight']) for u,v,d in net.edges(data=True)])

        pos=nx.spring_layout(net)
        nx.draw_networkx_edge_labels(net,pos,edge_labels=edge_labels)
        nx.draw(net,pos,with_labels=True,arrows=True)
        plt.show()
        plt.waitforbuttonpress()






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

myButton = tk.Button(root,text = "Solve")
myButton.grid(row=1,column=3,pady=10)

stats = "Not Yet Loaded"
myLabelStats = tk.Label(root,text = stats)
myLabelStats.grid(row = 7,column=0,pady=10,padx=20,columnspan=3)

root.mainloop()
