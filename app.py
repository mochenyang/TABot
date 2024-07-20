import time
from flask import Flask, render_template, request
from bot import *
#import pymongo

app = Flask(__name__)

# connect to mongodb
#dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = dbclient["TABot"]
#mycol = mydb["test"]
#user = "mochen"


@app.route("/")
def home():
    # initialize a thread
    thread_init()
    return render_template("index.html")

@app.route("/get")
def get_response():    
    userText = request.args.get('msg')
    response = ask_assistant(userText)
    # record in database
    #record = { "user": user, "thread": thread.id, "time": time.time(), "query": userText, "response": response }
    #_ = mycol.insert_one(record)
    return response

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run()