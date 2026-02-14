from array import array
import heapq

def kth_smallestElement(arr,k):
    # Min heap of array
    heapq.heapify(arr)
    #print(f "Min heap Array:{arr}")

    #popping [k-1] element from heap
    for _ in range(k-1): 
        heapq.heappop(arr)
    
    #returning kth smallest element 
    return heapq. heappop(arr)

arr = [100,17,36,25,19,7,3,2,1]
K=4
print(f"Normal Array: {array}")
print(f"{k}th Smallest Element: {kth_smallestElement(array,k)}")

