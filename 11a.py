#scenario 1:Dividing a number by zero
num=100
try:
    result=num/0#Attempt to divide by zero
except ZeroDivisionError as e:
    print(f"Error:Cannot divide by zero.{e}")#Handle division by zero error
#Scenario 11:Importing a library that doesn't exit
try:
  import matheqn#Trying to import a non-existing module
except ImportError as e:
   print(f"Error:Library'matheqn'not found.{e}")#Handle module import error
#Scenario 111:Accessing an invalid index in a list
num_list=[10,20,30]
try:
   print(num_list[5])#Trying to access the fifth index(out of range)
except IndexError as e:
   print(f"Error:List index out of range.{e}")#Handle list index out of the range error
#Scenario iv:Accessing an invalid key in a dictionary
Dict_Univ={'1':"MBU",'2':"Tirupathi",'3':"CSE"}
try:
  print(Dict_Univ['5'])#Trying to access a non-existing key
except KeyError as e:
   print(f"Error:key'5'not found in the dictionary.{e}")#Handle key error in dictionary






    

        