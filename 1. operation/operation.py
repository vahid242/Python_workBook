# dir(list)
temp=[5,8,6]
print(temp)
temp.append(7)
print(temp)
temp.clear()
print(temp)
temp=[5,8,6]
print(temp)
print(temp.index(8))
temp=[5,8,6,4,3,8]
print(temp.index(8,2))
temp.remove(4)
print(temp.__getitem__(1))
print(temp[1])
print(temp[1:4])
print(temp[:4])
print(temp[2:])
print(temp[-1])
print(temp[-5])
name=["vahid", "tom", "gerry"]
print(name[0][3])
name_grade={"vahid":9, "tom":6, "gerry":7}
print(name_grade["vahid"])
