#Python Program to Check if a Number is Positive, Negative or Zero
class NumberType:
    def checkTypeOfNumber(self):
        run= True
        while run:
            print('\n\t\t@@@Welcome In Number World@@@')
            try:
                num = eval(input('Enter the number to check if it is positive or negative:= '))
                if num>0:
                    print('#Given number is positive#')
                    print('\t\t\tThank you! Visit Again!')
                    run = False
                elif num<0:
                    print('#Given number is negative#')
                    print('\t\t\tThank you! Visit Again!')
                    run = False
                else:
                    print('#Given number is equal to zero#')
                    run = False
            except:
                print('\t\t Attention: Enter only integer number')

if __name__ == "__main__":
   NumberTypeObj = NumberType()
   NumberTypeObj.checkTypeOfNumber()

