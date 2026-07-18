def calculate_final_bill(food_type,quantity,distance):
    #validate input
    if food_type not in['v','N']:
        return -1 #invalid food type
    if distance<=0:
        return -1 #invalid distance
    if quantity<1:
        return -1 #invalid quantity
    #Food cost calculation
    if food_type=='v':
        food_cost=120*quantity#vegetarian combo cost
    else:
        food_cost=150*quantity#Non_vegetarian combo cost
        #Delivery charge calculation
        if distance<=3:
            delivery_charge=0
        elif distance<=6:
            delivery_charge=(distance-3)*3#3Rs per km for distance between 4-6km
        else:
            delivery_charge=3*3+(distance-6)*6 #First 3km free, next 3km at 3Rs/km,reamaining at 6Rs/km
            #total bill
            total_bill=food_cost+delivery_charge
            return total_bill
            #input from the customer
            food_type=input("Enter food type(v for vegetarian,N for Non-vegetatrian):").upper()
            quantity=int(input("Enter the quantity(number of plates):"))
            distance=float(input("Enter the distance(inkms):"))
            #calculate the final bill
            final_bill=calculate_final_bill(food_type,quantity,distance)
            #Display the result
            if final_bill==-1:
                print("invalid input.please check the data provided.")
            else:
                print(f"the total bill amount to be paid is:Rs.{final_bill:.2f}")
