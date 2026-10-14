with open("Python_Assignment1/myfile.txt", "r") as f:
    line = f.readlines()

print("Total number of lines:", len(line))
print("Second line:", line[1], end="")
print("Fourth line:", line[3], end="")

