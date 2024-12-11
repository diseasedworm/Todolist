value = float(input("Enter the price"))
price = float(value * 100)

amountgiv = float(input("Enter amount given"))
amount = float(amountgiv * 100)

change = (int(amount - price))

dollars = change // 100
change = change % 100
halfdollar = change // 50
change = change % 50
quarters = change // 25
change = change % 25
dime = change // 10
change = change % 10
nickel = change // 5
change = change % 5
penny = change


if dollars == 1:
    print("you have " +  str(dollars) + " dollar and " + str(halfdollar) + " half dollars and " + str(dime) + " dimes and " + str(nickel) + " nickels and " + str(quarters) + " quarters and " + str(penny) + " pennies")
else:
    print("you have " +  str(dollars) + " dollars and " + str(halfdollar) + " half dollars and " + str(dime) + " dimes and " + str(nickel) + " nickels and " + str(quarters) + " quarters and " + str(penny) + " pennies")

