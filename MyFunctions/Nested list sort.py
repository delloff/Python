def flatten_and_sort(arr):
    for sublist in arr:
        for i in range(len(sublist)-1):
            if (arr[i][2] > arr[i + 1][2]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1]= temp
    return arr


print(flatten_and_sort([[3, 9, 16], [7, 9, 85], [6, 4, 9]]))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
