z=open("mbox.txt")
count=0
sender_code={}
for line in z:
    if line.startswith('From '):
        line.strip()
        word=line.split()
        sender=word[1]
        if sender in sender_code:
            sender_code[sender]=sender_code[sender]+1
        else:
            sender_code[sender]=1

#print(sender_code)
maxcount=0
prolific_sender=None 
for sender,count in sender_code.items():
    if count>maxcount:
        maxcount=count
        prolific_sender=sender   

        
        
if prolific_sender:
            print(f"the most prolific committer  is {prolific_sender} with {maxcount} messages")   
mincount=[]
for number in sender_code.values():
    mincount.append(number) 

for sender,number in sender_code.items():
     if min(mincount)==number:
        print(f"the least prolific committer is {sender} with {number} messages")  