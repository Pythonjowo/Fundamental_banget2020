tamu = "Pria"
baik = True
rajin = True

if baik & rajin:
    if tamu == "Pria":
        print('Kita Nikah Yuk')
    else:
        print("Kita jAdi Saudara")
else:
    print("Hush! Pergi sana !")


## IF ELif Becabang

if baik & rajin & (tamu == "Pria"):
    print('Kita Nikah Yuk!')
elif baik & rajin & (tamu == "Cewe"):
    print('Kita Jadi Saudara')
else:
    print("Hush !, Pergi Sana !")
