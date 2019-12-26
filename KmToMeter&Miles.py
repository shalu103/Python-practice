#5.Python program to convert kilometers to meter and miles
class KilometerToMeterAndMiles:
    def meterAndMilesConverter():
        run=True
        while run:
            try:
                km = eval(input('enter no in kilometer'))
                meter = km*1000
                miles = km*0.62135
                print('given kilometer value in meters = ', meter)
                print('given kilometer value in miles= ', miles)
                run=False
            except:
                print('plz enter value of kilometer accordingly')
if __name__ == "__main__":
    KilometerToMeterAndMilesObj = KilometerToMeterAndMiles()
    KilometerToMeterAndMilesObj.meterAndMilesConverter()
