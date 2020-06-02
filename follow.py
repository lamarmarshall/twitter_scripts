
def get_my_followers():
    file_followers = open("followers.txt", 'r')
    followers = file_followers.read().splitlines()
    file_followers.close()
    return followers

def get_who_i_follow():
    file_following = open("following.txt", 'r')
    following = file_following.read().splitlines()
    following.sort()
    file_following.close()
    return following