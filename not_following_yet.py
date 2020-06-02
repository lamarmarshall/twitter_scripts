from potential_followers import get_potential_followers
from follow import get_who_i_follow

def not_followers(arr, potential_followers):
    res=[]
    for pfollow in potential_followers:
        if pfollow not in arr:
            res.append(pfollow)

    return res


def get_people_to_follow(hashtag="#veganos"):
    following = get_who_i_follow()
    pfollowers = get_potential_followers(hashtag)
    people_to_follow = not_followers(following, pfollowers)
    print("following: " + str ( len(following )) + " potential followers: " + str( len(pfollowers) ) + " people that follow back: " + str( len( people_to_follow ) ) )
    return people_to_follow

if __name__ == '__main__':
    print(get_people_to_follow())
    
