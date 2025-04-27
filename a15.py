file=open("mbox.txt")
count = 0
for line in file:
        if line.startswith('From '):
            line.strip()
            words = line.split()
            print(words[1])
            count += 1

    
print("There were", count, "lines in the file with From as the first word")