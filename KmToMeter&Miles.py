#5.Python program to convert kilometers to miles
class Kilometertomiles:
    run=True
    while run:
        try:
            km= int(input('enter no in killometer'))
            meter = km*1000
            miles = km*0.62135
            print('given killometer value in meters = ',meter)
            print('given killometer value in miles= ',miles)
            run=False
        except:
            print('plz enter value of killometer accordingly')
if __name__ == "__main__":
    obj= Kilometertomiles()
