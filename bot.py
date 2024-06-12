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
    
    for comment in r.subreddit('test').comments(limit=25) :
            if "dog" in comment.body and comment.id not in reply_id and comment.author != r.user.me():
                print("dog found!")
                comment.reply("woof woof")
            print("replied")
            
            #appents comment id in order to remember
            # which comments have been replied to
            
            reply_id.append(comment.id)
            
            # adds newline character ot the comment id
            
            with open ("comment_id.txt", "a") as f:
                f.write(comment.id + "\n")
                
    #bot sleeps for a set duration
    
    time.sleep(15)

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
