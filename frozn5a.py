#initial list of cities
cities=["tirupati","kurnool","kadapa"]
#display initial list
print("initial list of cities:")
print(cities)
print()
#1.add 3 more cities
cities.append("chittoor")
cities.append("nellore")
cities.append("guntur")
print("after adding chittor,nelloore,and guntur:")
print(cities)
print()
#2.insert hyderabad at 3rd position(index2)
cities.insert(2,"hyderabad")
print("after inserting hyderabad at 3rd position:")
print(cities)
print()
#3.Delete any two city names(e.g.,delete kadapa and nellore)
cities.remove("kadapa")
cities.remove("nellore")
print("after deleting kadapa and nellore")
print(cities)
print()
#4.update all city names to uppercase
cities=[city.upper()for city in cities]
print("after updating all city names to uppercase:")
print(cities)





