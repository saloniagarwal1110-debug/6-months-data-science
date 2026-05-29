import os
name=input("enter your name:-")
last_name=input("enter your last_name:-")
dob=input("enter your date of birth:-")
gender=input("enter your gender:-")
address=input("enter your address")

os.mkdir(name)

details=[]

details.append("Name:"+name)
details.append("last_name:"+last_name)
details.append("dob:"+dob)
details.append("gender:"+gender)
details.append("address:"+address)


file=open(f"{name}/{name}.txt","w")
file.write("\n".join(details))
file.close()