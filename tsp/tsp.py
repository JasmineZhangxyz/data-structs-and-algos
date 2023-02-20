# Author: Xiyue Zhang
# Date Created: September 1, 2020
# Last Revised: September 3, 2020


import math
import itertools


def file_to_array(filename):
    coordinates = {}
    f = open(filename, "r")
    lines = f.readlines()
    lines[0] = lines[0].rstrip()
    num_of_vertices = int(lines[0])
    for i in range(1, len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i].split()
        temp = []
        for num in lines[i]:
            temp.append(float(num))
        coordinates.update({i: (temp[0], temp[1])})
    return coordinates, num_of_vertices


def travelling_salesman(coordinates, num_of_vertices):
    # --------------- CREATE A DICTIONARY, a, TO STORE VALUES ---------------
    vertices = []
    for vertex in range(1, num_of_vertices + 1):
        vertices.append(vertex)

    all_subsets = []
    for size in range(1, 2):  # ONLY SETTING UP BASE CASE
        ss = list(itertools.combinations(vertices, size))
        refine_ss = refine_subset(ss)
        all_subsets += refine_ss

    a = base_case(all_subsets, num_of_vertices)

    # ---------------------------- FILL IN ARRAY ----------------------------
    for m in range(2, num_of_vertices + 1):  # m = subproblem size
        print(m)
        #ss = list(itertools.combinations(vertices, m))
        #refine_ss = refine_subset(ss)
        refine_ss = create_new_subsets(refine_ss, num_of_vertices)
        update_a = base_case(refine_ss, num_of_vertices)
        a.update(update_a)
        for s in refine_ss:
            temp_s = list(s)
            for j in s:
                if j != 1:
                    minimum = 100000000
                    new_list = temp_s.copy()
                    new_list.remove(j)  # partial s without j
                    for k in new_list:  # k != j
                        c_kj = calculate_euclidean_dist(k, j, coordinates)
                        partial_s_with_k = tuple(new_list) + (k,)
                        temp_cost = a.get(partial_s_with_k) + c_kj
                        if temp_cost < minimum:
                            minimum = temp_cost
                    a.update({(s + (j,)): minimum})
        # clearing out some memory
        a = clean_up_memory(a, m)
    answer = 100000000
    full_set = tuple(i for i in vertices)
    for j in range(2, num_of_vertices + 1):
        c_j1 = calculate_euclidean_dist(j, 1, coordinates)
        possible_answer = a.get(full_set + (j,)) + c_j1
        if possible_answer < answer:
            answer = possible_answer
    return answer


def refine_subset(subset):
    # removes all subsets that do not contain 1
    to_delete = []
    for s in subset:
        if s[0] != 1:
            to_delete.append(s)
    for d in to_delete:
        subset.remove(d)
    return subset


def base_case(subsets, num_of_vertices):
    a = {}
    for subset in subsets:
        for j in range(1, num_of_vertices + 1):
            if j == 1:
                # BASE CASES
                if subset == (1,):
                    a.update({(subset + (j,)): 0})
                else:
                    a.update({(subset + (j,)): 100000000})  # meant to represent infinity
            else:
                a.update({(subset + (j,)): None})
    return a


def calculate_euclidean_dist(k, j, coordinates):
    x = coordinates.get(k)[0]
    y = coordinates.get(k)[1]
    z = coordinates.get(j)[0]
    w = coordinates.get(j)[1]
    c_kj = math.sqrt((x - z) ** 2 + (y - w) ** 2)
    return c_kj


def clean_up_memory(a, m):
    to_del = []
    for key in a.keys():
        if len(key) == m:
            to_del.append(key)
    for del_key in to_del:
        del a[del_key]
    return a


def create_new_subsets(subset, num_of_vertices):
    new_subsets = []
    for s in subset:
        for i in range(2, num_of_vertices + 1):
            if i > s[-1]:
                new_s = s + (i,)
                new_subsets.append(new_s)
    return new_subsets


if __name__ == "__main__":
    testfile = "TestFile.txt"
    data = file_to_array(testfile)
    ans = travelling_salesman(data[0], data[1])
    print(ans)
