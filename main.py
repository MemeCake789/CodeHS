from colorama import Fore, Back, Style
import subprocess
import os

# found out a cool way to rerun the code if there is an error

while True:
  try:
    print("\n")
    # List all Python files in the current directory (excluding main.py)
    files = [f for f in os.listdir('.') if f.endswith('.py') and f != 'main.py']
    print(Back.WHITE+Fore.BLACK+
        " Python files in current directory: ")
    print(Style.RESET_ALL+"\n")
    for i, file in enumerate(files):
      print(Fore.BLUE+f"{i+1}. {file}")

    print(Style.RESET_ALL + "")

    # Ask the user which file to run
    print("To use input, click on the console screen.")
    print("")
    print(Fore.RED+"IMPORTANT: IF YOU WANT TO VIEW THE CODE, CLICK THE \"SHOW CODE\" " \
      "ICON AT THE TOP RIGHT OF THE CONSOLE SCREEN (YOU WILL HAVE TO " \
      "RERUN THE CODE TO VIEW THE PROGRAM AGAIN)")

    print("")
    file_number = int(
        input(Fore.WHITE+"Enter the number of the file you want to run : ")) - 1
    file_to_run = files[file_number]

    print("\n")
    print("--")
    print(Style.RESET_ALL+"\n")

    # Run the selected file
    subprocess.call(['python', file_to_run])

    # If no error occurs, break out of the loop
    break

  except Exception as e:
    print("")
    print(f"An error occurred: {e}")
    print("Restarting the program...\n")
    print("---------------------------")