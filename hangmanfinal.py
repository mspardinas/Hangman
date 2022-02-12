import os.path
import random
def life6(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print("_|______")
def life5(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print("_|______")
def life4(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" |   |  ")
	print(" |   |  ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print("_|______")
def life3(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" | --|  ")
	print(" | | |  ")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print("_|______")
def life2(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" | --|--")
	print(" | | | |")
	print(" |      ")
	print(" |      ")
	print(" |      ")
	print("_|______")
def life1(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" | --|--")
	print(" | | | |")
	print(" |   ^  ")
	print(" |  |   ")
	print(" |  |   ")
	print("_|______")
def life0(y):
	print("Lives remaining: ", y)
	print("________")
	print(" |   |  ")
	print(" |   O  ")
	print(" | --|--")
	print(" | | | |")
	print(" |   ^  ")
	print(" |  | | ")
	print(" |  | | ")
	print("_|______")
def lifecheck(oof):
	if oof == 6:
		life6(oof)
	elif oof == 5:
		life5(oof)
	elif oof == 4:
		life4(oof)
	elif oof == 3:
		life3(oof)
	elif oof == 2:
		life2(oof)
	elif oof == 1:
		life1(oof)
def title():
	print()
	print("+=====================================================================+")
	print("       _   _    ___    _   _   _____     ___  ___   ___    _   _       ")
	print("      | | | |  / _ \  | \ | | |  __ \    |  \/  |  / _ \  | \ | |      ")
	print("      | |_| | / /_\ \ |  \| | | |  \/    | .  . | / /_\ \ |  \| |      ")
	print("      |  _  | |  _  | | . ` | | | __     | |\/| | |  _  | | . ` |      ")
	print("      | | | | | | | | | |\  | | |_\ \    | |  | | | | | | | |\  |      ")
	print("      \_| |_/ \_| |_/ \_| \_/  \____/    \_|  |_/ \_| |_/ \_| \_/      ")
	print()
	print("+=====================================================================+")
	print()
	intro()
def spacer():
	print()
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
def intro():
	player = str(input("Enter username with a length 3: "))
	if len(player) != 3:
		print()
		print("Enter a username with a length of 3 only" + "\n")
		intro()
	elif len(player) == 3:
		print()
	print("Hello " + player + "!" + " Welcome to Hangman!")
	menu(player)
def menu (player):
	spacer()
	print("[1]Play now   [2]How to play   [3]View high scores   [4]Exit" + "\n")
	answer = str(input("Enter choice of preferred action(e.g. 2 to view game instructions): "))
	if answer == "1":
		spacer()
		playhangman(player)
	elif answer == "2":
		manual(player)
		menu(player)
	elif answer == "3":
		if os.path.exists("hangmanscores.txt"):
			print("___________________")
			print("|                 |")
			print("|  Name    Score  |")
			scoreread = open("hangmanscores.txt", "r")
			for line in scoreread:
				newline = line[:-1].split(",")
				if len(newline[1]) == 2: #checks if length of score is 2 e.g. 12 or 15
					print("|  " + newline[0] + "       " + newline[1] + "   |")
				elif len(newline[1]) == 1: #checks if length of score is 1 e.g. 7 or 4
					print("|  " + newline[0] + "        " + newline[1] + "   |")
			print("|_________________|")
			scoreread.close()
		else:
			print()
			print("There are no current highscores for this game")
		menu(player)
	elif answer == "4":
		spacer()
		print("Goodbye " + player + "!")
	else:
		print()
		print("Invalid input")
		print()
		menu(player)
def manual(name):
	spacer()
	print("The game's mechanics are as follows:")
	print("You,", name, ",are given 6 (six) chances of guessing an unknown word")
	print("You will guess the word by inputting a desired letter")
	print("You may only enter 1 (one) letter at a time every turn")
	print("The higher the difficulty, the higher the maximum score")
	print("Good luck " + name + "!")
def categorier(x, y, z): #x = chosen category, y = chosen difficulty, z = categories.txt
	catelinesz = z.readlines() 
	catelines = (catelinesz[int(x)-1])[:-1].split(",")
	if y == "A":
		index = 1
	elif y == "B":
		index = 2
	elif y == "C":
		index = 3
	return catelines[index]
def progressor(x):
	print("Word progress: " + "\n")
	for k in x:
		print(k, " ", end="")
	print()
	print()
def result(livesleft, smultiplier, playername):
	if livesleft == 0:
		life0(livesleft)
		print()
		print("You lose.. better luck next time, " + playername + ".")
		playagain()
	else:
		print()
		print("Congratulations, " + playername + "!" + " You win with " + str(livesleft) + " lives remaining")
		finalscore = livesleft*smultiplier
		print("You have a score of:", finalscore)
		if os.path.exists("hangmanscores.txt"):
			readscore = open("hangmanscores.txt", "r")
			counter = 0
			switch = False
			if switch == False:
				for indivline in readscore:
					indivscore = indivline[:-1].split(",")
					if finalscore >= int(indivscore[1]):
						readscores = open("hangmanscores.txt", "r")
						currentscore = (playername + "," + str(finalscore) + "\n")
						linez = readscores.readlines()
						linez.insert(counter, currentscore)
						readscores.close()
						nowscores = open("hangmanscores.txt", "w")
						nowscores.writelines(linez)
						nowscores.close()
						switch = True
						break
					counter += 1
				readscore.close()
				if switch == False:
					scorehandle = open("hangmanscores.txt", "a")
					scorehandle.write(playername + "," + str(finalscore) + "\n")
					scorehandle.close()
		else: 
			scorehandle_new = open("hangmanscores.txt", "w")
			scorehandle_new.write(playername + "," + str(finalscore) + "\n")
			scorehandle_new.close()
		playagain()
def playagain():
	spacer()
	player = str(input("Do you wish to play again? Y/N: "))
	if player == "Y":
		spacer()
		intro()
	elif player == "N":
		print("Goodbye, thank you for playing!")
	else:
		print("Invalid input, Y or N only.")
		print()
		playagain()
def playhangman(playername):
	print("CATEGORIES: " + "\n")
	categoryhandle_1 = open("categories.txt", "r") #handle to get categories
	for category in categoryhandle_1:
		newcat = category[:-1].split(",")
		print(newcat[0])
	print()
	categoryhandle_1.close()
	print("Difficulties: [A] Easy, [B] Medium, [C] Hard")
	spacer()
	while True:
		category = str(input("Enter category of choice (e.g. input '3' for Food): "))
		if category == "1" or category == "2" or category == "3":
			print()
			break
		else:
			print("Invalid input, try again")
			continue
	while True:
		difficulty = str(input("Enter difficulty of choice (e.g. input B for Medium): "))
		if difficulty == "A" or difficulty == "B" or difficulty == "C":
			break
		else:
			print("Invalid input, try again")
			continue
	spacer()
	categoryhandle_2 = open("categories.txt", "r")  #handle to get categories with difficulties
	handle2 = open((categorier(category, difficulty, categoryhandle_2)), "r")
	categoryhandle_2.close()
	x = random.randint(0, 34)
	line = handle2.readlines()
	word = (line[x])[:-1]
	print(word)
	handle2.close()
	progress = []
	for letter in word:
		progress.append("_")
	lives = 6
	progressor(progress)
	life6(lives)
	if difficulty == "A":
		scoremultiplier = 1
	elif difficulty == "B":
		scoremultiplier = 2
	elif difficulty == "C":
		scoremultiplier = 3
	while lives > 0 and "_" in progress:
		letterguess = input("\n" + "Enter your desired letter: ")
		if letterguess in word:
			spacer()
			print("Correct! Nice job " + playername + "!")
			print()
			indexer = 0
			for i in word:
				if i != letterguess:
					indexer += 1
				elif i == letterguess:
					progress[indexer] = letterguess
					indexer += 1
			progressor(progress)
			lifecheck(lives)
		elif letterguess not in word:
			spacer()
			print("Sorry, " + playername + ", your desired letter is not in the word.")
			print()
			lives -= 1
			progressor(progress)
			lifecheck(lives)
	result(lives, scoremultiplier, playername)
title()