print("
        catlinh = 1
        lathanh = 2
        thaiha = 3
        Lang = 4
        thuongdinh = 5
        vanhdai3 = 6
        phungkhoang = 7
        vanquan = 8
        hadong = 9
        lakhe = 10
        vankhe = 11
        yennghia = 12")
rates = 2000
total = 0
for n in range (0,1000000):
    price = 0
    Depart = int(input("Input your departing station code:"))
    Destination = int(input("Input your destination station code:"))
    if Destination == 1173:
        print ("Revenue=",total, "VND")
        break
        time.sleep(10)
    else:
        price = abs(rates*(Destination-Depart))
        print ("Price=", price,"VND")
        pay = int(input("Please insert money:"))
        while pay >= price:
            print (Destination)
            print (Depart)
            #I want to output the station name, but can't#
            print (pay)
            total = total + pay
            break
        if pay < price:
            missing = price-pay
            print ("Missing",missing,"VND")










