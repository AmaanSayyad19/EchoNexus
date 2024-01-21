from pymongo import MongoClient

def search_users(db):
    
    keyword = input("Enter a keyword to search for users: ").strip()
    regex = f"^{keyword} | {keyword}$"
    query = {'user.displayname': {'$regex': regex, '$options': 'i'}}

    # Using aggregation to avoid duplicates and project required fields
    pipeline = [
        {'$match': query},
        {'$group': {'_id': "$user.username", 'displayname': {'$first': "$user.displayname"}, 'location': {'$first': "$user.location"}}},
        {'$project': {'username': '$_id', 'displayname': 1, 'location': 1, '_id': 0}}
    ]

    results = list(db['tweets'].aggregate(pipeline))


    if not results:
        print("No users found with the given keyword.")
        return

    print("\nMatching Users:")
    for index, user in enumerate(results, start=1):
        location = user.get('location', 'NULL') if user.get('location') else 'NULL'
        print(f"{index}. Username: {user.get('username')}, Display Name: {user.get('displayname')}, Location: {location}")

    user_choice = input("\nEnter the number of a user to see more details or 'q' to quit: ")
    if user_choice.lower() == 'q':
        return

    try:
        selected_index = int(user_choice) - 1
        if 0 <= selected_index < len(results):
            selected_user = results[selected_index]['username']
            user_info = db['tweets'].find_one({'user.username': selected_user}, {'user': 1, '_id': 0})
            if user_info:
                print("\nSelected User Details:")
                for key, value in user_info['user'].items():
                    print(f"{key.capitalize()}: {value}")
            else:
                print("User details not found.")
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")


