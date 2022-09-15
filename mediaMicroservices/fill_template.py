import sys

if len(sys.argv) < 3:
    exit()
a = sys.argv[1]
b = sys.argv[2]
lines = []
outlines = []
with open("docker-template.yml","r") as f:
    lines = f.readlines()
for line in lines:
    if "$a" in line:
        s = line.index("$a")
        filled = line[:s]+a+line[s+2:]
        outlines.append(filled)
    elif "$b" in line:
        s = line.index("$b")
        filled = line[:s]+b+line[s+2:]
        outlines.append(filled)
    else:
        outlines.append(line)
with open("docker-temp.yml","w+") as f:
    f.writelines(outlines)
