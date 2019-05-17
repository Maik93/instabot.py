# Instabot utilities

## Ghost followers
Find out who follows you but doesn't give you any likes.

Before the first usage, you have to produce an Instaloader session file. Do this:

```sh
instaloader -l <your_instagram_username>
# enter your Instagram password
cp /tmp/.instaloader-<user>/session-<your_instagram_username> \
   ./<your_instagram_username>.instaloader-session
```

Then use it as follows:

```sh
./ghost_followers.py <your_instagram_username>
```
