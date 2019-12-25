#Python Program to Check Leap Year
class LeapYear:
    run= True
    while run:
        print('\n\t\t@@@Welcome In Number World@@@')
        try:
            year = int(input('Enter the year to check given year is leap year or not:= '))
            if year%4==0 or year%400==0:
                print('Given year is leap year')
            elif year%100!=0:
                print('Given year is not a leap year')
            else:
                print('Given year is not a leap year')
        except:
            print('Please type only integer value')
if __name__ == "__main__":
    object = LeapYear()
