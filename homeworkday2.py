# problem #1 task 1 code correction
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# problem #2 The Greatest Showdown
# task 1 Identify the Greatest
print("Please enter 3 different numbers!")
first_num = input("Enter first number. ")
second_num = input("Enter second number. ")
third_num = input("Enter third number. ")
if first_num > second_num and first_num > third_num:
    print(first_num)
elif second_num > first_num and second_num > third_num:
    print(second_num)
elif third_num > first_num and third_num > second_num:
    print(third_num)
else:
    print("i dont know")

# task 2 Identify the Smallest


if first_num < second_num and first_num < third_num:
    print(first_num)
elif second_num < first_num and second_num < third_num:
    print(second_num)
elif third_num < first_num and third_num < second_num:
    print(third_num)
else:
    print("i dont know")