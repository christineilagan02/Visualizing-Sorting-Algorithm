def bubble_sort(data):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data [j+1]:
                data[j], data[j+1] = data[j+1], data[j]     # swaping
    return data

data = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
data = bubble_sort(data)
print(data)