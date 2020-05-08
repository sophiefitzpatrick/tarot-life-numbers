import constants
import random
import sys
import time

class StringFormat:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

f = StringFormat()

def begin():
	print(f.BOLD + f.YELLOW + constants.TITLE_CREDITS + f.END)
	print(constants.ABOUT)
	choose_reading()

def choose_reading():
	pick_reading = input("\n" + f.YELLOW + "Enter your choice of reading to continue or \"exit\" to quit Tarot: " + f.END).lower()

	if pick_reading in constants.ULTIMATE_FAN_SPREAD:
		ultimate_fan_spread()
	elif pick_reading in constants.CELTIC_CROSS_SPREAD:
		celtic_spread()
	elif pick_reading in constants.EXIT:
		sys.exit(f.BOLD + f.YELLOW + constants.EXIT_SYSTEM + f.END)
	else:
		choose_reading()

def shuffle(deck, shuffle):
	if shuffle == "shuffle":
		card_keys = list(deck.keys())
		random.shuffle(card_keys)
	elif shuffle == "exit":
		choose_reading()
	else:
		shuffle()

	return card_keys

def choose_cards(number_of_cards, shuffled_cards):
	chosen_cards = []
	for i in range(number_of_cards):
		random_index = random.randrange(len(shuffled_cards))
		shuffled_cards[random_index], shuffled_cards[-1] = shuffled_cards[-1], shuffled_cards[random_index]
		chosen_card = shuffled_cards.pop()
		chosen_cards.append(chosen_card)

	return chosen_cards

def ultimate_fan_spread():
	print(constants.FAN)

	shuffle_input = input(f.YELLOW + "Enter \"shuffle\" to read or \"exit\" to choose another reading: " + f.END).lower()

	shuffled_cards = shuffle(deck=constants.CARDS, shuffle=shuffle_input)
	chosen_cards = choose_cards(number_of_cards=22, shuffled_cards=shuffled_cards)
	chosen_cards_dict = dict([(key, constants.CARDS[key]) for key in chosen_cards])

	time.sleep(2)

	print("\n \n \n" + f.YELLOW + constants.LINES + f.END + f.BOLD + "\n \n" + "| Your Reading:" + f.END + "\n")

	you = "| %s: %s" % (chosen_cards[0], chosen_cards_dict[chosen_cards[0]])
	character = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[1],
		chosen_cards_dict[chosen_cards[1]],
		chosen_cards[2],
		chosen_cards_dict[chosen_cards[2]],
		chosen_cards[3],
		chosen_cards_dict[chosen_cards[3]]
	)
	emotion = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[4],
		chosen_cards_dict[chosen_cards[4]],
		chosen_cards[5],
		chosen_cards_dict[chosen_cards[5]],
		chosen_cards[6],
		chosen_cards_dict[chosen_cards[6]]
	)
	desire = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[7],
		chosen_cards_dict[chosen_cards[7]],
		chosen_cards[8],
		chosen_cards_dict[chosen_cards[8]],
		chosen_cards[9],
		chosen_cards_dict[chosen_cards[9]]
	)
	expectation = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[10],
		chosen_cards_dict[chosen_cards[10]],
		chosen_cards[11],
		chosen_cards_dict[chosen_cards[11]],
		chosen_cards[12],
		chosen_cards_dict[chosen_cards[12]]
	)
	unexpected = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[13],
		chosen_cards_dict[chosen_cards[13]],
		chosen_cards[14],
		chosen_cards_dict[chosen_cards[14]],
		chosen_cards[15],
		chosen_cards_dict[chosen_cards[15]]
	)
	near_future = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[16],
		chosen_cards_dict[chosen_cards[16]],
		chosen_cards[17],
		chosen_cards_dict[chosen_cards[17]],
		chosen_cards[18],
		chosen_cards_dict[chosen_cards[18]]
	)
	far_future = "| %s: %s \n| %s: %s \n| %s: %s" % (
		chosen_cards[19],
		chosen_cards_dict[chosen_cards[19]],
		chosen_cards[20],
		chosen_cards_dict[chosen_cards[20]],
		chosen_cards[21],
		chosen_cards_dict[chosen_cards[21]]
	)

	print(f.BOLD + f.YELLOW + constants.YOU + f.END + "\n" + you + "\n")
	print(f.BOLD + f.YELLOW + constants.CHARACTER + f.END + "\n" + character + "\n")
	print(f.BOLD + f.YELLOW + constants.EMOTION + f.END + "\n" + emotion + "\n")
	print(f.BOLD + f.YELLOW + constants.DESIRE + f.END + "\n" + desire + "\n")
	print(f.BOLD + f.YELLOW + constants.EXPECTATION + f.END + "\n" + expectation + "\n")
	print(f.BOLD + f.YELLOW + constants.UNEXPECTED_FACTORS + f.END + "\n" + unexpected + "\n")
	print(f.BOLD + f.YELLOW + constants.NEAR_FUTURE + f.END + "\n" + near_future + "\n")
	print(f.BOLD + f.YELLOW + constants.FAR_FUTURE + f.END + "\n" + far_future + "\n \n \n")
	print(f.YELLOW + constants.LINES + "\n \n")

	time.sleep(5)
	choose_reading()

def celtic_spread():
	print(constants.CELTIC)

	shuffle_input = input(f.YELLOW + "Enter \"shuffle\" to read or \"exit\" to choose another reading: " + f.END).lower()

	upright_shuffled_cards = shuffle(deck=constants.CARDS, shuffle=shuffle_input)
	upright_chosen_cards = choose_cards(number_of_cards=8, shuffled_cards=upright_shuffled_cards)
	upright_chosen_cards_dict = dict([(key, constants.CARDS[key]) for key in upright_chosen_cards])

	reversed_shuffled_cards = shuffle(deck=constants.REVERSED_CARDS, shuffle=shuffle_input)

	for card in upright_chosen_cards:
		reversed_shuffled_cards.remove(card)

	reversed_chosen_cards = choose_cards(number_of_cards=2, shuffled_cards=reversed_shuffled_cards)
	reversed_chosen_cards_dict = dict([(key, constants.REVERSED_CARDS[key]) for key in reversed_chosen_cards])

	time.sleep(2)

	print("\n \n \n" + f.YELLOW + constants.LINES + f.END + f.BOLD + "\n \n" + "| Your Reading:" + f.END + "\n")

	you = "| %s: %s" % (upright_chosen_cards[0], upright_chosen_cards_dict[upright_chosen_cards[0]])
	situation = "| %s: %s" % (upright_chosen_cards[1], upright_chosen_cards_dict[upright_chosen_cards[1]])
	foundation = "| (R) %s: %s" % (reversed_chosen_cards[0], reversed_chosen_cards_dict[reversed_chosen_cards[0]])
	recent_past = "| %s: %s" % (upright_chosen_cards[2], upright_chosen_cards_dict[upright_chosen_cards[2]])
	short_term_outlook = "| %s: %s" % (upright_chosen_cards[3], upright_chosen_cards_dict[upright_chosen_cards[3]])
	present_state_of_problem = "| (R) %s: %s" % (reversed_chosen_cards[1], reversed_chosen_cards_dict[reversed_chosen_cards[1]])
	outside_influences = "| %s: %s" % (upright_chosen_cards[4], upright_chosen_cards_dict[upright_chosen_cards[4]])
	inside_influences = "| %s: %s" % (upright_chosen_cards[5], upright_chosen_cards_dict[upright_chosen_cards[5]])
	hopes_and_fears = "| %s: %s" % (upright_chosen_cards[6], upright_chosen_cards_dict[upright_chosen_cards[6]])
	long_term_outcome = "| %s: %s" % (upright_chosen_cards[7], upright_chosen_cards_dict[upright_chosen_cards[7]])

	print(f.BOLD + f.YELLOW + constants.YOU + f.END + "\n" + you + "\n")
	print(f.BOLD + f.YELLOW + constants.SITUATION + f.END + "\n" + situation + "\n")
	print(f.BOLD + f.YELLOW + constants.FOUNDATION + f.END + "\n" + foundation + "\n")
	print(f.BOLD + f.YELLOW + constants.RECENT_PAST + f.END + "\n" + recent_past + "\n")
	print(f.BOLD + f.YELLOW + constants.SHORT_TERM_OUTLOOK + f.END + "\n" + short_term_outlook + "\n")
	print(f.BOLD + f.YELLOW + constants.PRESENT_STATE_OF_PROBLEM + f.END + "\n" + present_state_of_problem + "\n")
	print(f.BOLD + f.YELLOW + constants.OUTSIDE_INFLUENCES + f.END + "\n" + outside_influences + "\n")
	print(f.BOLD + f.YELLOW + constants.INSIDE_INFLUENCES + f.END + "\n" + inside_influences + "\n")
	print(f.BOLD + f.YELLOW + constants.HOPES_AND_FEARS + f.END + "\n" + hopes_and_fears + "\n")
	print(f.BOLD + f.YELLOW + constants.LONG_TERM_OUTCOME + f.END + "\n" + long_term_outcome + "\n \n \n")
	print(f.YELLOW + constants.LINES + "\n \n")

	time.sleep(5)
	choose_reading()
