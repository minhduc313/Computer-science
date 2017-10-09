print("Catlinh = 1")
print    ("Lathanh = 2")
print   ("Thaiha = 3")
print   ("Lang = 4")
print  ("Thuongdinh = 5")
print   ("Vanhdai3 = 6")
print   ("Phungkhoang = 7")
print   ("Vanquan = 8")
print  ("Hadong = 9")
print  ("Lakhe = 10")
print  ("Vankhe = 11")
print  ("Yennghia = 12")
rates = 2000
total = 0
for n in range (0,1000000):
    price = 0
    Depart = int(input("Input your departing station code:"))
    Destination = int(input("Input your destination station code:"))
    if Destination == 1173:
        print ("Revenue=",total, "VND")
        break
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










