# Python program to display calendar
class calendar:
    def showCalendar(self): 
        run = True
        print('\t\t****Welcome In Magic world****')
        while run:
            try:
                import calendar
                year = int(input('enter the year: '))
                month = int(input('enter the month'))
                if (month<=12):
                    print(calendar.month(year,month))
                    run = False
                    print('GoodBye!!')
                else:
                    print('Enter month value in range')
            except:
                print('Enter only Integer')
if __name__ == "__main__":
  calendarobj = calendar()
  calendarobj.showCalendar()
