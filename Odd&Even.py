#Python Program to Check if a Number is Odd or Even
class OddEven:
    run = True
    while run:
        try:
            num = int(input('Enter num to check given num is odd or even : '))
            if num%2==0:
                print('Given Number is Even number')
            else:
                print('Given Number is Odd number')
                run = False
                print('\t\t****Thanks for running this program***')
        except:
            print('\t\t **Enter only integer Number**')
if __name__ == "__main__":
    obj = OddEven()
