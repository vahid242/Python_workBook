# create a new file with Python and write some text on it:

# with open("veg.txt", "w") as file:
#     file.write("tomato")

# append text to an existing file without overwriting it:

# with open("veg.txt", "a") as file:
#     file.write("\ncucumber")

# both append and read a file with:
with open("veg.txt", "a+") as file:
    file.write("\ngarlic")
    # put the crusor at rhe zero position
    file.seek(0)
    content = file.read()
    print(content)