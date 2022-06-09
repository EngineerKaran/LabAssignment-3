print("\nWelcome to the Program")
num = int(input("Kindly enter a number : "))
num1 = num
num_exp = 0
rem = 0
num_bi = 0
while (num1>0):
    rem= num1%2
    num_bi = (int)(num_bi + (rem*10**num_exp))
    num1 = num1//2
    num_exp+=1
print("The number in binary form of ",num," = ",num_bi)
#The binary number is of 8 numbers, so add 0 infront of the result if the result contains less than 8 numbers