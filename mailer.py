import james/scrape.py
	
# for each user
users = User.objects.all()
foodRequests = FoodRequests.objects

# TODO no more users!
for user in users:
	
	name = user.username
	
	# start matchList
	# SEAN'S STUFF GOES HERE
	matchList = []
	
	# for each food
	requests = foodRequests.filter(user=name)
	for foodItem in requests:
	
		# check if foodItem is in today's Food
		listItems = isThere(foodItem)
		
		matchList.concatenate(["%s @ %s [%s]" % (food, loc, cat) for food, cat, loc in listItems])

