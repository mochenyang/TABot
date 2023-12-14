import time
from openai import OpenAI
from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)

# connect to mongodb
dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = dbclient["TABot"]
mycol = mydb["test"]
user = "mochen"

# connect to openai
client = OpenAI()
thread = client.beta.threads.create()

def ask_assistant(user_input):
    # user input
    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = user_input
    )

    #thread_messages = client.beta.threads.messages.list(thread.id)
    #print(thread_messages.data)

    # run assistant
    run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = "asst_JfJJaCH0eWhN9bWK3CYq40ML"
    )

    # check run status
    while (run.status != "completed"):
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id = thread.id,
            run_id = run.id
        )

    # get assistant response
    response = client.beta.threads.messages.list(
        thread_id = thread.id
    )

    return response.data[0].content[0].text.value

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/get")
def get_response():    
    userText = request.args.get('msg')
    response = ask_assistant(userText)
    # record in database
    record = { "user": user, "thread": thread.id, "time": time.time(), "query": userText, "response": response }
    _ = mycol.insert_one(record)
    return response

if __name__ == "__main__":
    app.run()