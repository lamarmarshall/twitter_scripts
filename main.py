
from twitter_scraper import get_tweets, Profile
import twint
import sys
import io

if __name__ == '__main__':
    #for tweets in get_tweets('basadaplanta', pages=1):
    #    print(tweets['text'])
    #user = Profile('basadaplanta')
    #print(user.to_dict())


    #user = twint.Config()
    #user.Username = "basadaplanta"

    #twint.run.Following(user)
    for tweets in get_tweets('#vegano'):
        user = Profile(tweets['username'])
        try:
            if user.following_count == user.followers_count or user.following_count >= user.followers_count:
                print(tweets['username'] + " followers_count: "+ str( user.followers_count ) + " following_count: " + str( user.following_count) )
        except :
            pass
    
  


    