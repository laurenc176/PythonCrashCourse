hearts = []
for i in range(2,11):
	hearts.append(f"{i} of Hearts")
hearts.append("J of Hearts")
hearts.append("Q of Hearts")
hearts.append("K of Hearts")
hearts.append("A of Hearts")

#print(hearts)

#for i in hearts:
#	print(i)
#for i in hearts[0:-4]:
#	print(i)
#for i in hearts[-4:]:
#	print(i)

face_cards = ['J','Q','K','A']
num_cards = list(range(2,11))
print(num_cards)

suits = ['Hearts', 'Spades','Clubs','Diamonds']

all_cards =[]
for s in suits:
	for n in num_cards:
		all_cards.append(f"{n} of {s}")
	for f in face_cards:
		all_cards.append(f"{f} of {s}")

print(all_cards)
print('\n')
h=[]

for i in all_cards:
	if 'Hearts' in i:
		h.append(i)
print(h)

