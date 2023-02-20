# Author: Xiyue Zhang
# Date Started: July 9, 2020
# Last revised:


def file_to_array(filename):
    array1 = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        array1.append(int(line))
    return array1


# --------------- BRUTE FORCE ---------------
def find_distinct(a):
    distinct = []
    size_of_a = len(a)
    for i in range(size_of_a):
        distinctness = True
        for j in range(size_of_a):
            if i != j and a[i] == a[j]:
                distinctness = False
                break
        if distinctness:
            distinct.append(a[i])
    return distinct


def brute_force(distinct, t):
    size_of_distinct = len(distinct)
    for k in range(size_of_distinct):
        n = k + 1
        for m in range(n, size_of_distinct):
            if distinct[k] + distinct[m] == t:
                return True
    return False


# -------- IMPLEMENTING HASH TABLES ---------
def create(a, _size):
    # avoiding using even numbers as the mod later
    if _size % 2 == 0:
        ht = [[] for _ in range(_size + 3)]
    else:
        ht = [[] for _ in range(_size)]
    # insert elements from array a into hashtable, avoiding duplicates
    duplicates = []
    for item in a:
        bucket = ht[item % len(ht)]
        if item not in bucket:
            bucket.append(item)
        else:
            duplicates.append(item)
    # remove remaining duplicates
    for thing in duplicates:
        buck_num = thing % len(ht)
        ht[buck_num].remove(thing)
    filter_a = []
    for item in a:
        if item not in duplicates:
            filter_a.append(item)
    return ht, filter_a


def two_sum(ht, a, t):
    # hashtable, dupes = create(a, len(a))
    for item in a:
        b = ht[(t - item) % len(ht)]
        if (t - item) in b:
            print(b)
            return True
    return False


if __name__ == "__main__":
    testfile = "TestFile.txt"
    test_array = file_to_array(testfile)
    #filtered_array = find_distinct(test_array)
    #print(filtered_array)
    #testing = brute_force(filtered_array, 9)
    #print(testing)
    count = 0
    hashtable, new_a = create(test_array, len(test_array))
    print(len(new_a))
    for i in range(3, 11):
        temp = two_sum(hashtable, new_a, i)
        if temp:
            count += 1
    print(count)
