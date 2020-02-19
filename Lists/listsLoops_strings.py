#chapter 4 WORKING WITH LISTS	

# For loops, second line must be indented
magicians = ['alice','david','carolina']
for magician in magicians:  #doesn't have to be magician, but useful for this list to describe what is being done
	print(magician)

#can use anything ex. i:
for i in magicians: # also need to have : at the end of the for statement so Python knows to interpret as a loop
	print(i)

magicians = ['alice','david','carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Outside of loop, move indent back and will only be done once
print("Thank you, everyone. That was a great magic show!")	
