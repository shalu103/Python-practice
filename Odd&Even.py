#Python Program to Check if a Number is Odd or Even
class OddEven:
    def checkOddEven(self):
        run = True
        while run:
            try:
                num = eval(input('Enter num to check given num is odd or even : '))
                if num%2==0:
                    print('Given Number is Even number')
                else:
                    print('Given Number is Odd number')
                    run = False
                    print('\t\t****Thanks for running this program***')
            except:
                print('\t\t @@@Attention : Enter only Number@@@')
if __name__ == "__main__":
    OddEvenobj = OddEven()
    OddEvenobj.checkOddEven()
