print("Het_Kothari_60004230270")

input_list = list(map(int, input("Enter a list of numbers seperated by space: ").split()))
result = list(map(lambda x: x**3, filter(lambda x: x%2 != 0, input_list)))
print("Cubes of odd numbers from the input list: ", result)
