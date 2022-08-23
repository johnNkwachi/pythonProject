users = [
    {
    'name': 'Hadiza', 'age': 21, 'gender': 'female',
        'username': 'deeza', 'verified': True,
        'tweet':[
            { 'content': 'Po for president',  'likes': 222, 'retweets': 500},
            { 'content': 'Atiku is our man', 'likes': 33, 'retweet': 20}
        ]
    },
       {
    'name': 'Dorris', 'age': 17, 'gender': 'female',
        'username': 'deeza', 'verified': False,
        'tweet':[
            { 'content': 'I love Chimamanda',  'likes': 222, 'retweets': 500},
            { 'content': 'Feminism is the goal', 'likes': 33, 'retweet': 20}
           ]
    },

   {
    'name': 'Derrick', 'age': 29, 'gender': 'male',
        'username': 'deeza', 'verified': False,
        'tweet':[
            { 'content': 'Po for president',  'likes': 222, 'retweets': 500},
            { 'content': 'Atiku is our man', 'likes': 33, 'retweet': 20}
]
}
    ]

print(users)
no_of_users = {user ['username'] for user in users}
female_users = [user['name'] for user in users if users if user['gender'] == 'female']
#inactive_users = [user for user in users if len(user['tweets'])==0]
users_age = [user['age'] for user in users]
user_name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
average_age_of_users = round(sum([user['age'] for user in users]) / len(users))
print(average_age_of_users)
#print(inactive_users)
print(female_users)
print(users_age)
print(user_name_and_age)