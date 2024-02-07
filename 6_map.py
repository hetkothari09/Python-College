print("Het_Kothari_60004230270")
list1 = list(map(int, input("Enter the first list of numbers seperated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers seperated by space: ").split()))

result = list(map(lambda x, y: x+y, list1, list2))
print("Element wise addition of two lists: ", result)
