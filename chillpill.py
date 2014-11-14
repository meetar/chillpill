import twython, re, time, sys
from twython import Twython, TwythonError
from keys import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, APP_ACCOUNT

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
target = APP_ACCOUNT
timeout = 15 # timeout between checks in seconds

# when this is True, prints more messages
debug = False
# debug = True

# this regex matches valid Twitter usernames (ANC = alpha-numeric character):
#   (any whitespace or non-ANC or line start) + @ + (any letter or underscore) +
#   (any ANC) + (any non-@, whitespace, non-ANC, or string end) 
regex = "((?<=[\s\W])|^)(@[a-z_]+\w*)(?=((?=[^@])[\s\W]+|$))"

while True:
  print time.asctime(time.localtime())
  # get last status
  try:
    status = twitter.show_user(screen_name=target)["status"]
  except Exception, exception:
    print "Error:"
    print exception
    if debug:
      print 'Sleeping... \n'
    time.sleep(timeout)
    continue

  tweet = status["text"].encode('utf-8')
  tweet_id = str(status["id"])

  if debug:
    print "@"+target+" status " + tweet_id + " : " + tweet

  # remove any valid usernames

  if debug:
    print "usernames found:"
    print re.findall(regex, tweet)

  m = re.sub(regex, '', tweet)

  if debug:
    print "trimmed tweet:" + m

  # find any lowercase characters
  m = re.search('[a-z]', m)
  # if none are found
  if m is None:
    # ALL CAPS - DELETE
    print tweet
    print "ALL CAPS - DELETING: " + tweet_id
    try:
      twitter.destroy_status(id=tweet_id)
    except Exception, exception:
      print "Error:"
      print exception

  else:
    if debug:
      print "you're good"
    # sys.exit()

  if debug:
    print 'Sleeping... \n'

  time.sleep(timeout)
  # sys.exit()