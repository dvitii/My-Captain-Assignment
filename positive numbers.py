list1 = []
elements = int(input("enter the number elements: "))

for i in range(elements):
    list1.append(int(input("Enter the elements ")))

print("the input list is ", list1)

print("output: ", end = " ")
for i in range(elements):
    if list1[i] > 0:
        print(list1[i], end = " ")