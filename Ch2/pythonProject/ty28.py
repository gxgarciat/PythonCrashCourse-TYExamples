# Assign the value "python_notes.txt" to a variable called filename. Then use removesuffix() method
# to display the filename without the file extension.

filename = input("Enter file name: ")
print(f"The file name without the file extension is: {filename.removesuffix('.txt')}")
print("Thank you for using this program..")