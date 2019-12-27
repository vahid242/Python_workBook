# ask question
# repeat
# show sentence capitalize and end .?
total=[]
def convert(sen):
    interrogative = ("how", "why","what","who", "is", "are","am","do","dose")
    capitalized = sen.capitalize()
    if sen.startswith(interrogative):
       message =  "{}?".format(capitalized)
    else:
        message = "{}.".format(capitalized)
    total.append(message)
while True:
    answer = input("Say Something: ")
    if answer !="end":
        convert(answer)
    else:
        break
        
print(" ".join(total))
# for line in total:
#     print(line)