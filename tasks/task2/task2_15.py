from random import  randint as r

for x in range(1,11):
    num1 = r(1, 10)
    num2 = r(1, 10)


    print("Question :",x,")",num1 ,"X",num2)
    solution =int(input("Enter Solution: "))

    if(solution == num1 * num2):
      print("  Right!!")

    else:
       print( "Your Answer is Wrong anwer is ",num1 * num2)