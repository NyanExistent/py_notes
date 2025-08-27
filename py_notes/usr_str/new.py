#TODO: Get input for calculator
num1 = int(input("please type a number: "))
op = str(input("please type a + or - or * or / : "))
num2 = int(input("please type a second number: "))

#if tree logic
if (num2 == 0 and op == '/'):
  print("ERROR: YOU CANNOT DIVIDE BY 0")
elif (op == '+'):
  ans = num1 + num2
elif (op == '-'):
  ans = num1 - num2
#elif (op = '*'):
 # ans = num1 * num2
#damn it
elif (op == '*'):
  ans = num1 * num2
elif (op == '/'):
  ans = num1 / num2
else: print("ERROR")

print(ans)
