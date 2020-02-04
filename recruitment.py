def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	name = input('What\'s your name? ')
	age = int(input('How old are you? '))
	experience = int(input('How many years of experience do you have? '))

	cv['name'] = name
	cv['age'] = age
	cv['experience'] = experience
	cv['skills'] = []

	for idx, skill in enumerate(skills):
		print(str(idx+1)+'. '+skill)

	print(' ')
	skill1 = int(input('Choose a skill from above by entering its number: '))
	skill2 = int(input('Choose another skill from above by entering its number: '))

	cv['skills'] = [skills[skill1-1], skills[skill2-1]]

	if cv['age'] >= 25 and cv['age'] <= 40 and cv['experience'] > 5 and (skill1==6 or skill2==6):
		print('You have been accepted, '+name+'.')
	else:
		print('You have been rejected, '+name+'.')


if __name__ == '__main__':
	main()
