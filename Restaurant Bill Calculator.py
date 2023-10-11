from colorama import Fore, Back, Style

print(Fore.BLACK + Back.LIGHTWHITE_EX+ " Welcome to the Restaurant Bill Calculator ")
print(Style.RESET_ALL + "\n")
bill_total = float(input(Fore.LIGHTCYAN_EX + "What is the total amount on the bill? "))
tip_percentage = float(input("What % tip would you like to give? "))
people_count = int(input("How many people are sharing the bill? "))

tip_amount = bill_total * (tip_percentage / 100)
total_bill = bill_total + tip_amount
amount_per_person = total_bill / people_count

print(Style.RESET_ALL + "\n")
print(Back.WHITE + Fore.BLACK + "----------------------------------")
print("\n")
print("Tip amount: " + str(tip_amount))
print("Total bill: " + str(total_bill))
print("Total amount per person: " + str(amount_per_person))
print("\n")
print(Back.WHITE + Fore.BLACK + "----------------------------------")
print(Style.RESET_ALL)