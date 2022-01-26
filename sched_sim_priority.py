import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    my_pq = PriorityQueue()
    my_pq.display()
    my_pq.enqueue(5,'priority five')
    my_pq.display()
    my_pq.enqueue(10,'priority ten')
    my_pq.display()
    my_pq.enqueue(1,'prorority two')
    my_pq.display()
    my_pq.dequeue()
    my_pq.display()
    my_pq.dequeue()
    my_pq.display()
    
    print(my_pq)
    print(my_pq.peek())

def left(n):
    return 2*n+1

def right(n):
    return 2*n+2

def parent(n):
    return (n-1)//2

class PriorityQueue:

    def __init__(self):
        self.min_heap = []

    def enqueue(self,priority,value):
        logging.debug(f"Enqueuing {value}, priority {priority}")
        self.min_heap.append((priority,value))
        self.bubble_up(len(self.min_heap)-1)

    def peek(self):
        if len(self.min_heap) == 0:
            raise EmptyError()
        return self.min_heap[0][1]

    def dequeue(self):
        logging.debug(f"Dequeuing {self.min_heap[0]}")
        if len(self.min_heap) == 0:
            raise EmptyError()
        return_value = self.min_heap[0][1]
        last_node = self.min_heap.pop()
        self.min_heap[0] = last_node
        self.bubble_down(0)
        return return_value

    def bubble_up(self,n):
        
        if n == 0:
            return
        elif self.min_heap[n][0] >= self.min_heap[parent(n)][0]:
            return
        else:
            temp = self.min_heap[parent(n)]
            self.min_heap[parent(n)] = self.min_heap[n]
            self.min_heap[n] = temp
            self.bubble_up(parent(n))

    def bubble_down(self,n):
        #if no children
        if left(n) >= len(self.min_heap):
            return
        #if one child
        elif right(n) >= len(self.min_heap):
            if self.min_heap[n][0] > self.min_heap[left(n)][0]:
                temp = self.min_heap[left(n)]
                self.min_heap[left(n)] = self.min_heap[n]
                self.min_heap[n] = temp
        #if two children
        else:
            #find smallest of three nodes
            smallest = "n"
            smallest_priority = self.min_heap[n][0]
            if self.min_heap[left(n)] > smallest_priority:
                smallest = "left(n)"
                smallest_priority = self.min_heap[left(n)][0]
            if self.min_heap[right(n)][0] < smallest_pri:
                smallest = "right(n)"
            #swap and recurse if necessary
            if smallest == "left(n)":
                temp = self.min_heap[left(n)]
                self.min_heap[left(n)] = self.min_heap[n]
                self.min_heap[n] = temp
                self.bubble_down(left(n))
            elif smallest == "right(n)":
                temp = self.min_heap[right(n)]
                self.min_heap[right(n)] = self.min_heap[n]
                self.min_heap[n] = temp
                self.bubble_down(right(n))

    def display(self,n=0, path="X"):
        if n < len(self.min_heap):
            print(f"{path}: {self.min_heap[n]}")
        if left(n) < len(self.min_heap):
            self.display(left(n),path+"L")
        if right(n) < len(self.min_heap):
            self.display(left(n),path+"R")
            
        

    def __str__(self):
        output_string = "PQ["
        output_string += ",".join([repr(x) for x in self.min_heap])
        output_string += "]"
        return output_string

    def EmptyError(Exception):
        pass


    
        
    



if __name__ == "__main__":
    main()
