
def request():
    number = input('Enter Variable number')
    print(even(number))


def even(number):
    if(int(number)%2==0):
        return 'Even number'
    else:
        return 'Odd number'

request()