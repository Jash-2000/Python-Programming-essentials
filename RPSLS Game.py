"""
	This is a Python script that is used to create the RPSLS i.e. 
    Rock-Paper-Scissors-Lizard-Spock game. 
    
    This is my first project.
    
    In this game, the user plays against the computer and provides an
    input from the options available to them. The exact rules are a follows: - 

    The method for determining the winner is to assign each of the five choices a number:

	0 — rock
	1 — Spock
	2 — paper
	3 — lizard
	4 — scissors
	
	In this expanded list, each choice wins against the preceding two choices and loses against the following two choices 
	(if rock and scissors are thought of as being adjacent using modular arithmetic).


"""


import random   # importing required libraries. 

# Function to create codes.
def name_to_code(user_inp):      
    
    if user_inp == "rock" or user_inp == "ROCK" :
        user_code = 0
        
    elif user_inp == "spock" or user_inp == "SPOCK" :
        user_code = 1
    
    elif user_inp == "paper" or user_inp == "PAPER" :
        user_code = 2

    elif user_inp == "LIZARD" or user_inp == "lizard" :
        user_code = 3

    elif user_inp == "scissors" or user_inp == "SCISSORS" :
        user_code = 4

    else :
    	print("Choose a correct choice please!!!!!!")    

    return user_code
    

# Function to display the choice from the code.
def code_to_name(code):

	if code == 0 :
		inp = "ROCK"

    elif code == 1:
    	inp = "SPOCK"

    elif code == 2:
    	inp = "PAPER"

    elif code == 3:
    	inp = "LIZARD"

    elif code == 4:
    	inp = "SCISSORS"
    
    else :
    	PASS   

    return inp

# Main game's logic
def rspls(ref,comp) :

	error = 2 - ref          			# User input referenced to 2
	comp = (comp+error) % 5

	if(comp - 2 > 0) :
		print(" Sorry , you loose this round ")
	elif(comp - 2 <0) :
		print("YAY, you win")
	else :
		print("Its a tie")




# Main game's code.

print("                    Welcome to vaishvi's GAMING world!!!!!!!!!!!!!!!")
print("========================================================================================")
print("")
print("We are playing RPSLS. Please choose your choice from the following:")
print("1) Rock")
print("2) Spock")
print("3) Paper")
print("4) Lizard")
print("5) Scissors")
print("Please choose an option now : ")

user_inp = input("Your Input please")              # Taking user input.
comp_code = random.randint(0,4)  # Taking random input for computer.

comp_inp = code_to_name(comp_code)
user_code = name_to_code(user_inp)

print("")
print("")
if user_code == "NONE" :
	print("BTW, computer choose :" , comp_inp)

else :

	print("Your choice was : " , user_inp)
	print("Computer's choice was : ", comp_inp)
	print("And the result is :")
	rspls(user_code,comp_code)

print("")
print("")
print("Game Ends here!!!!!!!!")