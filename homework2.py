from os import system
system("clear")
n = 1
while n <= 10:
    print(n)
    n += 1

start_n = int(input("Enter the start number: "))
end_n = int(input("Enter the end number: "))

if start_n <= end_n:
    n = start_n
    while n <= end_n:
        print(n)
        n += 1
else:
    n = start_n
    while n >= end_n:
        print(n)
        n -= 1