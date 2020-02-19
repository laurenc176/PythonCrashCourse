
def build_deck():
	face_cards = ['J','Q','K','A']
	num_cards = list(range(2,11))
	suits = ['Hearts', 'Spades','Clubs','Diamonds']

	all_cards =[]
	for s in suits:
		for n in num_cards:
			all_cards.append(f"{n} of {s}")
		for f in face_cards:
			all_cards.append(f"{f} of {s}")
	return all_cards

def get_suit(card):
	return card[5:].strip()

print(get_suit("10 of Hearts"))

def get_value(card):
	return card[:2].strip()

print(get_value("8 of Clubs"))

def same_value(card1, card2):
	return card1[:2].strip() == card2[:2].strip()

print(same_value("8 of Clubs", "8 of Hearts"))

def same_suit(card1, card2):
	return card1[5:].strip() == card2[5:].strip()

print(same_suit("8 of Clubs", "8 of Hearts"))

print(same_suit("8 of Clubs", "10 of Clubs"))
