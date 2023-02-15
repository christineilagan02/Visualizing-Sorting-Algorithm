import time

def selection_sort(data):

    for i in range(len(data)-1):
        smallval = i
        for j in range(i, len(data)-1):
            if data[j] < data[smallval]:
                smallval = j
                
        data[i], data[smallval] = data[smallval], data[i] 
        



data = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
selection_sort(data)

print(data)