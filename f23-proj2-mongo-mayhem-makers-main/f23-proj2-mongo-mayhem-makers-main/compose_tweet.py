from pymongo import MongoClient
import json
from datetime import datetime

# Function to compose a tweet
def compose_tweet(db, content):
    # Create a new tweet document
    tweet = {
        "content": content,
        "date": datetime.now(),
        "username": "291user",
        "id": "NULL",  # Add your tweet ID here
        "url": "NULL",  # Add your tweet URL here
        "user": {
            "username": "291user",
            "displayname": "User 291",  # Add your display name here
            "description": "NULL",  # Add your description here
            "followersCount": "NULL",  # Add your followers count here
            "friendsCount": "NULL",  # Add your friends count here
            "statusesCount": "NULL",  # Add your statuses count here
            "location": "NULL",  # Add your location here
            "verified": False,  # Change this to True if your account is verified
        },
        "replyCount": 0,
        "retweetCount": 0,
        "likeCount": 0,
        "quoteCount": 0,
        "lang": "en",
        "source": '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>',  # Change this to your source
    }

    tweet['date'] = tweet['date'].isoformat()

    # Insert the tweet into the database
    db.tweets.insert_one(tweet)
    print("Tweet posted successfully")

    # Save the tweet to a JSON file
    tweet.pop('_id', None)

    with open("tweet.json", "w") as f:
        json.dump(tweet, f)
