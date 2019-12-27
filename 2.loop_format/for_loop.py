weather = [8.8, 9, 7]
def convert(temperatue):
    far_temp = (temperatue * 9 / 5) + 32
    return far_temp
for temp in weather:
    print(convert(temp))

phone_numbers = {"John Smith": "+37682929928",
 "Marry Simpons": "+423998200919"}
# for pair in phone_numbers.items():
#     print("{} has as phone number {}"
#     .format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has as phone number {}"
    .format(key, value))
    
for value in phone_numbers.values():
    print(value.replace("+", "00"))