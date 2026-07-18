#step1:collect data from the user
list_data=input("enter details about list(e.g.,[1,2,3,4]):")
tuple_data=input("enter details about tuple(e.g.,(1,2,3)):")
set_data=input("enter details about set(e.g.,{1,2,3}):")
dict_data=input("enter details about dictionary(e.g.,{'key':'value'}):")
#step2:open the file in write mode and collect the data
file_name='collect_literals_python.txt'
with open(file_name,'w')as file:
    file.write("details of collection literals in python:\n")
    file.write(f"list:{list_data}\n")
    file.write(f"tuple:{tuple_data}\n")
    file.write(f"set:{set_data}\n")
    file.write(f"dictionary:{dict_data}\n")
    #step3:open the file in read mode to read and display the contents
    with open(file_name,'r')as file:
        contents=file.read()
        print("\ncontents of the file'collect_literals_python.txt':")
        print(contents)
        