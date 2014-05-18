title = "Peanut Butter Jelly Time!"
print title.upper()
bread = 2
pb = 1
jelly = 0
none = "You need to go to the grocery store. :("

# Task Number One
if bread >= 2 and pb >= 1 and jelly >= 1:
	print "Woohoo, you can make a sandwich!"
elif pb >= 1 and jelly >=1 and bread %2 != 0:
	print "You can make an open faced or half PBJ, but otherwise need to get shopping"
else: print none

# Task Number Two - Number of Sandwiches
if pb <= jelly and pb <= (bread/2):
	sandwich = pb
elif jelly < pb and jelly < (bread/2):
	sandwich = jelly
else: sandwich = (bread/2)
if sandwich >= 1:
	print "You can make {0} PB&J sandwiches".format(sandwich)
else: print none

# Task Number Three - Open Faced or Half Sandwiches
if pb <= jelly and pb <= bread:
	of = pb
elif jelly < pb and jelly < bread:
	of = jelly
else: of = bread
if of >= 1:
	print "or you can make {0} open-faced sandwiches.".format(of)
else: print none

# Task Number Four - Missing ingredients
if pb <= jelly and pb <= (bread/2):
	print "Get some PB"
if jelly <= pb and jelly <= (bread/2):
	print "Get some jelly"
if (bread/2)<= pb and (bread/2)<= jelly:
	print "Get some bread"

# Task Number Five - No Jelly?!
if jelly <= 0 and pb >= 1 and bread >= 2:
	print "You can make a peanut butter sandwich but you should take a hard, honest look at your life."
