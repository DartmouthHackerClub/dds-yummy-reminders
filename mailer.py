# for each user
users = User.objects.all()
foodRequests = FoodRequests.objects

for user in users:
	
	name = user.username
	
	# start matchList
	# SEAN'S STUFF GOES HERE
	matchList = []

	# for each food
	requests = foodRequests.filter(user=name)
	for foodItem in requests:

		# check if foodItem is in today's Food
		listItem = menu.isthere(foodItem)
		if listItem != false:
			
			# print and add to matchList

