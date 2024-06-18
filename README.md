# Orion-s-reddit-bot
A basic bot that uses praw in order to reply to comments

You will alsow need to craete a config.py file in order to import the user details including the clietn secret and id

This bot is programmed to be used on r/test so in order to use it on other subreddits for purposes other than just a simple "bark" you will need to make nessacary changes


#Troubleshooting 

Often times there will be a rate limiter that will put the bot to sleep for 10 mins

```praw.exceptions.RedditAPIException: RATELIMIT: "Looks like you've been doing that a lot. Take a break for X minutes.```

# Fix 

```if "RATELIMIT" in e.error_type:
   print("Rate limit reached. Sleeping for 10 minutes.")
   time.sleep(600)  # Sleep for 10 minutes ```
