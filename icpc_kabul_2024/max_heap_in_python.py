
import heapq

class MaxHeap:

    def __init__(self) -> None:
        self.heap=[]
    def push(self,value):
        heapq.heappush(self.heap,-value)
    def pop(self):
        return -heapq.heappop(self.heap)
    def peak(self):
       return -self.heap[0] if self.heap else None
    def size(self):
        return  len(self.heap)
    


max_heap=MaxHeap()
max_heap.push(2)
max_heap.push(10)
max_heap.push(8)
max_heap.push(20)

print("Max element on the heap",max_heap.peak())
print("Max element on the heap pop",max_heap.pop())
print("size of heap",max_heap.size())