from colorama import Fore, Back, Style

print(Back.WHITE + Fore.BLACK+ "Welcome to the Paint Calculator!")
print(Style.RESET_ALL)

length = float(input(Fore.BLUE + "Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
height = float(input("Enter the height of the room in feet: "))
doors = int(input("Enter the number of doors: "))
windows = int(input("Enter the number of windows: "))
print(Style.RESET_ALL)

door_area = doors * 20
window_area = windows * 15

total_area = (2 * length * height) + (2 * width * height) - (door_area + window_area)
paint_needed = total_area / 350
gallons_needed = round(paint_needed, 2)

print(Fore.WHITE + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(Style.RESET_ALL)
print("Total surface area to paint: {} square feet".format(total_area))
print("Number of gallons of paint needed: {} gallons".format(gallons_needed))
print(Style.RESET_ALL)
print(Fore.WHITE + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
print(Style.RESET_ALL)

