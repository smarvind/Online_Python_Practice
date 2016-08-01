n = 0
while True:	
	a = raw_input("1..2..3..choose:")
	b = raw_input("1..2..3..choose:")
	if a == "done" and b =="done":
		c = raw_input("Do you want to start a new game:")
		if c == "yes":
			continue
		if c == "no":
			break
	if a == "rock" and b == "scissors":
		print "Congratulations player 'a' is the Winner"
	if a == "rock" and b == "paper":
                print "Congratulations player 'b' is the Winner" 
	if a == "scissors" and b == "paper":
                print "Congratulations player 'a' is the Winner" 
	if a == "scissors" and b == "rock":
                print "Congratulations player 'b' is the Winner" 
	if a == "paper" and b == "rock":
                print "Congratulations player 'a' is the Winner" 
	if a == "paper" and b == "scissors":
                print "Congratulations player 'b' is the Winner" 
	
	elif n < 3:
		print "Kindly give in appropriate input"
		n = n + 1
	else:
		break
