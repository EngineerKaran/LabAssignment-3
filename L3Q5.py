print("\nWelcome to the Program")
h_atom = int(input("Enter Number of Hydrogen atoms : "))
c_atom = int(input("Enter Number of Carbon atoms : "))
o_atom = int(input("Enter Number of Oxygen atoms : "))
total_atom = int((h_atom*1.00794)+(c_atom*12.0107)+(o_atom*15.9994))
print("\nThe total molecular weight in grams per Mole (g/mol) is = ",total_atom)