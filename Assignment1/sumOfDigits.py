num = int(input("Enter a number:"))

sum = 0
while(num>0):
    lastdigit = num % 10
    sum+=lastdigit
    num = num//10

print(int(sum))