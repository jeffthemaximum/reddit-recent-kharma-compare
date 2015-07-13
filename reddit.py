#http://www.reddit.com/r/beginnerprojects/comments/1i951e/project_compare_recent_karma/

import urllib2
import json
flag = True

while flag == True:
	user1 = raw_input("Please enter the first username: ")
	user2 = raw_input("Please enter the second username: ")

	try:
		response_user1 = urllib2.urlopen('http://www.reddit.com/user/' + user1 + '.json')
	except urllib2.HTTPError, e:
	    print("User 1 does not exist.")
	    print(e.code)
	try:
		response_user2 = urllib2.urlopen('http://www.reddit.com/user/' + user2 + '.json')
	except urllib2.HTTPError, e:
	    print("User 2 does not exist.")
	    print(e.code)

	user1_json = json.loads(response_user1.read())
	user2_json = json.loads(response_user2.read())

	most_recent_user1_kharma = user1_json['data']['children'][0]['data']['score']
	most_recent_user2_kharma = user2_json['data']['children'][0]['data']['score']

	print(user1 + " scored " + str(most_recent_user1_kharma) + " khrama on his most recent post.")
	print(user2 + " scored " + str(most_recent_user2_kharma) + " kharma on his most recent post.")
