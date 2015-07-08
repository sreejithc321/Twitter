import twitter
import json
from config1 import*

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

WORLD = 1
INDIA = 23424848
# US = 23424977

world_trends = twitter_api.trends.place(_id=WORLD)
india_trends = twitter_api.trends.place(_id=INDIA)
print json.dumps(world_trends, indent=1)
print json.dumps(india_trends, indent=1)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
india_trends_set = set([trend['name'] for trend in india_trends[0]['trends']]) 
common_trends = world_trends_set.intersection(india_trends_set)
print common_trends
