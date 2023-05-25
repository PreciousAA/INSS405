numbers = []

for i in range (10):
    num= int(input("Enter a number:"))
    numbers.append(num)
def calc_sum(arr):
    return sum(arr)
def calc_mean(arr):
    return sum(arr) / len(arr)
def cal_median(arr):
    arr.sort()
    n = len (arr)
    if n % 2 == 0:
        m1 = arr[n//2]
        m2 = arr[n//2 -1]
        median = (m1 + m2)/2
    else:
        median = arr[n//2]
        return median

print("Numbers:, numbers ")
print("Sum",calc_sum(numbers))
print("Mean",calc_mean(numbers))
print("Median",cal_median(numbers))

