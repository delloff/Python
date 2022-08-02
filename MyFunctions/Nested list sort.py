#Bubble sort

def nested_list_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if (arr[j][1] > arr[j + 1][1]):
                tempo = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tempo
    return arr

print(flatten_and_sort([[3, 9, 16, 32], [7, 9, 85], [6, 4, 9]]))  #[[6, 4, 9], [3, 9, 16, 32], [7, 9, 85]]
