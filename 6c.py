import re
#the input string
wel_str="welcome to AI ML DS"
#searching for the pattern"AI"in the string using regular expression
match=re.search(r"AI",wel_str)
#check if a match is found
if match:
    #start location of the pattern
    start_location=match.start()
    print("pattern start location:",start_location)
    #end location of the pattern
    end_location=match.end()
    print("pattern end location:",end_location)
    #span of the pattern
    span_location=match.span()
    print("pattern span location:",span_location)
else:
    print("pattern'AI not found in the string.")
    