uang = input("Kamu uangnya Berapa? ")
utang = 10000
if int(uang) < utang:
    print("Wah maaf bos ngga cukup")
elif int(uang) == utang:
    print("Terima Kasih Sudah Membayar!")
else:
    print("Wah Uangnya Lebih!")