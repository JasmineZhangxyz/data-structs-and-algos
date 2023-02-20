# Author: Xiyue Zhang
# Date Started: July 21, 2020
# Last Revised: July 22, 2020


def file_to_array(filename):
    g = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        line = line.split()
        temp = []
        for num in line:
            temp.append(int(num))
        g.append(temp)
    return g


def clustering(g):
    k = 4  # target number of clusters
    curr_k = int(g[0][0])
    # delete first line
    g.remove(g[0])
    # make each point a separate cluster; make dictionary { point: [cluster the point is in] }
    points = []
    clusters = {}
    for edge in g:
        if edge[0] not in points:
            points.append(edge[0])
            clusters.update({edge[0]: [edge[0]]})
        if edge[1] not in points:
            points.append(edge[1])
            clusters.update({edge[1]: [edge[1]]})
    # combine clusters
    while curr_k != k:
        # find p, q = closest pair of separated points
        closest_dist = 1000000  # meant to represent infinity
        p = None
        q = None
        index_of_edge = None
        for edge in g:
            if (edge[2] < closest_dist) and (clusters.get(edge[0]) != clusters.get(edge[1])):
                p = edge[0]
                q = edge[1]
                closest_dist = edge[2]
                index_of_edge = g.index(edge)
        # update clusters
        p_cluster = clusters.get(p)
        q_cluster = clusters.get(q)
        new_cluster = p_cluster + q_cluster
        for node in p_cluster:
            clusters[node] = new_cluster
        for node in q_cluster:
            clusters[node] = new_cluster
        # delete the edge
        g.remove(g[index_of_edge])
        curr_k -= 1
    # find maximum spacing
    spacing = 1000000  # meant to represent infinity
    for edge in g:
        if clusters.get(edge[0]) != clusters.get(edge[1]) and edge[2] < spacing:
            spacing = edge[2]
    return spacing


if __name__ == "__main__":
    testfile = "clustering1.txt"
    test_array = file_to_array(testfile)
    part1 = clustering(test_array)
    print("answer for part 1: " + str(part1))
