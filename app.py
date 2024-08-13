import time
import os
from flask import Flask, render_template, request, redirect, url_for
from bot import *
from db import *

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")

@app.route("/")
def login_page():
    error = request.args.get('error')
    return render_template("login.html", error = error)

# handle login
@app.route("/login", methods = ["POST"])
def login():
    session['user_id'] = request.form['username']
    print(session['user_id'])
    if check_user(session['user_id']):
        # initialize a thread and store it in db
        thread_init()
        insert_thread(session['thread_id'], "open")
        return render_template("index.html")
    else:
        return redirect(url_for('login_page', error="Invalid x500. Please try again."))

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