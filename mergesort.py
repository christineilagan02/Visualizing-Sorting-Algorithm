
import time

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1
        drawData(data, ['yellow' if x >= start and x < mid else 'orange' if x == mid 
                else 'white' if x > mid and x <=end else 'gray' for x in range(len(data))])
        time.sleep(timeTick)

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, ['yellow' if x >= start and x < mid else 'orange' if x == mid 
                        else 'white' if x > mid and x <=end else 'gray' for x in range(len(data))])
        time.sleep(timeTick)