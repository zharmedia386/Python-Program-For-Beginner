# Numbers To Words Converter in Indonesian

def converter(number) :
    if(number == 1) :
        print("satu ", end='')
    elif(number == 2) :
        print("dua ", end='')
    elif(number == 3) :
        print("tiga ", end='')
    elif(number == 4) :
        print("empat ", end='')
    elif(number == 5) :
        print("lima ", end='')
    elif(number == 6) :
        print("enam ", end='')
    elif(number == 7) :
        print("tujuh ", end='')
    elif(number == 8) :
        print("delapan ", end='')
    elif(number == 9) :
        print("sembilan ", end='')
    elif(number == 10) :
        print("sepuluh ", end='')
    elif(number > 10 and number  < 20) :
        number = number - 10
        converter(number)
        print("belas ", end='')
    elif(number == 20 or number == 30 or number == 40 or number == 50 
    or number == 60 or number == 70 or number == 80 or number == 90) :
        number = number / 10
        converter(number)
        print("puluh ", end='')
    elif(number > 20 and number < 100) :
        temp = int(number / 10)
        converter(temp)
        print("puluh ", end='')
        number = number % 10
        converter(number)
    elif(number == 100) :
        print("seratus ", end='')
    elif(number > 100 and number < 200) :
        print("seratus ", end='')
        number = number - 100
        converter(number)
    elif(number >= 200 and number < 1000) :
        temp = int(number / 100)
        converter(temp)
        print("ratus ", end='')
        temp = int(number % 100)
        converter(temp)
    elif(number >= 1000 and number < 2000) :
        print("seribu ", end='')
        temp = int(number % 1000)
        converter(temp)
    elif(number >= 2000 and number < 1000000) :
        temp = int(number / 1000)
        converter(temp)
        print("ribu ", end='')
        temp = int(number % 1000)
        converter(temp)
    elif(number >= 1000000 and number < 1000000000) :
        temp = int(number / 1000000)
        converter(temp)
        print("juta ", end='')
        temp = int(number % 1000000)
        converter(temp)
    elif(number == 1000000000) :
        print("satu milyar ", end='')

if __name__ == "__main__" :
    number = int(input("[Maks 1 milyar] Masukkan Angka : "))
    converter(number)