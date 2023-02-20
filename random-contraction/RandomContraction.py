# ------------------------------
# Author: Jasmine Zhang
# Date Created: June 11, 2020
# Description: Working version of Random Contraction.
# ------------------------------

import random


def file_to_adjacency_list(filename):
    adj_array = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        data = line.split("\t")
        for i in range(len(data)):
            data[i] = int(data[i])
        adj_array.append(data)
    return adj_array


def randomContraction(graph):
    while (len(graph) > 2):
        # pick edge at random
        v_array = random.choice(graph)
        v = v_array[0]
        w = random.choice(v_array)
        while w == v:
            w = random.choice(v_array)
        # merge v and w into a single vertex
        contract(graph, v_array, w)
    mincut = len(v_array) - 1
    return mincut


def contract(graph, v_array, w):
    # ----------- FIND W'S ARRAY -----------
    for node in graph:
        if node[0] == w:
            w_array = node
            break
    # ------ DELETE W'S FROM V ARRAY -------
    v_array = delete_element_from_array(v_array, w)
    # ------- DELETE SELF-LOOPS IN V -------
    v_array = delete_self_loops(v_array)
    # ------------ MERGE W TO V ------------
    for i in range(1, len(w_array)):
        if (w_array[i] != v_array[0]) and (w_array[i] != w):  # avoid self-loops
            v_array.append(w_array[i])
    # ---------- DELETE W'S ARRAY ----------
    graph.remove(w_array)
    # -------- ALTER OTHER VERTICES --------
    for node in graph:
        if (node != v_array) and (node != w_array):
            for i in range(1, len(node)):
                if node[i] == w:
                    node[i] = v_array[0]
    # --------------------------------------
    return graph


def delete_element_from_array(a, element):
    i = 0
    for item in a:
        if item == element:
            i += 1
    for j in range(0, i):
        a.remove(element)
    return a


def delete_all_self_loops(graph):
    for node in graph:
        node = delete_self_loops(node)
    return graph


def delete_self_loops(a):
    element = a[0]
    j = 0
    for i in range(1, len(a)):
        if a[i] == element:
            a[i] = 0
            j += 1
    for k in range(0, j):
        a.remove(0)
    return a


def trials(filename):
    adj_array = file_to_adjacency_list(filename)
    trial = randomContraction(adj_array)
    return trial


if __name__ == "__main__":
    testfile = "kargerMinCut.txt"
    trial_num = 10000
    cuts = []
    i = 0
    while (i < trial_num):
        trial = trials(testfile)
        cuts.append(trial)
        i += 1
    min_cut = min(cuts)
    print(min_cut)

