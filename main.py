import subprocess
import os

# found out a cool way to rerun the code if there is an error

while True:
  try:
    print("\n")
    # List all Python files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.py')]
    print(
        "Python files in current directory ( main.py is the current file ):" +
        "\n")
    for i, file in enumerate(files):
      print(f"{i+1}. {file}")

    print("")

    # Ask the user which file to run
    print("To use input, click on the console screen.")
    print("IMPORTANT: IF YOU WANT TO VIEW THE CODE, CLICK THE \"SHOW CODE\" ICON AT THE TOP RIGHT OF THE CONSOLE SCREEN")
    print("\n")
    file_number = int(
        input("Enter the number of the file you want to run : ")) - 1
    file_to_run = files[file_number]

    print("\n")
    print("--")
    print("\n")

    # Run the selected file
    subprocess.call(['python', file_to_run])

    # If no error occurs, break out of the loop
    break

  except Exception as e:
    print("")
    print(f"An error occurred: {e}")
    print("Restarting the program...\n")
    print("---------------------------")
