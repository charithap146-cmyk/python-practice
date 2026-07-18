#function to calculate learner's age in days with positional and keyword arguments
def learner_age_days(name,age):
    age_in_days=age*365
    print(f"learner's name:{name}")
    print(f"learner's age in days:{age_in_days}")
    #driver code using positional arguments
    print("using positional arguments:")
    learner_age_days("john",25)
    #drive code using keyword arguments
    print("\n using keyword arguments:")
    learner_age_days(name="alice",age=30)
    #function with default arguments
    def learner_age_days(name="unknown",age=18):
        age_in_days=age*365
        print(f"learner's name:{name}")
        print(f"learner's age in days:{age_in_days}")
        #drive code using default arguments
        print("\n using default arguments:")
        learner_age_days()#no arguments passed,default values will be used
        #drives code using custom arguments(overriding default)
        print("\n using custom arguments:")
        learner_age_days("david",22)#custom values for name and age)
    