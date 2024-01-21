from pymongo import MongoClient

def list_top_tweets(db):
    print("Choose a field for ranking the top tweets:")
    print("1. Retweet Count")
    print("2. Like Count")
    print("3. Quote Count")
    field_choice = input("Enter your choice (1-3): ")

    field_map = {'1': 'retweetCount', '2': 'likeCount', '3': 'quoteCount'}
    field = field_map.get(field_choice)

    if not field:
        print("Invalid choice. Exiting the top tweets listing.")
        return

    try:
        n = int(input("Enter the number of top tweets to display: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Adjusted query to use count_documents
    if db.tweets.count_documents({field: {'$exists': True}}) == 0:
        print(f"No tweets found for the given criteria.")
        return

    query = list(db['tweets'].find({field: {'$exists': True}}).sort(field, -1).limit(n))

    print(f"\nTop {n} Tweets based on {field}:\n")
    for index, tweet in enumerate(query, start=1):
        user_data = tweet.get('user')
        username = user_data.get('username') if user_data else None
        print(f"{index}. ID: {tweet.get('_id')}\n   Date: {tweet.get('date')}\n   Username: {username}\n   {field}: {tweet.get(field)}\n   Content: {tweet.get('content')}")
        print("")
        
    while True:
        selection = input("\nEnter the number of a tweet to see more details or 'q' to quit: ")
        if selection.lower() == 'q':
            break
        
        try:
            selected_index = int(selection) - 1
            if 0 <= selected_index < len(query):
                tweet = query[selected_index]
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
                print("\nUser Details:")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
