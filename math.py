#!/usr/bin/python3

#THIS IS A WORK IN PROGRESS! IT WILL NOT WORK!


ask1 = input("What math question do you want answered? Vaild answers can be found in math.txt.")

if ask1 == "1":
    ask2 = input("Please enter your equation.")
    data1, data2, data3 = ask2.split(" ", 3)
    data4, data5 = data1.split("x", 2)
    conversion1 = int(float(data4))
    conversion2 = int(float(data3))
    answer = (conversion2 / conversion1)
    print (answer)
