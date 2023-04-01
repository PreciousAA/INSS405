
score1=input('Enter score for INS405')
score2=input('Enter score for BUIS360')
score3=input('Enter score for DANL470')

sum=int(score1)+int(score2)+int(score3)
average=int(sum/3)
print(sum)
print(average)

score = input('Enter Score')
if(int(score)>=90):
    print('A')
elif(int(score)>=70 and int(score)<=79):
    print('B')
elif(int(score)>=60 and int(score)<=69):
    print('C')
else:
    print('f')


