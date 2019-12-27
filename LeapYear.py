#Python Program to Check Leap Year
class LeapYear:
    def checkLeapYear(self):
        run= True
        while run:
            print('\n\t\t@@@Welcome In Year World@@@')
            try:
                year = int(input('Enter the year to check if given year is leap year or not:= '))
                if year%4==0 or year%400==0:
                    print('This year is leap year')
                elif year%100!=0:
                    print('This year is not a leap year')
                else:
                    print('This year is not a leap year')
            except:
                print('Please type only integer value')
if __name__ == "__main__":
    LeapYearObject = LeapYear()
    LeapYearObject.checkLeapYear()
