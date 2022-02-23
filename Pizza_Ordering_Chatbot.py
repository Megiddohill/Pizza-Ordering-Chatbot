print("Hello, my name is Alex your virtual assistent. I will help you order a pizza!")
print("I need to ask you a few questions, after typing your answer, press enter.")
print("\n")
userName = input("\nEnter  your name:  ")
while (len(userName) ==0):
    userName = input("Please enter your name:  ")
if userName.lower() == "david prato":
    print("\nMy creator, " + userName +  ". Pleasure to serve you!")
else:
    print("\nHello, " + userName + " . Nice to meet you!")
keepGoing = "y"
while keepGoing.lower() == "y":
    size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
    while size.lower() != "small" and size.lower() != "medium" and size.lower() != "large":
        size = input("\nWhat size do you want?  Enter small, medium, or large:  ")
    flavor = input("\nEnter the flavor of your pizza:  ")
    crustType = input("\nWhat kind of crust do you want:  ")
    quantity = input("\nHow many of these do you want to order, use only numeric values:  ")
    while not quantity.isdigit():
        quantity = input("\nValue not recognized. Please enter a numeric value:  ")
    quantity = int(quantity)
    method = input("\nIs this carry out or delivery:  ")
    while method.lower() != "delivery" and method.lower() != "carry out":
        method = input("\nInvalid value. Please enter delivery or carry out:  ")
    salesTax = 1.1
    if size.lower() == "small":
        pizzaCost = 8.99
    elif size.lower() == "medium":
        pizzaCost = 14.99
    elif size.lower() == "large":
         pizzaCost = 17.99
    if method.lower() == "delivery":
        deliveryFee = 5
    else:
        deliveryFee = 0
    total = (pizzaCost * quantity) * salesTax + deliveryFee
    print("\n--------------------------")
    print("Thank you", userName, "for your order.")
    print("Your", quantity, size, flavor, "pizza with", crustType, "crust costs", "${:,.2f}".format(total) + "." )
    if total >= 50:
        print("\nCongradulations, you've been awarded a $10 Off couponfor your next order!")
    else:
        print("\nOrders over $50 will receive a free $10 Off coupon!")
    print("----------------------------")
    print ("Order has been recieved. ETA 3 mins!")
    for min in range(3, 1, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end= "  \r")
            import time
            time.sleep(1)
    print("Order is ready")
    keepGoing = input("Do you wan to place another order? Enter y or n:  ")