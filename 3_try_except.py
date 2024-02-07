print("Het_Kothari_60004230270")

def perfect(n):
    if n<=1:
        return False


    factors_sum = 1

    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            factors_sum += i
            if i!=n//i:
                factors_sum+=n//i

    return factors_sum==n


try:
    num=int(input("Enter a positive integer: "))
    if num>0:
        result=perfect(num)
        if result:
            print(f"{num} is a perfect number")
        else:
            print(f"{num} is not a perfect number")

    else:
        print("Please enter a positive number")

except ValueError:
    print("Invalid input. Please enter a positive integer")
    
