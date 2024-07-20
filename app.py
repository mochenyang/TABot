import time
from flask import Flask, render_template, request
from bot import *
from db import *

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route("/")
def home():
    # initialize a thread and store it in db
    thread_init()
    insert_thread(session['thread_id'], "open")
    # store user ID in session (update later based on sso)
    session['user_id'] = "yang3653"
    
    return render_template("index.html")

@app.route("/get")
def get_response():
    userText = request.args.get('msg')
    response = ask_assistant(userText)
    # store in database
    insert_conversation(session['user_id'], session['thread_id'], userText, response)
    return response

@app.route("/tab_close", methods=["POST"])
def handle_tab_close():
    # Mark the user's thread as closed
    thread_id = session['thread_id']
    if thread_id:
        update_thread(thread_id, "closed")
    return '', 204  # Return an empty response


if __name__ == "__main__":
    app.run()