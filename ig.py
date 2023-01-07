import json


def parse_json(json_file, str_):
    following_set = set()
    for user in json_file[str_]:
        following_set.add(user['string_list_data'][0]['value'])
    return following_set


try:
    with open("following.json", "r") as following:
        following_json = json.load(following)
        following_set = parse_json(following_json, 'relationships_following')

    with open("followers.json", "r") as followers:
        followers_json = json.load(followers)
        followers_set = parse_json(followers_json, 'relationships_followers')

    not_following = following_set.difference(followers_set)

    for user in not_following:
        print(user)

except IOError:
    print("Error opening JSON file")
except json.JSONDecodeError:
    print("Error parsing JSON file")
