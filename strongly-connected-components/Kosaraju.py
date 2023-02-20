# Author: Xiyue Zhang
# Date Started: June 19th, 2020
# Last Revised:


import sys
import threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def file_to_array(filename):
    graph_array = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = line.split()
        temp = []
        for num in line:
            temp.append(int(num))
        graph_array.append(temp)
    return graph_array


# -------------- GLOBAL VARIABLES ---------------
t = 0  # number of nodes processed so far (finishing times)
s = None  # current source vertex (leaders)
explored = []
finish_times = {}
scc_dict = {}
N = 875714  # number of nodes; constant
#N  = 12
g_nodes = {}  # nodal representation of reversed graph


def edge_to_node(g):
    """
    takes
    :param g: directed graph represented by nodes, where i is the tail and j is the head [[i, j], [...], ...]
    :return: directed graph represented by a dictionaries, where the key is the node, i, and the value is the list
    of its connections {i: [j, ...], ...}
    """
    global g_nodes
    for edge in g:
        if edge[0] in g_nodes.keys():
            g_nodes[edge[0]].append(edge[1])
        else:
            g_nodes.update({edge[0]: [edge[1]]})


def kosaraju(g):
    # --- GLOBAL VARIABLES THAT'LL BE EDITED ----
    global s
    global explored
    global scc_dict
    global g_nodes
    # ------------- REVERSE GRAPH G -------------
    for edge in g:
        edge[0], edge[1] = edge[1], edge[0]

    # ---- TURN EDGE REPRESENTATION TO NODES ----
    edge_to_node(g)
    print("first edge_to_node done")

    # ----- ASSIGN FINISHING TIMES TO NODES -----
    dfs_loop(g)
    print("first dfs_loop done")

    # -- REASSIGN NODE VALUES & REVERSE EDGES ---
    for edge in g:
        edge[0] = finish_times[edge[0]]
        edge[1] = finish_times[edge[1]]
        edge[0], edge[1] = edge[1], edge[0]

    # ---- TURN EDGE REPRESENTATION TO NODES ----
    g_nodes = {}
    edge_to_node(g)
    print("second edge_to_node done")

    # ------------ IDENTIFY LEADERS -------------
    s = None  # reset some variables for second loop
    explored = []
    scc_dict = {}
    dfs_loop(g)


def dfs_loop(g):
    global s
    # ---------- FROM i = n DOWN TO 1 -----------
    for i in reversed(range(1, N + 1)):
        if i in g_nodes.keys() and i not in explored:
            s = i  # i becomes the leader for any nodes that can be reached from it
            dfs(g, i)


def dfs(g, i):
    # --- GLOBAL VARIABLES THAT'LL BE EDITED ----
    global t
    global explored
    global finish_times
    global scc_dict
    # -------------------------------------------
    # mark i as explored
    explored.append(i)
    # set leader(i) = node s
    if s in scc_dict.keys():
        scc_dict[s].append(i)
    else:
        scc_dict.update({s: [i]})
    # for each arc (i, j) in g
    edges = g_nodes.get(i)
    if edges:
        for j in edges:
            if j not in explored:
                dfs(g, j)
    t += 1
    # set f(i) = t
    ft = {i: t}
    # global variable finish_times will keep track of f(i)
    finish_times.update(ft)


def find_top_five(scc_dictionary):
    top_five = []
    # convert scc_dict to list of sizes of scc
    size_list = []
    for key in scc_dictionary:
        size = len(scc_dictionary.get(key))
        size_list.append(size)
    for j in range(0, 5):
        if not size_list:
            top_five.append(0)
        else:
            largest = max(size_list)
            top_five. append(largest)
            size_list.remove(largest)
    return top_five


def main():
    testfile = "SCC.txt"
    g = file_to_array(testfile)
    kosaraju(g)
    answer = find_top_five(scc_dict)
    print(answer)


thread = threading.Thread(target=main)
thread.start()
