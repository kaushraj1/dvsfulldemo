
with open("artifacts01.txt","r") as f:
    text=f.read()

with open("artifacts02.txt","w") as f:
    text=f.write(text+"added line") 
print("end of stage3")


