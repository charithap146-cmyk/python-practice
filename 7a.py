def hanoi(n,source,target,auxiliary):
    #base case:when only one disk is left
    if n==1:
        print(f"move disk 1 from{source} to {target}")
        return
    #move n-1 disks from source to auxiliary,so they are out of the way
    hanoi(n-1,source,auxiliary,target)
    #move the nth disk from source to target
    print(f"move disk{n}from{source}to{target}")
    #move the n-1 disks from auxiliary to target
    hanoi(n-1,auxiliary,target,source)
    #number of disks
    n=3
    #calling the hanoi function
    print(f"steps to solve towers of hanoi with{n}disks:")
    hanoi(n,'A','C','B')#A is source,B is a auxiliary,C is target
    