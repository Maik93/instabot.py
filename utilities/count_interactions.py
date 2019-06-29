#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import instaloader
from instabot_py.persistence.sql import Persistence

here = os.path.abspath(os.path.dirname(__file__))

if len(sys.argv) == 1:
    print("Usage: ./count_interactions.py <your_instagram_username>")
    sys.exit()

USER = sys.argv[1]
PROFILE = USER

# load follower list from file
current_followers = [line.rstrip('\n') for line in open(os.path.join(here, "followers.txt"), 'r')]

# loader = instaloader.Instaloader()
#
# # Login method 1: ask password in terminal
# # loader.interactive_login(USER)
#
# # Login method 2: load session created with `instaloader -l <your_instagram_username>`
# loader.load_session_from_file(USER, filename=os.path.join(here, f"{USER}.instaloader-session"))
#
# loaded_profile = instaloader.Profile.from_username(loader.context, PROFILE)
#
# print(f'Fetching followers of profile {loaded_profile.username}.')
# followers = set(loaded_profile.get_followers())
#
# # print('Storing followers into file.')
# # with open('followers.txt', 'w') as f:
# #     for follower in followers:
# #         print(follower.username, file=f)
#
# current_followers = [follower.username for follower in followers]

db = Persistence(f'sqlite:///{PROFILE}.db', None)

users_interacted_with = db.get_all_interactions()

matured_followers = list(set(current_followers).intersection(users_interacted_with))
print(f"You've done {len(matured_followers)} new followers! It's {len(matured_followers)*.03}€, much wow!")
