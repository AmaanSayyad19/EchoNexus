from pymongo import MongoClient
import compose_tweet
import list_top_tweets
import list_top_users
import search_users
import search_tweets
import sys

def connect_to_mongodb(port):
    try:
        client = MongoClient('localhost', port)
        print("Connected successfully to MongoDB")
        return client['291db']
    except Exception as e:
        print(f"Could not connect to MongoDB: {e}")
        return None
    
def logged_in_menu(db):
    while True:
        try:
            print("1. Search Tweets")
            print("2. Search For Users")
            print("3. List Top Tweets")
            print("4. List Top Users")
            print("5. Compose A tweet")
            print("6. Exit\n")
            choice = input("Choose an option: ")
            if choice == "1":
                search_tweets.search_tweets(db)  # Assuming you have a function named search_tweets in mysearch_users
            elif choice == "2":
                search_users.search_users(db)
            elif choice == "3":
                list_top_tweets.list_top_tweets(db)
            elif choice == "4":
                list_top_users.list_top_users(db)
            elif choice == "5":
                tweet_content = input("Enter your tweet content: ")
                compose_tweet.compose_tweet(db, tweet_content)
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.\n")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <port_number>")
        return

    port_number = int(sys.argv[1])
    db = connect_to_mongodb(port_number)
    if db is not None:
        logged_in_menu(db)


if __name__ == "__main__":
    main()
