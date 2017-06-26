filename = 'files/inputfile.txt'
for line in open(filename):
    print(line)
for line in open(filename):
    line = line.rstrip()
    print(line)
print()
for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

f = open('files/output.txt', 'w')
f.write('Python \n')
f.close()
print()
F = open("files/input.txt", "w")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("input.txt"):
    lines.append(line.strip())
print(lines)