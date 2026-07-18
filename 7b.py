def generate_fibonacci(n):
    fibonacci=[1,1]
    while len(fibonacci)<n:
        next_fib=fibonacci[-1]+fibonacci[-2]
        fibonacci.append(next_fib)
        return fibonacci[:n]
    def find_missing_numbers(fib_numbers,max_number):
        #generate a set of all numbers from 1 to max_number
        all_numbers=set(range(1,max_number+1))
        #find missing numbers by subtracting the fibonacci numbers set from the all numbers set
        missing_numbers=all_numbers-set(fib_numbers)
        return sorted(missing_numbers)
    #input from user
    n=int(input("enter the number of fibonacci numbers to generate:"))
    #generate the fibonacci series for n numbers
    fib_numbers=generate_fibonacci(n)
    #determine the maximum number in the fibonacci series
    max_number=fib_numbers[-1]
    #find and display the missing numbers
    missing_numbers=find_missing_numbers(fib_numbers,max_number)
    print(f"fibonacci numbers:{fib_numbers}")
    print(f"missing numbers:{missing_numbers}")
    

    