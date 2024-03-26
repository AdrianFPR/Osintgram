# Note: A username and password need to be provided in the credentials.ini file found in Osintgram/config
# Only accounts which are viewable (being followed by or are public to) the account whose credentials have been provided can be scraped
from src.Osintgram import Osintgram # An api class which is used to obtain desired information


def my_followers():
    api = Osintgram(target='afpr8', is_file=False, is_json=False, is_cli='followers', output_dir=None, clear_cookies=False)
    follower_info = list(api.get_followers()) # Should return a list of triples
    followers = [x['username'] for x in follower_info] # Extracting just the usernames from the triples
    return followers


def who_i_follow():
    api = Osintgram(target='afpr8', is_file=False, is_json=False, is_cli='followings', output_dir=None, clear_cookies=False)
    followings_info = list(api.get_followings()) # Should return a list of triples
    followings = [x['username'] for x in followings_info] # Extracting just the usernames from the triples
    return followings


def not_following_me_back():
    i_follow = list(who_i_follow())
    follows_me = list(my_followers())
    not_following_me_back = []
    for i in i_follow:
        if i not in follows_me:
            not_following_me_back.append(i)
    return not_following_me_back

def who_am_i_not_following_back():
    i_follow = list(who_i_follow())
    follows_me = list(my_followers())
    who_am_i_not_following_back = []
    for i in follows_me:
        if i not in i_follow:
            who_am_i_not_following_back.append(i)
    return who_am_i_not_following_back

print(not_following_me_back())