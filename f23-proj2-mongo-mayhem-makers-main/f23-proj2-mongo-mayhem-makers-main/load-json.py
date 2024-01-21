import sys
import json
from pymongo import MongoClient, InsertOne
from pymongo.errors import ConnectionFailure
# import time


# command line argument parsing
if len(sys.argv) != 3:
    print("Usage: python load-json.py [JSON_FILE] [PORT_NUMBER]")
    sys.exit(1)

json_file = sys.argv[1]
port_number = int(sys.argv[2])

# start_time = time.time()

# connecting to mongoDB
try:
    client = MongoClient('localhost', port_number)
    print("Connected successfully to MongoDB")
except ConnectionFailure:
    print("Could not connect to MongoDB")
    sys.exit(1)

# creating or accessing the database or collection
db = client['291db']
tweets_collection = db['tweets']

# drop existing if exists
if 'tweets' in db.list_collection_names():
    tweets_collection.drop()
    print("Existing 'tweets' collection dropped")

# Loading JSON Data and Insert into Collection in Batches
try:
    with open(json_file, 'r') as file:
        batch_size = 5000  # or any number you prefer
        batch = []
        for line in file:
            try:
                tweet = json.loads(line)
                batch.append(tweet)
                if len(batch) == batch_size:
                    tweets_collection.insert_many(batch)
                    batch = []
            except json.JSONDecodeError:
                print("Error decoding JSON")

        # Insert any remaining tweets
        if batch:
            tweets_collection.insert_many(batch)

    print("Data loaded successfully into MongoDB")
    
    # Create index on 'content' field after all tweets have been inserted
    tweets_collection.create_index('user.username')
    tweets_collection.create_index('user.displayname')
    tweets_collection.create_index('user.location')
    tweets_collection.create_index('content')
    tweets_collection.create_index('date')
    tweets_collection.create_index('username')
    tweets_collection.create_index('user.location')
    tweets_collection.create_index('user.followersCount')
    
except FileNotFoundError:
    print(f"File {json_file} not found")

# closing the connection
client.close()
# end_time = time.time()
# runtime = end_time - start_time
# print(f"Runtime: {runtime} seconds")
