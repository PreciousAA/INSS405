sum=0
for i in range (10):
    score = int(input("Enter score:"))
    if(int(score)>=90):
        print("A")
    elif(int(score)>=80):
        print('B')
    elif(int(score)>=75) and (int(score)<=79):
        print("C")
    elif(int(score)>=60):
        print("D")
    else:
        print("F")
    sum= sum+int(score)
average=int(sum/10)
print("Total sum", sum)
print("Average score", average)






