import random as rand
sum=0.00
for i in range(1000):
    randomNumber=rand.randint(1,1000)
    print("Random number=",randomNumber)
    sum=sum+randomNumber
    print("sum=",sum)
print("final sum",sum)
print("Average = ", sum)

