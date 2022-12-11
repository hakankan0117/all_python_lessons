
value = input("lütfen bir cümle giriniz : ")

a = ("a", "b", "c","ç", "d", "e", "f", "g","ğ", "h", "ı", "i", "j", "k", "l", "m",
     "n", "o", "ö", "q", "p", "r", "s", "ş", "t", "u", "ü", "v", "w", "y", "z")

dizi = []

for i in value :
    if not (i in dizi) and i != " "  and i in a:
        dizi.append(i)

print(dizi)

#  print()
