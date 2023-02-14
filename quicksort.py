def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]
    
    for j in range(head, tail):
        if (data[j] < pivot):
            data[border], data[j] = data[j], data[border]
            border +=1
            
# swapping pivot element with border value
            
    data[border], data[tail] = data[tail], data[border]
    return border
    

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)
        
        # LEFT Partition
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)
        
        # now for RIGHT Partition
        
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)
        
        
        
        
        
# now let's check whether our algorithm is correct or not

data = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
quick_sort(data, 0, len(data)-1, 0, 0)
print(data)