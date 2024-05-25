def sort_numbers(num1, num2, num3):
    return sorted([num1, num2, num3])


num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sorted_numbers = sort_numbers(num1, num2, num3)

print("Numbers in ascending order:", sorted_numbers)
