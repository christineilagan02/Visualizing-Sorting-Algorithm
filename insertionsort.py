

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1 
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key  

data = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
insertion_sort(data)

print(data)