# def motto():
#     print("Get up, stand up, Don't give up the right")
# motto()

# def ilk_fonksiyonumuz(a, b):
#     print((a ** 2) + (b ** 2))
# ilk_fonksiyonumuz(int(input("bir sayi giriniz: ")), int(input("bir sayi daha giriniz: ")))

# def multiply(a, b):
#     print(a * b)
# multiply(3, 5)
# multiply(-1, 2.5)
# multiply("amazing", 3)

# def add(a, b):
#     print(a + b)
# add(int(input("Bir sayı giriniz : ")), int(input("Bir sayı daha giriniz : ")))

# def calculator(x, y, z):
    
#     if (z == "+"):
#         print(x + y)
#     elif (z == "-"):
#         print(x - y)
#     elif (z == "*"):
#         print(x * y)
#     elif (z == "/"):
#         print(x / y)
#     else:
#         print("Yapilacak işlemi >> + - * / şeklinde giriniz")
# calculator(int(input("ilk sayiyi giriniz: ")), int(input("ikinci sayiyi giriniz: ")), input("yapilacak işlemi giriniz: "))


# def calculator(x, y, z):
#     if z == "+":
#         print(x + y)
#     elif z == "-":
#         print(x - y)
#     elif z == "*":
#         print(x * y)
#     elif z == "/":
#         print(x / y)
#     else:
#         print("Invalid input, please input + - * /")
# calculator(int(input("Enter first number: ")), int(input("Enter second number: ")),
#            input("Which function do you want?: "))

# def multiply(a, b):
#     print(a * b, type(a * b))
# multiply(2, 3)


# def çarpma(a, b):
#     return a * b
# print(çarpma(2, 3))
# print(type(çarpma(2, 3)))
# print(type(çarpma(2, 3)))

# def A():
#     return "Nasilsin"

# def B():
#     return "iyilik senden naber"

# def C():
#     return "Neler yapıyorsun"

# def D():
#     return "valla ne olsun, aynı"

# print(A())
# print(B())
# print(C())
# print(D())

# def hesap_makinesi(a, b, c):
#     if c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/":
#         print(a / b)
#     else:
#         print("lütfen şu işlemlerden birini giriniz + - * / ")
# hesap_makinesi(int(input("Bir sayı giriniz : ")),int(input("Bir sayı giriniz : ")),
#                str(input("Lütfen yapılacak işlemi giriniz : ")))
        
        
# def calculator(a, b, c):
#     if c == "+":
#         return(a + b)
#     elif c == "-":
#         return(a - b)
#     elif c == "*":
#         return(a * b)
#     elif c == "/":
#         return(a / b)
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = input("Enter an operation: ")
# print(calculator(a, b, c))

# def ReCalculater(a,b,r):
#     if r == "+":
#        return (a + b)
#     elif r == "-":
#          return (a - b)
#     elif r == "*":
#         return (a * b)
#     elif r == "/":
#         return (a / b)
#     else:
#         return "Duzgun bir operator giriniz!"
# print(ReCalculater(int(input("Bir sayı giriniz : ")),int(input("Bir sayı giriniz : ")),
#                    str(input("Lütfen yapılacak işlemi giriniz : "))))

# def absolute_value(x):
#     if x < 0:
#         return -1 * x
#     if x > 0:
#         return x
#     else:
#         return f"{x} is not absolute value"

# print(absolute_value(0))
# print(absolute_value(-4))


# def mutlak_deger(a):
#     if a < 0:
#         return(abs(a))
#     if a >= 0:
#         return a

# print(mutlak_deger(3.3))
# print(mutlak_deger(-4))

def max_length():
    l = []
    k = []
    for i in range(int(input("karlılaştırılacak kelime sayısını giriniz : "))):
        kelime = input("lütfen bir kelime giriniz: ")
        l.append(len(kelime))
        k.append(kelime)
    return (f"{k[l.index(max(l))]} kelimesi daha uzun bir kelimedir : {max(l)}")
print(max_length())
