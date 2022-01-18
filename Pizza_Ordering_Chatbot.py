print("Hello, my name is Alex your virtual assistent. I will help you order a pizza!")
print("I need to ask you a few questions, after typing your answer, press enter.")
print("\n")
userName = input("\nEnter  your name:  ")
print("\n")
print("\nHello, " + userName + " . Nice to meet you!")
size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of your pizza:  ")
crustType = input("\nWhat kind of crust do you want:  ")
quantity = input("\nHow many of these do you want to order, use only numeric values:  ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery:  ")
salesTax = 1.1
pizzaCost = 14.99
total = (pizzaCost * quantity) * salesTax
print("\n--------------------------")
print("Thank you", userName, "for your order.")
print("Your", quantity, size, flavor, "pizza with", crustType, "crust costs", "${:,.2f}".format(total) + "." )
print("----------------------------")