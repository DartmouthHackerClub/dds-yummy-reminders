import james.scrape
from dds.models import Subscription
	
prev_name = ""

# Subscriptions: [email, food]
# mimics nested for loops to minimize queries
for sub in Subscription.objects.all():
	
	print(str(sub))

	if sub[0] != prev_name:
		matchList = []

	items = isThere(sub[1])
	for item in items:

		matchList.concatenate(["%s @ %s [%s]" % (food, loc, cat) for food, cat, loc in listItems])

	print ("\t".join(matchList))
