import tweepy 	#	tweepy package
import json		#	twitter json handler
# import xlwt		#	writting to excel sheets
# import textblob	#	sentimetn analysis in python

#	to disable urllib warning
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

#	user ids obtained by registering you app on twitter
consumer_key = '*******************'
consumer_secret = '****************'
access_token = '*********-*********'
access_token_secret = '****************'

#	Authenticate user credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit  = True, wait_on_rate_limit_notify = True)

''' Get tweets from your timeline'''
public_tweets = api.home_timeline()		# Shows your tweets
public_tweets = api.followers()			# Shows your followers
# print public_tweets
for tweet in public_tweets:
    print tweet
    print '\n-------', count
    count += 1

''' Search for tweets with specific string. '''
search_text = 'helmet'										# search keyword
search_number = 50
count = 0
search_tweets = api.search(search_text, rpp=search_number)	# Search for a in the tweeet / status
for tweet in search_tweets:
	print tweet.text
	print '\n------',count
	count = count + 1

'''Cursor example'''
count = 1
follower_count = 1

''' query for a particular tweet and store tweets in a txt file'''
f = open("data.txt","a")
query = "helmet"
ids = []
max_tweets = 10
for tweet in tweepy.Cursor(api.search, q=query, count = 100, lang = "en").items(max_tweets):
	# print '\n\n Retrieving Tweet...', type(tweet)
	# j_tweet = json.dumps(tweet._json)
	print "----------------------"
	print count, tweet.text #tweet.user.screen_name, '---',type(tweet.user.description)
	print tweet.user.name, '...',tweet.user.description,'...', tweet.user.screen_name
	for friend_id in tweepy.Cursor(api.friends_ids,user_id=tweet.user.id, count = 100).items():
		print follower_count, api.get_user(friend_id).screen_name 
		follower_count += 1
	# f.write(str(count)+tweet.text+'\n')
	# print count,' ',
	count += 1
	# break
membercnt = 0
count = 0

'''search users and find tweets'''
query_list = [' helmet ' , ' hat ']
for user in tweepy.Cursor(api.search_users, q='Construction Worker').items():		# Find people related to 'Construntion Worker Keyword'	
	print membercnt, user.screen_name, user.friends_count
	membercnt+=1
	for user_follows in tweepy.Cursor(api.friends_ids, user_id = user.id).items():
		# print count,
		count+=1
		if 'construction' in api.get_user(user_follows).description:
			print api.get_user(user_follows).screen_name,
		if count == 10:
			# print '\n'
			count = 0
			break
			# print user_follows.id, user_follows.screen_name
	# break
	
	for user_tweets in tweepy.Cursor(api.user_timeline, user_id=user.id).items():	# Get their tweets
		status =  user_tweets.text
		if any(word in status for word in query_list):								# Check if the tweet matches out quert list, any() return T/F
			print status
			try:
				f.write(str(count)+tweet.text+'\n')
				print 'write to file : Tweet ',str(count)
			except:
				print 'Skipping tweet write ',str(count)
		count += 1
f.close()