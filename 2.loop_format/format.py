name = input("Enter a name: ")
surname = input("Enter surname: ")
when = "today"
# message = "Hello %s" % name
# message = "Hello %s %s" % (name, surname.capitalize())
# message = f"Hello {name} {surname.title()}. What's up {when}"
message = "Hi {} {} . what's up {}".format (name, surname.title(), when)
print(message)