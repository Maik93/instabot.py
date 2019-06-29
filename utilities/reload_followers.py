#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import instaloader
from instabot_py.persistence.sql import Persistence, Follower

here = os.path.abspath(os.path.dirname(__file__))

if len(sys.argv) == 1:
    print("Usage: ./list_all_followers.py <your_instagram_username>")
    sys.exit()

USER = sys.argv[1]
PROFILE = USER

loader = instaloader.Instaloader()

# Login method 1: ask password in terminal
# loader.interactive_login(USER)

# Login method 2: load session created with `instaloader -l <your_instagram_username>`
loader.load_session_from_file(USER, filename=os.path.join(here, f"{USER}.instaloader-session"))

profile = instaloader.Profile.from_username(loader.context, PROFILE)

print(f'Fetching followees of profile {profile.username}.')
followees = set(profile.get_followers())

# print('Storing followees into file.')
# with open('followees.txt', 'w') as f:
#     for followee in followees:
#         print(f"{followee.userid}, {followee.username}", file=f)

db = Persistence(f'sqlite:///{PROFILE}.db', None)

print('Clearing followees database...')
db._session.query(Follower).delete()
db._session.commit()

print('Inserting current followees into database...')
for f in followees:
    db.insert_username(f.userid, f.username)

print('Everything done!')
db._session.close()
