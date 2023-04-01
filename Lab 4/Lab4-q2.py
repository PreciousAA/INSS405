temperature=input('Enter Temperature:')
for i in range (2):
    if (int(temperature)>=50):
        print('Hot')
    if(int(temperature)>=30 and int(temperature)<50):
        print('Warm')
    if(int(temperature)>=0 and int(temperature)<=30):
        print('Cold')
    else:
        print('Extreme cold')



