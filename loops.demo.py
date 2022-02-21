import random

sayi = random.randint(1,100)

try = int(input("How many try do you want?: "))
hak = try
sayac = 0

while (hak>0):
    hak -= 1
    sayac += 1
    tahmin = int(input("Prediction:"))

    if (sayi == tahmin):
        print(f"Congruculations. Your Grade: {(100 - (100/try) * (sayac - 1))}")
        break
    elif (sayi>tahmin):
        print("More")
    else:
        print("Less")
    if (hak == 0):
        print(f"Your turn is over. the predicted number: {sayi} ")
     
