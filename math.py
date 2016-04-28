#!/usr/bin/env python3

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
    elif "/" in ask2:
        data1, data2, data3 = ask2.split(" ", 3)
        data4, data5 = data1.split("x", 2)
        data6, data7 = data5.split("/", 2)
        conversion1 = int(float(data3))
        conversion2 = int(float(data7))
        answer = (conversion1 * conversion2)
        print ("Your answer is: " + str(answer))
    elif "*" in ask2:
        data1, data2, data3, data4, data5 = ask2.split(" ", 4)
        data6 = data1.split("x", 2)
        conversion1 = int(float(data1))
        conversion2 = int(float(data5))
        answer = (conversion2 / conversion1)
        print ("Your answer is: " + str(answer))
    else:
        print ("This equation is not valid. Please check math.txt.")
elif ask1 == "cir":
    ask2 = input("What problem do you want solved? Vaild answers can be found in math.txt. ")
    if ask2 == "cc":
        ask3 = input("What is your radius? ")
        conversion1 = int(float(ask3))
        answer = (2 * 3.14 * conversion1)
        print ("Your answer is: " + str(answer))
    if ask2 == "a":
        ask3 = input("What is your radius? ")
        conversion1 = int(float(ask3))
        answer = (3.14 * conversion1**2)
        print("Your answer is: " + str(answer))
    if ask2 == "d":
        ask3 = input("What is your radius? ")
        conversion1 = int(float(ask3))
        answer = (conversion1 * 2)
        print ("Your answer is: " + str(answer))
elif ask1 == "ba":
    ask2 = input("Please enter your addition problem: ")
    data1, data2, data3 = ask2.split(" ", 3)
    conversion1 = int(float(data1))
    conversion2 = int(float(data3))
    answer = (conversion1 + conversion2)
    print ("Your answer is: " + str(answer))
elif ask1 == "bs":
    ask2 = input("Please enter your subtraction problem: ")
    data1, data2, data3 = ask2.split(" ", 3)
    conversion1 = int(float(data1))
    conversion2 = int(float(data3))
    answer = (conversion1 - conversion2)
    print ("Your answer is: " + str(answer))
elif ask1 == "bm":
    ask2 = input("Please enter your multiplication problem: ")
    data1, data2, data3 = ask2.split(" ", 3)
    conversion1 = int(float(data1))
    conversion2 = int(float(data3))
    answer = (conversion1 * conversion2)
    print ("Your answer is: " + str(answer))
elif ask1 == "bd":
    ask2 = input("Please enter your division problem:")
    data1, data2, data3 = ask2.split(" ", 3)
    conversion1 = int(float(data1))
    conversion2 = int(float(data3))
    answer = (conversion1 / conversion2)
    print ("Your answer is: " + str(answer))
