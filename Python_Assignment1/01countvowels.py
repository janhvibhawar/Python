with open("Python_Assignment1/myfile.txt", "r") as f:
    text = f.read()

count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count +=1

print("Number of vowels:", count)