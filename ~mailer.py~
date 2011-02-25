import james/scrape.py
	
# for each user
users = User.objects.all()
foodRequests = FoodRequests.objects

prev_name = ""

# Subscriptions: [email, food]
# mimics nested for loops to minimize queries
for sub in Subscriptions.objects.all()

	if sub[0] != prev_name:
		matchList = []

	items = isThere(sub[1])
	for item in items:

# THIS IS AN INTERMEDIARY W.I.P.

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

