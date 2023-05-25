import random
# Generate 100 random integers between 1 and 500
arr = [random.randint(1,500)
       for i in range(100)]
# Print out only the odd values
print("Odd values:")
for num in arr:
    if num % 2 == 0:
        print(num)


