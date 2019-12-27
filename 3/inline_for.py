# temps=[224, 230, 340, 221]
# new_temps = [temp/10 for temp in temps]
# print(new_temps)

# def convert(lst):
#   new_temps = [temp for temp in lst if not isinstance(temp, str)]  
#   return new_temps
# temps=[224, 230, "no data", 340, "no data", 221]
# print(convert(temps))


temps=[224, 230, -999, 221]
new_temps = [temp/10 if temp !=-999 else 0 for temp in temps]
print(new_temps)