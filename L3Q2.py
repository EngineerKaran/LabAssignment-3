print("\nWelcome to the Calculator")
print("\n\nThe calculator has following functions :")
print("FUNCTION MENU")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Integer Division")
print("5 Float Division")
print("\n")
n1 = int(input("Enter the first argument : "))
n2 = int(input("Enter the second argument : "))
fin_ans = None
c = str(input("Enter the serial number of the function to be performed : "))
while c >= "6" :
    print("\nKindly choose from the options listed in the FUNCTIONS MENU only!!")
    break
while c <= "5" :
    if c == "1" :
        fin_ans = int(n1 + n2)
        print("\nAnswer = ",fin_ans)
    if c == "2" :
        fin_ans = int(n1 - n2)
        print("\nAnswer = ", fin_ans)
    if c == "3" :
        fin_ans = int(n1 * n2)
        print("\nAnswer = ", fin_ans)
    if c == "4" :
        fin_ans = int(n1//n2)
        print("\nAnswer = ", fin_ans)
    if c == "5" :
        fin_ans = float(n1/n2)
        print("\nAnswer = ", fin_ans)
    break
print("\nThanks for using the Calculator")