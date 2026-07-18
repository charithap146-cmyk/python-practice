def check_smaller_elements(tup):
    #iterate over the tuple(excluding the last element,as it has no next element)
    for i in range(len(tup)-1):
        if tup[i]>tup[i+1]:
            print(tup[i+1],end="")#print smaller element if it exists
            print(-1,end="")#if no smaller element,print-1
            #for the last element,print-1 as there is no next element
            print(-1)
            #example input tuple
            input_tuple=(4,2,1,5,3)
            #call the function with the example tuple
            check_smaller_elements(input_tuple)
            
    

        














                

