import time

def selection_sort(data, drawData, timeTick):

    for i in range(len(data)-1):
        smallval = i
        for j in range(i, len(data)):
            if data[j] < data[smallval]:
                smallval = j
                
        data[i], data[smallval] = data[smallval], data[i] 
        
        drawData(data, ['yellow' if x == i or x == smallval else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)  
    
    drawData(data, ['yellow' for x in range (len(data))])
