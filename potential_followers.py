import sys
from twitter_scraper import get_tweets, Profile


def get_potential_followers(tag, pages=2):
    pfollowers = []
    for tweets in get_tweets(tag, pages):
            user = Profile(tweets['username'])
            try:
                if user.following_count == user.followers_count or user.following_count >= user.followers_count:
                    print(tweets['username'] + " followers_count: "+ str( user.followers_count ) + " following_count: " + str( user.following_count) )
                    pfollowers.append(tweets['username'] )
            except :
                pass
    return pfollowers

if __name__ == '__main__':
    arg = "#vegano"
    try:
        if sys.argv[1] != None :
            arg = str( sys.argv[1] )
    except IndexError:
        pass

    print(arg)
    pfollow = get_potential_followers(arg, 1)
    print(pfollow)


