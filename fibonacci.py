r = int(input("Please enter the number of terms: "))
a = 0
b = 1
c = a + b
if r <= 0:
  print("Please enter a positive number")

elif r == 1:
    print(a)

else:
    print(a)
    print(b)
    for i in range(3, r + 1):
        c = a + b
        print(c)
        a = b
        b = c
        i = i + 1