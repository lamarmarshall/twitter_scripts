
def not_following_me():
    file_following = open("following.txt", 'r')
    file_followers = open("followers.txt", 'r')

    followers = file_followers.read().splitlines()
    following = file_following.read().splitlines()
    followers.sort()
    following.sort()

    file_following.close()
    file_followers.close()

    return list(set(following) - set(followers))



