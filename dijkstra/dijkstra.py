# Author: Xiyue Zhang
# Date Started: June 24, 2020
# Date Completed:


def file_to_graph(filename):
    """

    :param filename: input file of an undirected, weighted graph. Each row consists of node tuples.
    :return: nested list graph representation
    """
    g = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        data = line.split("\t")
        temp_array = [int(data[0])]
        for i in range(1, len(data)):
            j = data[i].split(",")
            temp_tuple = (int(j[0]), int(j[1]))
            temp_array.append(temp_tuple)
        g.append(temp_array)
    return g


def dijkstra(g, s, t):
    # g is the graph
    # s is the source node
    # -------- GET LIST OF NODES IN g --------
    v = []
    for i in g:
        v.append(i[0])
    # --------- INITIALIZE VARIABLES ---------
    x = [s]  # vertices processed so far
    a = {s: 0}
    # a[s] = 0   compute shortest path distances
    # -------------- MAIN LOOP ---------------
    while x != v:
        v = None
        w = None
        temp_list = []
        temp_dist = []
        # identify edges where the tail is in x and the head is not
        for node in g:
            if node[0] in x:
                for k in range(1, len(node)):
                    if node[k][0] not in x:
                        # pick edge (v, w) that minimizes A[v] + l_vw
                        dist = a[node[0]] + node[k][1]
                        temp_list.append([int(dist), node[0], node[k][0]])
                        temp_dist.append(int(dist))
        minimum_dist = min(temp_dist)
        for item in temp_list:
            if item[0] == minimum_dist:
                v = item[1]
                w = item[2]
        x.append(w)
        a.update({w: minimum_dist})
        if w == t:
            break
        if (x == v) and (w != t):
            return 1000000
    return a[w]


if __name__ == "__main__":
    testfile = "dijkstraData.txt"
    g = file_to_graph(testfile)
    print(g)
    testing = dijkstra(g, 1, 197)
    print(testing)
