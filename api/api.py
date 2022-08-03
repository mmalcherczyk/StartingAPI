import json

def read_user():
    with open('data/users.json') as stream:
        users = json.load(stream)
    
    return users

def read_photos():
    with open('data/photos.json') as photos:
        photos = json.load(photos)




