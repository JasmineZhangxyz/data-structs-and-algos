# file has a long list of integers
# compute the number of inversions, where the ith row of the file indicates the ith entry of an array

# brute force method:
# go through array. for each entry, count the number of entries after it that is larger
# add up; return the value

def file_to_array(filename):
    array1 = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        array1.append(int(line))
    return array1

def brute_force(filename):
    array1 = file_to_array(filename)
    num_of_inversions = 0
    for i in range(len(array1)):
        for j in range(i + 1, len(array1)):
            if array1[i] > array1[j]:
                num_of_inversions += 1
    return num_of_inversions

def sort_and_count(array1, temp_array, start, length):
    # base case
    if (length - start) == 1:
        return 0
    # recursive case merge 2 arrays; expose inversions; return a sorted larger array
    else:
        # split the array
        mid = (length - start)/2 + start
        left = sort_and_count(array1, temp_array, start, mid)
        right = sort_and_count(array1, temp_array, mid, length)
        split = countSplitInv(array1, temp_array, start, mid, length)
    return left+right+split

def countSplitInv(array1, temp_array, start, mid, length):
    count = 0
    i = int(start)
    j = int(mid)
    for k in range(int(start), int(length)):
        if i < mid and j < length:
            if array1[i] < array1[j]:
                temp_array[k] = array1[i]
                i += 1
            else:
                temp_array[k] = array1[j]
                j += 1
                count += mid - i
        else:
            if i >= mid:
                temp_array[k] = array1[j]
                j += 1
            elif j >= int(length):
                temp_array[k] = array1[i]
                i += 1
            else:
                break
    for l in range(int(start), int(length)):
        array1[l] = temp_array[l]
    return count


if __name__ == "__main__":
    testfile = "TestFile.txt"
    testing1 = brute_force(testfile)
    print("Brute Force Method:")
    print(testing1)
    a = file_to_array(testfile)
    length = len(a)
    temp_a = [0]*length
    testing2 = sort_and_count(a, temp_a, 0, length)
    print("Divide and Conquer Method:")
    print(testing2)
    difference = testing1 - testing2
    print("")
    print("")
    print("---------- Testing Results ----------")
    if difference == 0:
        print("The answers are consistent!")
    else:
        print("The divide and conquer method is wrong")
