class PrimeNumber:
    def checkPrimeNumber(self):
        run=True
        while run:
            try:
                lower=int(input('enter the lower limit'))
                upper=int(input('enter the upper limit'))
                for num in range(lower,upper+1):
                    if(num > 1):
                        for i in range(2,num):
                            if(num%i)==0:
                                break
                        else:
                            print(num)
                            run=False
            except:
                print('plz enter integer value')
            
if __name__ == "__main__":
    PrimeNumberObj=PrimeNumber()
    PrimeNumberObj.checkPrimeNumber()
