from james.scrape import isThere
from james.blitz import blitz
from dds.models import Subscription
	
prev_name = ""

# Subscriptions: [email, food]
# mimics nested for loops to minimize queries
for sub in Subscription.objects.all():

	if sub.email != prev_name:
		print("email: %s -> %s" % (prev_name, sub.email))
		body = []
		subject = []
		prev_name = sub.email
		if body:
			blitz(sub.email, "[DDS TODAY]: "+", ".join(subject), "\n".join(body))
			

	items = isThere(sub.food)
	
	if items:
		# sorry this is a little hacky/sloppy/whatever
		body.append("%s! YOUR FAVORITE!" % (sub.food.upper(),))
		body.extend(["%s @ %s [%s]" %  (food, loc, cat) for food,cat,loc in items])
		body.append("") #add a filler line to seperate query terms
		subject.append(sub.food.lower())

if body:
	print("\nSUBJECT:\n" + " ".join(subject));
	print("\nBODY:\n" + "\n".join(body));
	body.append("---\nThis is a service of Hacker Club. To unsubscribe, go here:")
	body.append(sub.unsubscribe_link())
	blitz(sub.email, "[DDS TODAY]: "+", ".join(subject), "\n".join(body))
