# def average(num):
#     avg = sum(num) / len(num)
#     return avg

# print(type(average), type(sum))
# print(average([5,6,7]))
# name_grade={"vahid":9, "tom":6, "gerry":7}
# print(average(name_grade.values()))

def average(num):
    # if type(num) == dict:
    if isinstance(num, dict):
        avg = sum(num.values()) / len(num)
    else:
       avg = sum(num) / len(num) 
    return avg

name_grade={"vahid":9, "tom":6, "gerry":7}
print(average(name_grade))