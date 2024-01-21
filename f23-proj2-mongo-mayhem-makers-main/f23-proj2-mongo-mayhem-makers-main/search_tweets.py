from pymongo import MongoClient

def search_tweets(db):
    keywords = input("Enter keywords for searching tweets (separated by comma): ").strip().split(',')

    # MongoDB query using '$and' and '$regex' for the keywords (case insensitive)
    query = {'$and': [ {'content': {'$regex': keyword.strip(), '$options': 'i'}} for keyword in keywords ]}
    
    results = list(db['tweets'].find(query))

    if not results:
        print("No tweets found with the given keywords.")
        return

    print("\nMatching Tweets:")

    for index, tweet in enumerate(results, start=1):
        user = tweet.get('user', {}).get('username', 'N/A')
        print(f"{index}. ID: {tweet.get('_id')} \nDate: {tweet.get('date')} \nContent: {tweet.get('content')} \nUsername: {user}\n")

    while True:
        selection = input("Enter the number of a tweet to see more details or 'q' to quit: ")
        if selection.lower() == 'q':
            break
        
        try:
            selected_index = int(selection) - 1
            if 0 <= selected_index < len(results):
                tweet = results[selected_index]
                user = tweet.get('user', {})
                print("\nSelected Tweet Details:")
                print(f"ID: {tweet.get('_id')}")
                print(f"Date: {tweet.get('date')}")
                print(f"Content: {tweet.get('content')}")
                print(f"Username: {user.get('username', 'N/A')}")
                print(f"URL: {tweet.get('url')}")
                print(f"Reply Count: {tweet.get('replyCount')}")
                print(f"Retweet Count: {tweet.get('retweetCount')}")
                print(f"Like Count: {tweet.get('likeCount')}")
                print(f"Quote Count: {tweet.get('quoteCount')}")
                print(f"Conversation ID: {tweet.get('conversationId')}")
                print(f"Language: {tweet.get('lang')}")
                print(f"Source: {tweet.get('source')}")
                print(f"Source URL: {tweet.get('sourceUrl')}")
                print(f"Source Label: {tweet.get('sourceLabel')}")
                print(f"Media: {tweet.get('media')}")
                print(f"Retweeted Tweet: {tweet.get('retweetedTweet')}")
                print(f"Quoted Tweet: {tweet.get('quotedTweet')}")
                print(f"Mentioned Users: {tweet.get('mentionedUsers')}")
                print(f"Outlinks: {tweet.get('outlinks')}")
                print(f"TCO Outlinks: {tweet.get('tcooutlinks')}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
