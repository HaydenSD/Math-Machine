#!/usr/bin/python3

#THIS IS A WORK IN PROGRESS! IT WILL NOT WORK!


ask1 = input("What math question do you want answered? Vaild answers can be found in math.txt. ")

if ask1 == "1" or ask1 == "one":
    ask2 = input("Please enter your equation: ")
    if "+" in ask2:
        data1, data2, data3, data4, data5 = ask2.split(" ", 5)
        conversion1 = int(float(data5))
        conversion2 = int(float(data1))
        answer = (conversion1 - conversion2)
        print ("Your answer is: " + str(answer))
    elif "-" in ask2:
        data1, data2, data3, data4, data5 = ask2.split(" ", 5)
        conversion1 = int(float(data5))
        conversion2 = int(float(data1))
        answer = (conversion2 - conversion1)
        print ("Your answer is: " + str(answer))



#data1, data2, data3 = ask2.split(" ", 3)
#data4, data5 = data1.split("x", 2)
#conversion1 = int(float(data4))
#conversion2 = int(float(data3))
#answer = (conversion2 / conversion1)
#print (answer)
