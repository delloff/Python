# replace 1 with 0 and vice versa

arr =  [[1,1,0],
        [1,0,1],
        [0,0,0]]

# option 1
for row in arr:
    for index, val in enumerate(row):
        row[index] = 0 if val > 0 else 1

#-------------------------------------------

# option 2
for row in arr:
    for index, val in enumerate(row):
        if val > 0:
            row[index] = 0
        else:
            row[index] = 1

        

print(arr)
