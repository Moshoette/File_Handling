
with open("my_file.txt", "w") as file:
    file.write("This is line 1.\n")
    file.write("12345\n")
    file.write("Another line here.\n")


with open("my_file.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)


with open("my_file.txt", "a") as file:
    file.write("Appending line 1.\n")
    file.write("67890\n")
    file.write("Appending another line here.\n")


try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("Error handling completed.")
