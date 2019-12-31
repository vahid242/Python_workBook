import time
import os
import pandas
while True:
    if os.path.exists("data.csv"):
        data = pandas.read_csv("data.csv")
        print(data.mean())
        #  print(data.mean()["st1"])
        # print(data)
    else:
        print("file dose not exit.")
    time.sleep(10)