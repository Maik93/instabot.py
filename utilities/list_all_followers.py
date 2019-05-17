#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import instaloader

if len(sys.argv) == 1:
    print("Usage: ./list_all_followers.py <your_instagram_username>")
    sys.exit()

USER = sys.argv[1]
PROFILE = USER

loader = instaloader.Instaloader()

# Login method 1: ask password in terminal
# loader.interactive_login(USER)

# Login method 2: load session created with `instaloader -l <your_instagram_username>`
here = os.path.abspath(os.path.dirname(__file__))
loader.load_session_from_file(USER, filename=os.path.join(here, f"{USER}.instaloader-session"))

profile = instaloader.Profile.from_username(loader.context, PROFILE)

print(f'Fetching followers of profile {profile.username}.')
followers = set(profile.get_followers())

print('Storing followers into file.')
with open('followers.txt', 'w') as f:
    for follower in followers:
        print(follower.username, file=f)
