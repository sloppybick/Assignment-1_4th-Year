e=input("enter the file name:")
file=open(e)
count=0
total=0.0
for line in file:
    if line.startswith('X-DSPAM-Confidence: '):
        print(line.strip())
        confidence_str=line[len('X-DSPAM-Confidence: '):].strip()
        confidence_value=float(confidence_str)
        total=total+confidence_value
        count=count+1

if count>0:
    average=total/count
    print(f"the average spam confidence is: {average}")
else:
    print("no X-DSPAM-Confidence: lines found")

               
    