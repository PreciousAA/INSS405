def request():
    num1 = input('Enter Variable num1')
    num2 = input('Enter Variable num2')
    num3 = input('Enter Variable num3')
    print(sum(num1,num2,num3))
    print(Avg(num1,num2,num3))
    print(maximum(num1,num2,num3))
    print(Minimum(num1,num2,num3))
    print(product(num1,num2,num3))
def sum (num1,num2,num3):
    sum=int(num1)+int(num2)+int(num3)
    return sum
def Avg(num1,num2,num3):
    sum = int(num1)+int(num2)+int(num3)
    mean=int(sum)/3
    return mean
def maximum(num1,num2,num3):
    print(max(num1,num2,num3))
def Minimum(num1,num2,num3):
    print(min(num1,num2,num3))
def product(num1,num2,num3):
    product=int(num1)*int(num2)*int(num3)
    return product
request()