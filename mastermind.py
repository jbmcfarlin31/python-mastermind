import random
import re


COLORS = {
	1: 'r',
	2: 'b',
	3: 'g',
	4: 'w',
	5: 'y'
}
COLORS_TEXT = {
	'r': 'red',
	'b': 'blue',
	'g': 'green',
	'w': 'white',
	'y': 'yellow'
}

MASTER_SOLUTION = []

PATTERN = "^[r,b,g,w,y]+$"


def check_answer(answer, nbr_colors):
	""" This method handles the logic for checking whether or not the answer is correct """

	def check_result(ans,ms):
		""" Helper method to handle repeated checks """
		if ans <= ms:
			result = ans
		else:
			result = ms

		return result
	# -----------------------------------

	# Set some default variables
	global MASTER_SOLUTION

	check1, check2, check3, check4, check5 = 0,0,0,0,0

	r_cnt_ms, b_cnt_ms, g_cnt_ms, w_cnt_ms, y_cnt_ms = 0,0,0,0,0
	r_cnt_ans, b_cnt_ans, g_cnt_ans, w_cnt_ans, y_cnt_ans = 0,0,0,0,0
	r_result, b_result, g_result, w_result, y_result = 0,0,0,0,0

	# Handles the correct answer in the correct space logix
	if answer[0] == MASTER_SOLUTION[0]:
		check1 = 1

	if answer[1] == MASTER_SOLUTION[1]:
		check2 = 1

	if answer[2] == MASTER_SOLUTION[2]:
		check3 = 1

	if answer[3] == MASTER_SOLUTION[3]:
		check4 = 1

	if answer[4] == MASTER_SOLUTION[4]:
		check5 = 1

	correct_answer_in_correct_space = check1 + check2 + check3 + check4 + check5

	# Default is always 2, so we will always have the values
	r_cnt_ms = MASTER_SOLUTION.count("r")
	r_cnt_ans = answer.count("r")

	r_result = check_result(r_cnt_ans, r_cnt_ms)

	b_cnt_ms = MASTER_SOLUTION.count("b")
	b_cnt_ans = answer.count("b")

	b_result = check_result(b_cnt_ans, b_cnt_ms)

	# If they choose more than 2 colors we handle it here
	if nbr_colors > 2:
		g_cnt_ms = MASTER_SOLUTION.count("g")
		g_cnt_ans = answer.count("g")
		g_result = check_result(g_cnt_ans, g_cnt_ms)

	if nbr_colors > 3:
		w_cnt_ms = MASTER_SOLUTION.count("w")
		w_cnt_ans = answer.count("w")
		w_result = check_result(w_cnt_ans, w_cnt_ms)

	if nbr_colors > 4:
		y_cnt_ms = MASTER_SOLUTION.count("y")
		y_cnt_ans = answer.count("y")
		y_result = check_result(y_cnt_ans, y_cnt_ms)

	correct_answer_in_wrong_space = r_result + b_result + g_result + w_result + y_result
	correct_answer_in_wrong_space = correct_answer_in_wrong_space - correct_answer_in_correct_space

	print('\n')
	# answer_text = COLORS_TEXT[answer[0]]
	# answer_text = answer_text + ', '

	# answer_text = COLORS_TEXT[answer[1]]
	# answer_text = answer_text + ', '
	
	# answer_text = COLORS_TEXT[answer[2]]
	# answer_text = answer_text + ', '
	
	# answer_text = COLORS_TEXT[answer[3]]
	# answer_text = answer_text + ', '

	# answer_text = COLORS_TEXT[answer[4]]
	# answer_text = answer_text

	answer_text = """
	You entered {}, {}, {}, {}, {}
	""".format(COLORS_TEXT[answer_text[0]],COLORS_TEXT[answer_text[1]],COLORS_TEXT[answer_text[2]],COLORS_TEXT[answer_text[3]],COLORS_TEXT[answer_text[4]])

	print("You entered {}".format(answer_text))

	print("The correct number in the correct spot was {}".format(correct_answer_in_correct_space))
	print("The correct number in the wrong spot was {}".format(correct_answer_in_wrong_space))
	print('\n')

	if correct_answer_in_correct_space == 5:
		end_game = True
	else:
		end_game = False


	return end_game

# ---------------------------------------------------

def run():
	""" Handles the starting of the game """

	# Get how many colors the user wants to play with
	nbr_colors = input("How many colors do you want to play with? (2-5): ")
	nbr_colors = int(nbr_colors)

	# Empty list that will store what colors are chosen
	color_list = []
	for x in range(nbr_colors):
		color_list.append(COLORS[x+1])

	# Build the master solution so we know what the solution is
	for x in range(5):
		rand_nbr = random.randint(1,nbr_colors)
		MASTER_SOLUTION.append(COLORS[rand_nbr])

	# Debug statements to see what our solution is
	#print("[DEBUG] The MASTER SOLUTION is:",MASTER_SOLUTION,'\n')

	# Just some helpful info to display to the user
	print("You are playing with {} colors. Your choices can be 5 of the following letters: {}\n".format(nbr_colors, color_list))

	# Start the logic for playing the game
	userCounter = 0
	end_game = False
	while end_game == False:

		# Prompt user for their choice
		answer = input("What 5 colors would you like to try?: {} ".format(color_list))
		answer = str(answer)
		userCounter += 1

		# Check the answer to make sure it is a valid selection by matching our regex
		if re.search(PATTERN,answer):
			if len(answer) == 5:
				# Check user answer with MASTER_SOLUTION
				end_game = check_answer(answer, nbr_colors)
			else:
				print("You must choose 5 letters.")
		else:
			print("You are playing with {} colors. Your choices can be 5 of the following letters: {}".format(nbr_colors, color_list))


	print("Congratulations, you won!!! It took you {} tries to win".format(userCounter))

# ------------------------------------------------

# Run the game
run()
