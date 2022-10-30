hour = int(input("Enter Hour Between 1 and 12: "))

e = int(input("Choose 1 for AM and 2 for pm"))

future_hour = int(input("Enter Hours in the future: "))

if e == 1:
    if (hour + future_hour > 12):
        print("Future Hours ", (hour + future_hour) - 12, "AM")
    else:
        print("Future Hours ", (hour + future_hour) , "AM")
else:
    if(hour + future_hour>12):
     print("Future Hours ", (hour + future_hour)-12, "pm")
    else:
     print("Future Hours ", (hour + future_hour) , "pm")