myFile = open("fruit.txt")
content = print(myFile.read())
myFile.close()
print(content)

# read the bear.txt file, and print out the first 90 charactor of its content
# file = open("bear.txt")
# content = file.read()
# file.close()
# print(content[:90])

""" function get a single string and a file as parametrs and return 
 the number of occurrence of that string in the file """
#  def foo(character, filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(character)