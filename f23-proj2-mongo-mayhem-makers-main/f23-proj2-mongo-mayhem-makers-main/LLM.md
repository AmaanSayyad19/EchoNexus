We used AI Agents such as ChatGPT and BingAI.

# Steps to Build load-json.py
**This script is responsible for loading JSON data into a MongoDB collection.**
Here’s the step-by-step process:

1. **Import Required Libraries:** Import the necessary Python libraries `(sys, json, pymongo).`
2. **Command Line Arguments:** Parse command line arguments to obtain the JSON file name and port number.
3. **MongoDB Connection:** Establish a connection to the MongoDB server running on the provided port.
4. **Database and Collection Access:** Access the `291db` database and the `tweets` collection.
5. **Collection Handling:** If the ‘tweets’ collection already exists, drop it.
6. **JSON File Processing:** Open the JSON file and read it line by line.
7. **JSON Parsing and Insertion:** For each line, parse it as a JSON object and add it to a batch. When the batch size reaches a certain limit (e.g., 1000), insert the batch into the ‘tweets’ collection using insert_many().
8. **Remaining Tweets Insertion:** If there are any remaining tweets in the batch after all lines in the file have been processed, insert them into the collection.
9. **Connection Closure:** Close the connection to the MongoDB server.
    
# Steps to write the main.py
**This is the main script of the application. Here are the steps:*

1. **Import Libraries and Modules:** Import necessary Python libraries and modules `(pymongo, search_tweets, search_users, list_top_tweets, list_top_users, compose_tweet)`.
2. **Command Line Arguments:** Parse command line arguments to get the port number.
3. **MongoDB Connection:** Establish a connection to the MongoDB server running on the specified port.
4. **Database Access:** Access the ‘291db’ database.
5. **Menu Display:** Display a menu to the user with options to search for tweets/users, list top tweets/users, compose a tweet, or exit.
6. **User Choice Handling:** Depending on the user’s choice, call the appropriate function from the imported modules.
7. **Loop Until Exit:** Repeat steps 5-6 until the user chooses to exit.

# Steps to Write the search_tweets Function
1. Prompt for User Input: Inside the function, prompt the user to enter keywords for searching tweets. The keywords should be separated by commas.

2. **Construct the Query:** Construct a MongoDB query using the ‘$and’ and ‘$regex’ operators for the keywords. The ‘$regex’ operator allows for case-insensitive matching.
3. **User:** "Here is the format of a tweet in a database:
     >{"url": "https://twitter.com/ShashiRajbhar6/status/1376739399593910273", "date": "2021-03-30T03:33:46+00:00", "content": "Support \ud83d\udc47\n\n#FarmersProtest", "renderedContent": "Support \ud83d\udc47\n\n#FarmersProtest", "id": 1376739399593910273, "user": {"username": "ShashiRajbhar6", "displayname": "Shashi Rajbhar", "id": 1015969769760096256, "description": "Satya presan \ud83e\udd14ho Sakta but prajit\ud83d\udcaa nhi\njhuth se samjhauta kbhi nhi\nJai Shree Ram \ud83d\udd49 \ud83d\ude4f\ud83d\udd49 followed by hon'ble @ArunrajbharSbsp", "rawDescription": "Satya presan \ud83e\udd14ho Sakta but prajit\ud83d\udcaa nhi\njhuth se samjhauta kbhi nhi\nJai Shree Ram \ud83d\udd49 \ud83d\ude4f\ud83d\udd49 followed by hon'ble @ArunrajbharSbsp", "descriptionUrls": [], "verified": false, "created": "2018-07-08T14:44:03+00:00", "followersCount": 1788, "friendsCount": 1576, "statusesCount": 14396, "favouritesCount": 26071, "listedCount": 1, "mediaCount": 254, "location": "Azm Uttar Pradesh, India", "protected": false, "linkUrl": null, "linkTcourl": null, "profileImageUrl": "https://pbs.twimg.com/profile_images/1354331299868237825/eDzdhZTD_normal.jpg", "profileBannerUrl": "https://pbs.twimg.com/profile_banners/1015969769760096256/1613727783", "url": "https://twitter.com/ShashiRajbhar6"}, "outlinks": [], "tcooutlinks": [], "replyCount": 0, "retweetCount": 0, "likeCount": 0, "quoteCount": 0, "conversationId": 1376739399593910273, "lang": "en", "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>", "sourceUrl": "http://twitter.com/download/android", "sourceLabel": "Twitter for Android", "media": null, "retweetedTweet": null, "quotedTweet": null, "mentionedUsers": null}<br>

How to search for tweets that contain all the keywords entered by a user which is case insensitive"
**Agent**: 
>To search for tweets that contain all the keywords entered by a user in a case-insensitive manner, you can use MongoDB’s $and and $regex operators. Here’s a Python code snippet that demonstrates this:<br>
query = {'$and': [ {'content': {'$regex': keyword.strip(), '$options': 'i'}} for keyword in keywords ]}
   
5. **Execute the Query:** Execute the query on the ‘tweets’ collection in the database and retrieve the results. Convert the results to a list.

6. **Handle No Results:** If no tweets are found with the given keywords, inform the user and return from the function.

7. **Display Matching Tweets:** If matching tweets are found, display the ID, date, content, and username of each tweet.

8. **Handle User Selection:** Allow the user to enter the number of a tweet to see more details. If the user enters ‘q’, break the loop and return from the function.

9. **Display Tweet Details:** If the user enters a valid number, display all fields of the selected tweet.

# Steps for `search_users`
1. **Import Required Libraries:** Import the necessary Python libraries. In this case, you need to import the pymongo library for MongoDB operations.

2. **Define the connect_to_mongodb Function:** Define a function named connect_to_mongodb that takes a port parameter. This function establishes a connection to the MongoDB server running on the specified port and returns the MongoDB client.

3. **Define the search_users Function:** Define a function named search_users that takes a db parameter representing the MongoDB database.

4. **Prompt for User Input:** Inside the search_users function, prompt the user to enter a keyword for searching users by display name or location.

5. **Construct the Query:** Construct a MongoDB query using the ‘$or’ and ‘$regex’ operators for the keyword. The ‘$regex’ operator allows for case-insensitive matching.
6. User: what is the alternative for like operator (sql) in mongodb<br>
Agent:
>In MongoDB, the equivalent of the SQL LIKE operator is achieved using regular expressions with the $regex operator1. Here’s an example:<br>
db.collection.find({ "field": { "$regex": pattern, "$options": "i" } })
In this example, field is the name of the field you want to search, and pattern is the pattern you want to match. The $options: 'i' part makes the search case insensitive, similar to the SQL LIKE operator1.<br><br>Remember, MongoDB’s regular expressions are more powerful than SQL’s LIKE operator. With regular expressions, you can create any pattern that you imagine1. For more information on regular expressions, you can refer to the Regular Expressions documentation on MDN1. I hope this helps! Let me know if you have any other questions.

7. **Construct the Aggregation Pipeline:** Construct a MongoDB aggregation pipeline that matches the query, groups the tweets by username, gets the first display name and location for each group, and projects the required fields.

8. **Execute the Aggregation Pipeline:** Execute the pipeline on the ‘tweets’ collection in the database and retrieve the results. Convert the results to a list.

9. **Handle No Results:** If no users are found with the given keyword, inform the user and return from the function.

10. **Display Matching Users:** If matching users are found, display the username, display name, and location of each user.

11. **Handle User Selection:** Allow the user to enter the number of a user to see more details. If the user enters ‘q’, break the loop and return from the function.

12. **Call the get_user_info Function:** If the user enters a valid number, call the get_user_info function with the username of the selected user.

`get_user_info` Function
1. **Define the get_user_info Function:** Define a function named get_user_info that takes a db parameter representing the MongoDB database and a username parameter representing the username of the user.

2. **Find the User:** Find the tweet with the given username in the ‘tweets’ collection in the database.

3. **Check if the User Exists:** If the tweet exists and has a ‘user’ field, get the user information.

4. **Display the User Information:** Display all fields of the user information.

# Steps to Write the `list_top_users` and `get_user_info` Functions

`list_top_users` Function:
1. **Prompt for User Input:** Inside the list_top_users function, prompt the user to enter the number of top users to list.
2 **Construct the Aggregation Pipeline:** Construct a MongoDB aggregation pipeline that groups the tweets by username, gets the first display name and followers count for each group, sorts the groups by followers count in descending order, and limits the results to the top ‘n’ users.
3. User: Write a MongoDB aggregation query that groups tweets by username, and for each group, retrieves the display name and follower count of the first tweet in the group. The output documents should have fields for the username (_id), display name, and follower count<br>
Agent:
>{"$group": {"_id": "$user.username", "displayname": {"$first": "$user.displayname"}, "followersCount": {"$first": "$user.followersCount"}}}

User: Write a MongoDB aggregation query that sorts the documents in descending order based on the ‘followersCount’ field.
Agent:
>{"$sort": {"followersCount": -1}}
4. **Execute the Aggregation Pipeline:** Execute the pipeline on the ‘tweets’ collection in the database and retrieve the results. Convert the results to a list.
5. **Display the Top Users:** Display the rank, username, display name, and followers count of each top user.
6. **Handle User Selection:** Allow the user to enter the number of a user to see more details. If the user enters ‘q’, break the loop and return from the function.

`get_user_info` Function
1. **Find the User:** Find the tweet with the given username in the ‘tweets’ collection in the database.
2. **Check if the User Exists:** If the tweet exists and has a ‘user’ field, get the user information.
3. **Display the User Information:** Display all fields of the user information.

# Steps to Write the list_top_tweets Function
1. **Import Required Libraries:** Import the necessary Python libraries. In this case, you need to import the pymongo library for MongoDB operations.

2. **Define the connect_to_mongodb Function:** Define a function named connect_to_mongodb that takes a port parameter. This function establishes a connection to the MongoDB server running on the specified port and returns the MongoDB client.

3. **Define the list_top_tweets Function:** Define a function named list_top_tweets that takes a db parameter representing the MongoDB database.

4. **Prompt for User Input:** Inside the list_top_tweets function, prompt the user to choose a field for ranking the top tweets and to enter the number of top tweets to display.

5. **Map User Choice to Field:** Map the user’s choice to the corresponding field in the tweet documents.

6. **Check if Field Exists:** Check if the chosen field exists in the ‘tweets’ collection in the database. If not, inform the user and return from the function.

7. **Construct the Query:**Construct a MongoDB query that finds tweets where the chosen field exists.
**User:** Write a MongoDB query that retrieves the top n documents from the ‘tweets’ collection where a specific field exists. The documents should be sorted in descending order based on the field
**Agent:**
>query = list(db.tweets.find({field: {'$exists': True}}).sort(field, -1).limit(n))

9. **Execute the Query:**
   Execute the query on the ‘tweets’ collection in the database, sort the results by the chosen field in descending order, limit the results to the top ‘n’ tweets, and retrieve the results. Convert the results to a list.

10. **Display the Top Tweets:**
   Display the rank, ID, date, username, chosen field, and content of each top tweet.

11. **Handle User Selection:**
    Allow the user to enter the number of a tweet to see more details. If the user enters ‘q’, break the loop and return from the function.

12. **Display Tweet Details:**
    If the user enters a valid number, display all fields of the selected tweet.

# Steps for Compose_tweets.py

1. **Take Input**
2. **Initialise all subfields as Null if they are not specified**
3. **use .isoformat() to enforce the correct date time format for a new tweet**
4. **use insert_one to insert the new tweet to the database**
