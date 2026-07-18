#define a custom exception called negative
class negative(exception):
    def__init__(self,message):
    self.message=message
    super().__init__(self.message)
    #function to collect marks for 10 students
    def collect_marks():
        python_mark=[] #list to store valid marks
        for i in range(10):
            try:
                #collect mark from the user 
                mark=float(input(f"enter the mark for student{i+1}:"))
                #check if the entered mark is negative
                if mark<0:
                    raise negative("error:negative marks are not allowed!")
                #if mark is valid,store it in the list
                python_mark.append(mark)
            except negative as e:
                print(e)#display the custom exception message
            except ValueError:
                print("error:please enter a valid number for the marks.")
                return python_mark
            #drive code 
            if__name__=="__main__":
            #call the collect_marks function to collect marks
            marks_list=collect_marks()
            #display the valid marks collected
            print("\nvalid marks collected:")
            print(marks_list)
