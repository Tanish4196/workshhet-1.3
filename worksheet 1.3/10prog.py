def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Divisible by both 3 and 5"
    else:
        return "Not divisible by both 3 and 5"


num = int(input("Enter a number: "))

result = check_divisibility(num)
print(result)
