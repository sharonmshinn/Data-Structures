
import random
import time

def swap(the_list,i,j):
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp

def quicksort(the_list,left=0,right=None):
    if right is None:
        right = len(the_list)-1
    #print(f"quicksort from {left} to {right}")

    # recursive case - if left == right we are of length 1
    if left < right:

        # is alex crazy?
        mid = (right + left) // 2

        #print(f"Pivot candidates: L:{the_list[left]}, M:{the_list[mid]}, R:{the_list[right]}")
        
        # pivot
        if the_list[right] < the_list[left]:
            swap(the_list,right,left)
        # guarantee: the_list[right] >= the_list[left]
        if the_list[mid] < the_list[left]:
            swap(the_list,mid,left)
        # guarantee: the_list[mid] >= the_list[left]
        # guarantee: the_list[left] <- not the median-est
        # so at this point, we just want the lower of the
        # REMAINING two values in the_list[right]
        if the_list[mid] < the_list[right]:
            swap(the_list,mid,right)

        #the_list[right] <--- PIVOT
        #print(f"Selected pivot: {the_list[right]}")

        i = left
        next_available = left

        # compare each value to pivot value
        while i < right:
            if the_list[i] < the_list[right]:
                swap(the_list,i,next_available)
                next_available += 1
            i += 1

        # swap in the pivot
        swap(the_list,next_available,right)

        #print(the_list)

        quicksort(the_list,left,next_available-1)
        quicksort(the_list,next_available+1,right)
    #else:
        #print("(base case)")

    
    

def mergesort(the_list, v=0, depth=0):
    #v = verbosity

    #print("\t"*depth,end="")
    #print(f"{the_list} begins")
    
    # recursive case
    if len(the_list) > 1:

        # split list into two equal sublists
        # if list has odd # of elements, extra element goes right
        middle_index = len(the_list)//2
        left_list = the_list[:middle_index]
        right_list = the_list[middle_index:]

        # perform recursive sorts
        mergesort(left_list,depth+1)
        mergesort(right_list,depth+1)

        merged_index = 0
        left_index = 0
        right_index = 0

        # comparison loop
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                # left is smaller
                the_list[merged_index] = left_list[left_index]
                left_index += 1
            else:
                # right is smaller (or they're equal)
                the_list[merged_index] = right_list[right_index]
                right_index += 1
            merged_index += 1

        # left dump
        while left_index < len(left_list):
            the_list[merged_index] = left_list[left_index]
            left_index += 1
            merged_index += 1

        # right dump
        while right_index < len(right_list):
            the_list[merged_index] = right_list[right_index]
            right_index += 1
            merged_index += 1

        

        
    # base case implicit - don't do anything
    #print("\t"*depth,end="")
    #print(f"{the_list} ends")
        
if __name__ == "__main__":
    my_list = list()
    for i in range(1000):
        my_list.append(random.randint(0,10))
    #print(f"Unsorted: {my_list}")
    start_time = time.time()
    quicksort(my_list)
    end_time = time.time()
    print(end_time-start_time)
    #print(f"Sorted: {my_list}")
