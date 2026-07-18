class REPORT:
    #constructor to initialize the private members
    def __init__(self):
        self.__admno=0#admission number
        self.__name="" #name of the student
        self.__marks=[]#list to store marks of 5 subjects
        self.__average=0.0#average of marks
    #private method to compute the average
    def __GETAVG(self):
        self.__average=sum(self.__marks)/len(self.__marks)
    #public method to accept information
    def DISPLAYINFO(self):
        print("\n---report information---")
        print(f"admission number:{self.__admno}")
        print(f"name:{self.__name}")
        print(f"marks:{self.__marks}")
        print(f"average marks:{self.__average:.2f}")
        #drive code to demonstrate the functionality
if __name__=="__main__":
    #create an object of REPORT class
    report=REPORT()
    #read information using READINFO()
    report.READINFO()
    #display the information using DISPLAYINFO()
    report.DISPLAYINFO()
        

