def main():
	print("Welcome to the special recruitment program, please answer the following questions: ")

	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	wanted_skill = 5
	cv = {}

	cv["name"] = input("What's your name? ")
	cv["age"] = input("How old are you? ")
	cv["experience"] = input("How many years of experience do you have? ")

	print()
	print("Skills: ")
	print("1. %s" % skills[0])
	print("2. %s" % skills[1])
	print("3. %s" % skills[2])
	print("4. %s" % skills[3])
	print("5. %s" % skills[4])
	print("6. %s" % skills[5])
	print()

	cv["skills"] = []

	skill = input("Choose a skill from above by entering its number: ")
	cv["skills"].append(skills[int(skill)-1])

	skill = input("Choose another skill from above by entering its number: ")
	cv["skills"].append(skills[int(skill)-1])

	if (int(cv["age"]) > 25 and int(cv["age"]) < 40) and int(cv["experience"]) > 3 and (cv["skills"][0] == skills[wanted_skill] or cv["skills"][1] == skills[wanted_skill]):
	    print("You have been accepted, %s." % cv["name"])
	else:
	    print("Sorry, you're not cool enough to work with us.")


if __name__ == '__main__':
	main()