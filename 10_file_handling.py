print("Het_Kothari_60004230270")
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Writing to files in Python is easy!")


# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content (Read): ")
    print(content)


# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nAppending additional content to the file")


# Reading and Writing to a file
with open("example.txt", "w+") as file:
    file.write("\nNew content written in w+ mode")
    file.seek(0)  # Move the file cursor to the beginning
    updated_content = file.read()
    print("\nFile Content (Read and Write): ")
    print(updated_content)


# Handling Exceptions
try:
    with open("non-existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"\nFile not found: {e}")
    
