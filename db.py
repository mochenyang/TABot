import time
import pymongo

# connect to mongodb
dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = dbclient["TABot"]
conversation_col = mydb["conversation"]
user_col = mydb["user"]
thread_col = mydb["thread"]

# check if a user should have access
def check_user(username):
    if user_col.find_one({"x500": username}):
        return True
    else:  
        return False 

# store a conversation
def insert_conversation(user, thread, query, response):
    record = { "user": user, "thread": thread, "time": time.time(), "query": query, "response": response }
    _ = conversation_col.insert_one(record)


# store a thread
def insert_thread(thread, status):
    record = { "thread": thread , "status": status}
    _ = thread_col.insert_one(record)


# get all open threads and return thread ID in a list
def get_open_threads():
    open_threads = []
    for thread in thread_col.find({"status": "open"}):
        open_threads.append(thread["thread"])
    return open_threads


# update thread status
def update_thread(thread, newstatus):
    query = { "thread": thread }
    new_values = { "$set": { "status": newstatus } }
    thread_col.update_one(query, new_values)