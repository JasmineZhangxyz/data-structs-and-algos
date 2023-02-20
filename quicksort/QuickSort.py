def file_to_array(filename):
    array1 = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        array1.append(int(line))
    return array1


def quickSort(a, start, end):
    """
    :param a: array to be sorted
    :param start: starting index
    :param end: ending index
    :return: number of comparisons used to sort the given array
    How to count: when there is a recursive call on a subarray of length m, you should simply add m - 1 to your running
    total of comparisons. (This is because the pivot element is compared to each of the other m − 1 elements in the
    subarray in this recursive call.)
    """
    if (end - start) <= 1:
        return 0
    else:
        # find pivot value
        p = choosePivot(a, start, end)
        # partition around pivot; count the comparisons
        count = partition(a, start, end, p)
        # recurse on the 1st half of the array
        count += quickSort(a, start, a.index(p))
        # recurse on the 2nd half of the array
        count += quickSort(a, a.index(p) + 1, end)
    return count


def choosePivot(a, start, end):
    # --------------- USE FIRST ELEMENT OF ARRAY AS PIVOT ---------------
    # p = a[start]
    #
    # -------------------------------------------------------------------
    # --------------- USE FINAL ELEMENT OF ARRAY AS PIVOT ---------------
    # p = a[end - 1]
    #
    # -------------------------------------------------------------------
    # -- USE THE MEDIAN OF THE START, MIDDLE, AND END INDICES AS PIVOT --
    if (end - start) % 2 == 0:
       middle = a[int(((end - start) / 2) - 1 + start)]
    else:
       middle = a[int(((end - start) / 2) - 0.5 + start)]
    b = [a[start], middle, a[end - 1]]
    b.sort()
    p = b[1]
    # -------------------------------------------------------------------
    return p


def partition(a, l, r, p):
    # l is the leftmost element
    # r is the rightmost element
    #
    # --------------- USE FINAL ELEMENT OF ARRAY AS PIVOT ---------------
    # a[r - 1], a[l] = a[l], a[r - 1]
    #
    # -------------------------------------------------------------------
    # -- USE THE MEDIAN OF THE START, MIDDLE, AND END INDICES AS PIVOT --
    a[a.index(p)], a[l] = a[l], a[a.index(p)]
    #
    # -------------------------------------------------------------------
    p = a[l]
    i = l + 1
    for j in range(l + 1, r):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    # insert pivot where it belongs
    a[l], a[i - 1] = a[i - 1], a[l]
    # return the number of comparisons done
    return (r - l) - 1


if __name__ == "__main__":
    testfile = "TestFile.txt"
    a = file_to_array(testfile)
    n = len(a)
    q = quickSort(a, 0, n)
    print(q)
    print(a)
