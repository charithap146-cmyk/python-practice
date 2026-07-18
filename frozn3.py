def sum_of_numbers_divisible_by_4():
    total_sum=0#initialize the sum to 0 
    while True:
        try:
            #accept the user input
            number=int(input("enter a number(or type'exit to stop):"))
            #check if the number is divible by 4
            if number%4==0:
                total_sum+=number#add to the sum if divisible by 4
                print(f"added{number}to the sum.")
            else:
                print(f"{number}is not divisible by 4,so it is not added to the sum.")
        except ValueError:
            #if the user types'exit'or a non-integer value,break the loop
            exit_input=input("do you want to stop?(yes/no):").lower()
            if exit_input=='yes':
                break
            else:
                continue #if not stopping,continue the loop
        print(f"\nfinal sum of numbers divisible by 4:{total_sum}")
#call the function to run the program
sum_of_numbers_divisible_by_4()

     
