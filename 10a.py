#base class basic_info
class basic_info:
    def __init__(self):
        self.name=""
        self.rollno=""
        self.gender=""
    #function to get the basic information
    def getdata(self):
        self.name=input("enter name:")
        self.rollno=input("enter rollnumber:")
        self.gender=input("enter gender(Male/Female):")
        #function to display the basic information
        def display(self):
            print("\nbasic information:")
            print(f"name:{self.name}")
            print(f"roll number:{self.rollno}")
            print(f"gender:{self.gender}")
            #derived class physical_fit
class physical_fit(basic_info):
    def __init__(self):
    #initialize the base class constructor
        super().__init__()
        self.height=0.0
        self.weight=0.0
    #function to get the physical information
def getdata(self):
#call the base class getdata()function
    super().getdata()
    self.height=float(input("enter height(in cm):"))
    self.weight=float(input("enter weight(in kg):"))
#function to display the physical information
def display(self):
#call the base class display()function
    super().display()
    print("\nphysical fitness information:")
    print(f"height:{self.height}cm")
    print(f"weight:{self.weight}kg")
#driver code
if __name__=="__main__":
                        #create an object of the derived class
    student=physical_fit()
                        #get all data using the object of the derived class
    student.getdata()
                        #display all information using the object of the derived class
    student.display()
                        



                