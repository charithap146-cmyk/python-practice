#defining the city_pin dictionary
city_pin={'tirupati':517101,'hyderabad':500002,'chittoor':517001,'nellore':524001}
#sort the dictionary by city name(keys)
sorted_by_city=dict(sorted(city_pin.items(),key=lambda item:item[0]))
print("sorted by city name:",sorted_by_city)
#sort the dictionary by pincode(values)
sorted_by_pincode=dict(sorted(city_pin.items(),key=lambda item:item[1]))
print("sorted by pincode:",sorted_by_pincode)



