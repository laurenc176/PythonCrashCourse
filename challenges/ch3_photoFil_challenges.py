rgb = [58,101,148]
for c in rgb:
	print(c)

hsl = [211, 44, 40] 

#hexidecimal colors
teal = '#57c9ba'
purple = '#712e9e'
green = '#38c750'

hexcolors = ['#57c9ba', '#712e9e', '#38c750']

decimalcolors = [1,0.75,0]
rgba = [58,101,148,0.2]

print(rgba)

modified = [a-5 for a in rgb]
print(modified)

avg = round((sum(rgb) / 3))
avg_gray = [avg, avg, avg]
max_gray = [max(rgb), max(rgb), max(rgb)]
min_gray = [min(rgb), min(rgb), min(rgb)]
r_gray = [58, 58, 58]
