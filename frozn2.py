def calculate_electricity_bill(previous_unit,current_unit):
    #step1:calculate the total consumption
    consumption=current_unit-previous_unit
    #step2:define the rates for different slabs
    if consumption<=200:
        rate=3.0
    elif consumption<=250:
        rate=4.5
    elif consumption<=300:
        rate=5.2
    elif consumption<=400:
        rate=6.5
    else:
        rate=7.0
        #step3:calculate the bill
        bill=consumption*rate
        #step4:return the consumption and bill amount
        return consumption,bill
    #collect input from the user
    previous_unit=float(input("enter the previous unit reading(in kwh):"))
    current_unit=float(input("enter the current unit reading(in kwh):"))
    #ensure current unit is greater than previous unit
    if current_unit<previous_unit:
        print("current unit reading cannot be less than previous unit.please enter valid readings.")
    else:
        #calculate the electricity bill
        consumption,bill=calculate_electricity_bill(previous_unit,current_unit)
        #output the results
        print(f"\nelectricity consumption:{consumption}kwh")
        print(f"total bill:Rs.{bill:.2f}")


