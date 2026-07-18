#part1:constructing a list of odd numbers from 1to10
odd_numbers=list(filter(lambda x:x%2!=0,range(1,11)))
print("odd numbers from 1 to 10:",odd_numbers)
#part2:constructing a list of negative numbers from -7to 7
negative_numbers=list(filter(lambda x:x<0,range(-7,8)))
print("negative numbers from -7to7:",negative_numbers)
#part3:finding the biggest number from a list of numbers
numbers_list=[2,4,7,1,9,5]
biggest_number=max(numbers_list)
print("the biggest number in the list is:",biggest_number)

