import time

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        
        drawData(data, ['yellow' if x == i or x == key or x == j else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)   
        
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key
        
        drawData(data, ['yellow' if x == j or x == j+1 or x == j-1 else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)    
    
    drawData(data, ['yellow' for x in range (len(data))])
