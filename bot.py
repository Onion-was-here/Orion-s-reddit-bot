import praw
import config
import time
import os


def bot_login():

    #login to reddit using user details from config.py

    r = praw.Reddit(username = config.username,
                password =  config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Onionsoup's bot V0.1")

    print('Login successful')

    return r

def run_bot(r,reply_id):

    # searches for a specific string in a subreddit
    # and replies to it with text of your choosing
        for comment in r.subreddit('test').comments(limit = 50):
            try:
                if "item" in comment.body and comment.id not in reply_id and comment.author != r.user.me():
                    submission = comment.submission
                    print("commentfound!")
                    if submission.locked:
                        print("This cant be replied to because the submission is locked")
                    else:
                        if not comment.locked:
                            try:
                                comment.reply(body="Text")
                                print("replied")
                                
                            except Exception as e:
                                if "RATELIMIT" in e.error_type:
                                    print("Rate limit reached. Sleeping for 10 minutes.")
                                    time.sleep(600)  # Sleep for 10 minutes
                                else:
                                    raise
                            
            except Exception as e:
                print(f"An error occurred: {e}")
                #appents comment id in order to remember
                # which comments have been replied to

                reply_id.append(comment.id)

                # adds newline character ot the comment id

                with open ("comment_id.txt", "a") as f:
                    f.write(comment.id + "\n")

def open_saved_comment_id():

    #creates empty file if reply_id does not already exist

    if not os.path.isfile("comment_id.txt"):
        reply_id = []

    #reads through comment id and splits them whenever
    #new line character is read

    with open("comment_id.txt", "r") as f:
        reply_id = f.read()
        reply_id = reply_id.split("\n")
        reply_id = list(filter(None, reply_id))

        return reply_id


reply_id= open_saved_comment_id()

r = bot_login()

#running the bot while true

while True:
    run_bot(r,reply_id)


