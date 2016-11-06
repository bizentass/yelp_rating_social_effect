import json


class User:

    def __init__(self):
        self.user_id = "null"
        self.review_set = ()
        self.review_dict = {}
        self.user_friends_list = []
        self.user_friends_dict = {}

user_file = open("yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_user.json", "r")
review_file = open("yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json", "r")

target_user_dict = {}
user_id_reviews_dict = {}
custom_user_list = []

for user_line in user_file.readlines():
    user_object = json.loads(user_line)
    if len(user_object['friends']) >= 5:
        userObj = User()
        userObj.user_id = user_object['user_id']
        userObj.user_friends_list = user_object['friends']
        target_user_dict[user_object['user_id']] = userObj

for review_line in review_file.readlines():
    review_object = json.loads(review_line)
    if review_object['user_id'] in target_user_dict.keys():
        userObj = target_user_dict.get(review_object['user_id'])
        review_dict = userObj.review_dict
        review_dict.setdefault('review', []).append({
            'businessId': review_object['business_id'],
            'stars': review_object['stars']
        })
        userObj.review_dict = review_dict
        target_user_dict[review_object['user_id']] = userObj

for userId in target_user_dict.keys():
    userObj = target_user_dict.get(userId)
    userFriendsList = []
    for friendId in userObj.user_friends_list:
        friendObj = target_user_dict.get(friendId)
        userFriendsList.append(friendObj)
    userObj.user_friends_list = userFriendsList
    target_user_dict[userId] = userObj
