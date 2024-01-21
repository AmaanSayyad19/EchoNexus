from pymongo import MongoClient

def list_top_users(db):
    n = int(input("Enter the number of top users to list: "))
    # Get top n users based on followersCount
    collection = db["tweets"]

    pipeline = [
    {'$sort': {'user.followersCount': -1}},
    {'$group': {'_id': "$user.username", 'displayname': {'$first': "$user.displayname"}, 'location': {'$first': "$user.location"}, 'followersCount': {'$first': "$user.followersCount"}}},
    {'$project': {'username': '$_id', 'displayname': 1, 'location': 1, 'followersCount': 1}},
    {'$sort': {'followersCount': -1}},
    {'$limit': n}
]

    top_users = list(db['tweets'].aggregate(pipeline))

    # Iterate over the top users
    for i, user in enumerate(top_users, 1):
        # Print the rank, username, displayname, and followersCount
        print()
        print(f"{i}. Username: {user['_id']}")
        print(f"Displayname: {user['displayname']}")
        print(f"FollowersCount: {user['followersCount']}")

    while True:
        # print("\nEnter the number of the username to see more details or 'q' to quit.")
        selection = input("\nEnter the number of a user to see more details or 'q' to quit: ")
        if selection.lower() == 'q':
            break

        try:
            selected_index = int(selection) - 1
            if 0 <= selected_index < len(top_users):
                selected_user = top_users[selected_index]['username']
                get_user_info(db, selected_user)
            else:
                print("Invalid selection. Please enter a number between 1 and " + str(len(top_users)))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_user_info(db, username):
    user = db['tweets'].find_one({'user.username': username})
    
    if user:
        user_info = user['user']
        print(f"Username: {user['user']['username']}")
        print(f"Displayname: {user['user']['displayname']}")

    
        print(f"ID: {user_info['id']}")
        print(f"Description: {user_info['description']}")
        print(f"Verified: {user_info['verified']}")
        print(f"Created: {user_info['created']}")
        print(f"FollowersCount: {user_info['followersCount']}")
        print(f"FriendsCount: {user_info['friendsCount']}")
        print(f"StatusesCount: {user_info['statusesCount']}")
        print(f"FavouritesCount: {user_info['favouritesCount']}")
        print(f"ListedCount: {user_info['listedCount']}")
        print(f"MediaCount: {user_info['mediaCount']}")
        print(f"Location: {user_info['location']}")
        print(f"Protected: {user_info['protected']}")
        print(f"Profile Image URL: {user_info['profileImageUrl']}")
        print(f"Profile Banner URL: {user_info['profileBannerUrl']}")
        print(f"URL: {user_info['url']}")
    else:
        print("User not found.")
