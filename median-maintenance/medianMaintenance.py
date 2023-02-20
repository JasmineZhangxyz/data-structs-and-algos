# Author: Xiyue Zhang
# Date Started: July 1, 2020
# Last Revised: July 5th, 2020


# --------------------- OBJECTIVE ---------------------
# The goal of this problem is to implement the "Median Maintenance" algorithm.
# The text file contains a list of the integers from 1 to 10000 in unsorted order; you should treat this as a stream of
# numbers, arriving one by one.
# Letting x_i denote the ith number of the file, the kth median m_k is defined as the median of the numbers x_1, ..., x_k.
# If k is odd, then m_k is ((k + 1) / 2)th smallest number among x_1, ..., x_k; if k is even, then m_k is the (k_2)th
# smallest number among x_1, ..., x_k.)
# The answer is given as the sum of these 10000 medians, modulo 10000.


from heapq import heappush, heappop
# heapq is for min heaps. It can be easily adjusted to work for max heaps.
# heappush(heap, item): pushes the value item onto the heap; maintains the heap invariant.
# heappop(heap): pops and returns the smallest item from the heap; maintains the heap invariant.
#                If the heap is empty, IndexError is raised.
# heapify(x) (not used in this code but good to know): transforms list x into a heap, in-place, in linear time.


def file_to_array(filename):
    array1 = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        array1.append(int(line))
    return array1


# -------------------- BRUTE FORCE --------------------
def brute_force_median(array1):
    med_sum = 0
    for i in range(len(array1)):
        partial_array = array1[0: i + 1]
        partial_array.sort()
        length = len(partial_array)
        if length % 2 == 0:
            median = partial_array[int(length / 2) - 1]
        else:
            median = partial_array[int((length + 1) / 2) - 1]
        med_sum += median
    answer = med_sum % len(array1)
    return answer


# ---------------- HEAP IMPLEMENTATION ----------------
def median_maintenance(a):
    sum_of_med = 0
    min_heap = []
    max_heap = []
    for item in a:
        if min_heap == [] and max_heap == []:
            heappush(min_heap, item)
        elif item < curr_med:
            heappush(max_heap, -1 * item)  # adds item to max_heap
        else:
            heappush(min_heap, item)  # adds item to min_heap

        # balance heap sizes (& maintain heap properties)
        if (len(min_heap) - len(max_heap)) > 1 or (len(max_heap) - len(min_heap)) > 1:
            if len(min_heap) > len(max_heap):
                # take top out of min heap & give to max heap
                top = heappop(min_heap)
                heappush(max_heap, -1 * top)
            else:
                # take top out of max heap & give to min heap
                top = -1 * heappop(max_heap)
                heappush(min_heap, top)

        # find curr_med
        if len(min_heap) == len(max_heap):
            curr_med = -1 * max_heap[0]  # top value of max heap
        else:
            if len(min_heap) > len(max_heap):
                curr_med = min_heap[0]  # top value of min heap
            else:
                curr_med = -1 * max_heap[0]  # top value of max heap
        sum_of_med += curr_med
    return sum_of_med % len(a)


if __name__ == "__main__":
    testfile = "Median.txt"
    test_array = file_to_array(testfile)
    print("Brute Force Method: ")
    bf = brute_force_median(test_array)
    print(bf)
    print("Heap Implementation: ")
    hm = median_maintenance(test_array)
    print(hm)
    if bf == hm:
        print("The results are consistent.")
    else:
        print("The results are inconsistent.")
