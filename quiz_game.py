#Ask the user if he/she will like to play
#Prompt user to enter number of questions he/she will like to answer
#Prompt a question to the user randomly
#Collect answer from user as input
#Check if the answer is correct or wrong
#Print number of correct answers

from random import randint

user_decision = eval(input("Will you like to play? Yes, press 1 0r 0 to exit\n"))

number_of_questions = int(input("How many questions will you like to play\n"))

correct_answers = 0

question_counter = 1

if (user_decision != 0):

	while (question_counter <= number_of_questions):

		random_question = randint(1,20)

		print ("Select a to c for this question")

		if (random_question == 1):

			selected_answer = input ("Question 1: What is the product of 3 and 5? a)23 (b)20 (c)15\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers = correct_answers + 1

		elif (random_question == 2):

			selected_answer = input ("Question 2: What is the sum of 3 and 5? a)23 (b)2 (c)8\n")
			if (selected_answer) == "a": 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 3):

			selected_answer = input ("Question 3: What is the difference between 5 and 2? a)2 (b)20 (c)3\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 4):

			selected_answer = input ("Question 4: What is the first letter in the English alphabet? a)A (b)D (c)C\n")
			if (selected_answer == "a"): 
				print("correct")
				correct_answers += 1

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("failed")

		elif (random_question == 5):

			selected_answer = input ("Question 5: Who is the president of Nigeria? a)Tinubu (b) Buhari (c) Chinedu\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("correct")
				correct_answers += 1
			else:
				print("failed")
		elif (random_question == 6):

			selected_answer = input ("Question 6: What is the product of 3 and 5? a)23 (b)20 (c)15\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers = correct_answers + 1

		elif (random_question == 7):

			selected_answer = input ("Question 7: What is the sum of 3 and 5? a)23 (b)2 (c)8\n")
			if (selected_answer) == "a": 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 8):

			selected_answer = input ("Question 8: What is the difference between 5 and 2? a)2 (b)20 (c)3\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 9):

			selected_answer = input ("Question 9: What is the first letter in the English alphabet? a)A (b)D (c)C\n")
			if (selected_answer == "a"): 
				print("correct")
				correct_answers += 1

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("failed")

		elif (random_question == 10):

			selected_answer = input ("Question 10: Who is the president of Nigeria? a)Tinubu (b) Buhari (c) Chinedu\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("correct")
				correct_answers += 1
			else:
				print("failed")
		elif (random_question == 11):

			selected_answer = input ("Question 11: What is the product of 3 and 5? a)23 (b)20 (c)15\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers = correct_answers + 1

		elif (random_question == 12):

			selected_answer = input ("Question 12: What is the sum of 3 and 5? a)23 (b)2 (c)8\n")
			if (selected_answer) == "a": 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 13):

			selected_answer = input ("Question 13: What is the difference between 5 and 2? a)2 (b)20 (c)3\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 14):

			selected_answer = input ("Question 14: What is the first letter in the English alphabet? a)A (b)D (c)C\n")
			if (selected_answer == "a"): 
				print("correct")
				correct_answers += 1

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("failed")

		elif (random_question == 15):

			selected_answer = input ("Question 15: Who is the president of Nigeria? a)Tinubu (b) Buhari (c) Chinedu\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("correct")
				correct_answers += 1
			else:
				print("failed")
		elif (random_question == 16):

			selected_answer = input ("Question 16: What is the product of 3 and 5? a)23 (b)20 (c)15\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers = correct_answers + 1

		elif (random_question == 17):

			selected_answer = input ("Question 17: What is the sum of 3 and 5? a)23 (b)2 (c)8\n")
			if (selected_answer) == "a": 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 18):

			selected_answer = input ("Question 18: What is the difference between 5 and 2? a)2 (b)20 (c)3\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("correct")
				correct_answers += 1

		elif (random_question == 19):

			selected_answer = input ("Question 19: What is the first letter in the English alphabet? a)A (b)D (c)C\n")
			if (selected_answer == "a"): 
				print("correct")
				correct_answers += 1

			elif (selected_answer == "b"):
				print("failed")

			else:
				print("failed")

		elif (random_question == 20):

			selected_answer = input ("Question 20: Who is the president of Nigeria? a)Tinubu (b) Buhari (c) Chinedu\n")
			if (selected_answer == "a"): 
				print("failed")

			elif (selected_answer == "b"):
				print("correct")
				correct_answers += 1
			else:
				print("failed")
	
		question_counter += 1

print("You answered {} correct questions".format(correct_answers))	
