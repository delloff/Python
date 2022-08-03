#Bubble sort

def nested_list_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):           # j == i because it accesses nested list, not nested list value
            if (arr[j][2] > arr[j + 1][2]):     # swap nested arrays here
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(nested_list_sort([[3, 9, 16, 32], [7, 9, 85], [6, 4, 9]]))  #[[6, 4, 9], [3, 9, 16, 32], [7, 9, 85]]

#------------------------------------------------
def nested_list_sort(arr):
    arr.sort(key = lambda l: l[2])
    return arr

#------------------------------------------------
def nested_list_sort(arr):
    return(sorted(arr, key = lambda i: i[2]))
