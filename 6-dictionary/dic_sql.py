import mysql.connector

# use a variable to store that connection object
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)
cursor = con.cursor()

def translate(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
    
# store actual data in results variable
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[1])
    else:
        print ("No word found!")
word = input("Enter a word: ")
translate(word) 