#Bubble sort

def nested_list_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j][2] > arr[j + 1][2]):     #swap nested arrays here
                tempo = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tempo
    return arr

print(nested_list_sort([[3, 9, 16, 32], [7, 9, 85], [6, 4, 9]]))  #[[6, 4, 9], [3, 9, 16, 32], [7, 9, 85]]
