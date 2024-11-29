#import responses
#import requests

#@responses.activate
#def test_my_api():
#    responses.add(responses.GET, 'http://twitter.com/api/1/foobar',body='{"error": "not found"}', status=404,content_type='application/json')
#    resp = requests.get('http://twitter.com/api/1/foobar')
#    assert resp.json() == {"error": "not found"}
#    assert len(responses.calls) == 1
#    assert responses.calls[0].request.url == 'http://twitter.com/api/1/foobar'
#    assert responses.calls[0].response.text == '{"error": "not found"}'

# pip install tweepy
# http://tweepy.readthedocs.io/en/v3.5.0/api.html#timeline-methods
import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'AA443eBSdMKWu4sBQ3NZ9Bo94ciC5AA'
consumer_secret = 'AA44A0zmqMiAFszx1qclJRAxh4g4HOa5P8p9pNsjjQmqI8zlAe9dmHAA'
access_token = 'AA44484527396-mz8aVftwUMTtv1XKm9T070h9PkwDQvUxeG6PZ7KbAA'
access_secret = 'AA44pb1CQELQJ2G4y5SeTNvYID7h099QGj1IV1gucCtrZwgEPAA'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(20):
    # Process a single status
    print(status.text)

for status in tweepy.Cursor(api.user_timeline).items(10):
    print (status.text)	


#for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
#    process_or_store(status._json) 

#for friend in tweepy.Cursor(api.friends).items():
#    process_or_store(friend._json)

#for tweet in tweepy.Cursor(api.user_timeline).items():
#    process_or_store(tweet._json)

#def process_or_store(tweet):
#    print(json.dumps(tweet))

