#Python Program to Check if a Number is Positive, Negative or Zero
class Number:
    run= True
    while run:
        print('\n\t\t@@@Welcome In Number World@@@')
        try:
            num = int(input('Enter the number to check it is positive or negative:= '))
            if num!=0 and num>0:
                print('#Given number is positive#')
                print('\t\t\tThank you! Visit Again!')
                run = False
            elif num!=0 and num<0:
                print('#Given number is negative#')
                print('\t\t\tThank you! Visit Again!')
                run = False
            else:
                print('Given number will be equal to zero')
                run = False
        except:
            print('\t\t Attention: Enter only integer number')

if __name__ == "__main__":
   object1 = Number()
