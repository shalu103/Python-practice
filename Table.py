class Table:
    def printTable__init__(startNum, endNum):
        for i in range(1,11):
            for j in range(startNum,endNum+1):  
                print(i*j, end='\t')
            print('')
    def main__init__():
        run = True
        while run:
            print('\n\n\t\t*******Welcome in TABLE world*******\n')
            print('\t\t1.Input the range for print the tables, the both input values are inclusive\n')
            try:
                startNum = int(input('Enter start table number: '))
                endNum = int(input('Enter end table number: '))
                diff = endNum-startNum
                if(diff+1 <= 10):
                    printTable(startNum, endNum)
                    print('\t\t\tThank you! Visit Again!')
                    run = False
                else:
                    print('\t\t@CAUTION: At a time only ten tabels can print on the screen, so please enter range accordingly.\n\n')
            except:
                print('Enter only integer number in input.')

if __name__ == "__main__":
    obj = Table()
    obj.main()
    obj.printable(2,5)
