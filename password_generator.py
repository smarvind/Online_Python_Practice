import string
import random
b = string.digits+string.punctuation+string.ascii_letters
a = raw_input("Do you require a computer generated password:")
c = ""
n = int(raw_input("Number of characters required in the password:"))
if a == "yes":
	length = n
	c = "".join(random.sample(b,length))
	print c

####################Another way of doing the Problem###########################
for i in range(length):
	v = random.choice(b)
	c = c + v
  

print c[:n]



