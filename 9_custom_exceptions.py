print("Het_Kothari_60004230270")

try:
    # Example 1: ZeroDivisionError
    result = 10/0

except ZeroDivisionError as zd_error:
    print(f"ZeroDivisionError: {zd_error}")


try:
    # Example 2: ValueError
    num = int("abc")

except ValueError as val_error:
    print(f"ValueError: {val_error}")


try:
    # Example 3: IndexError
    my_list = [1,2,3]
    value = my_list[5]

except IndexError as index_error:
    print(f"IndexError: {index_error}")


try:
    # Example 4: FileNotFoundError
    with open("non-existent_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError as file_error:
    print(f"FileNotFoundError: {file_error}")


try:
    # Example 5: TypeError
    result = "10" + 5

except TypeError as type_error:
    print(f"TypeError: {type_error}")


try:
    # Example 6: Custom Exception
    raise ValueError("This is a custom exception")

except ValueError as custom_error:
    print(f"Custom Exception: {custom_error}")

finally:
    print("Finally block always executes")
    
