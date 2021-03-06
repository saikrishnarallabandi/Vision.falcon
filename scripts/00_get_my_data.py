#!usr/bin/env python
# Program to mine data from your own facebook account

import json
import facebook
import os

token = os.environ.get('FACEBOOK_TOKEN')
id = os.environ.get('MY_GROUP_ID')

def main():
    graph = facebook.GraphAPI(token)
    #fields = ['first_name', 'location{location}','email','link']
    profile = graph.get_object(
        'me', fields='first_name,location,link,email,groups')
    # return desired fields
    print(json.dumps(profile, indent=5))
    group = graph.get_object(id=id)
    print(json.dumps(group, indent=1))
    #print(id)
    id = group['id']
    graph.put_photo(album_path=id + '/photos', image=open('temp.png', 'rb'), message='Look at this!')

    print(group)

if __name__ == '__main__':
    main()
