x=open("regex-sum-42.txt")
w=list()
numbers=[]
print(x)
for line in x:
    z=line.split()
    for contents in z:
        if contents.isdigit():
            numbers.append(int(contents))
        else:
            w.append(contents)

print("\n")
#print(numbers,"\n")   
s=sum(numbers)
print(f"the sum of all the numbers is:{s} \n")
#another way



import re
file_name = input("Enter the file name: ")


file=open(file_name, 'r') 
content = file.read()
numbers = re.findall(r'\d+', content)
total_sum = sum(int(number) for number in numbers)

print(f"The sum of all numbers in the file is: {total_sum}\n")


   

      
            

        
