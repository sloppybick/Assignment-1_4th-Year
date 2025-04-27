z=open("amth.txt")

teachers=[]

for line in z:
    if line.startswith('Applied'):
        continue
    else:
        x=line.split()
        for name in x:
            if name not in teachers:
             teachers.append(name)


teachers.sort()
print(teachers)    