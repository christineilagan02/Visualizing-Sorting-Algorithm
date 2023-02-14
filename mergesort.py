
def merge_sort(data, drawData, timeTick):
    merge_sort_algo(data, 0, len(data)-1, drawData, timeTick)

def merge_sort_algo(data, left, right, drawData, timeTick):
    if left < right:
        middle = ( left + right) // 2
        merge_sort_algo(data, left, middle, drawData, timeTick)
        merge_sort_algo(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)
        
def merge(data, left, middle, right, drawData, timeTick):
    leftpart = data[left : middle+1]
    rightpart = data[middle+1 : right+1]
    
    leftIdx = rightIdx = 0
    
    for dataIdx in range(left, right):
        if leftIdx < len(leftpart) and rightIdx < len(rightpart):
            if leftpart[leftIdx] <= rightpart[rightIdx]:
                data[dataIdx] = leftpart[leftIdx]
                leftIdx +=1
            else:
                data[dataIdx] = rightpart[rightIdx]
                rightIdx +=1
                
        elif leftIdx < len(leftpart):
            data[dataIdx] = leftpart[leftIdx]
            leftIdx +=1
        else:
            data[dataIdx] = rightpart[rightIdx]
            rightIdx +=1
            
data = [55, 13, 11, 88, 63, 17, 29, 94, 5, 92]
merge_sort(data, 0, 0)
print(data)