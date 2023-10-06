import os
import subprocess

# so the main code just makes a list with all the .py files and allows you to run the file

# List all Python files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.py')]
print("Python files in current directory:")
for i, file in enumerate(files):
    print(f"{i+1}. {file}")

# Ask the user which file to run
file_number = int(input("Enter the number of the file you want to run: ")) - 1
file_to_run = files[file_number]

# Run the selected file
subprocess.call(['python', file_to_run])
