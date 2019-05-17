# Instabot utilities

Before the first usage, you have to produce an Instaloader session file. Do this:

```sh
instaloader -l <your_instagram_username>
# enter your Instagram password
cp /tmp/.instaloader-<user>/session-<your_instagram_username> \
   ./<your_instagram_username>.instaloader-session
```

## Ghost followers
Find out who follows you but doesn't give you any likes.

```sh
./ghost_followers.py <your_instagram_username>
```

## List all followers
Get a list of all your followers.

```sh
./list_all_followers.py <your_instagram_username>
```
