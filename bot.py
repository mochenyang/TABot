import time
from openai import OpenAI
from flask import session

# global variables
client = OpenAI(
    organization="org-OLj35i3NXxpSuuOGH1a1HxNm",
    project="proj_GB1WRZh96Njv1a7nASGFgcZT")

assistant_id = "asst_81TxmQ0vUYW0zxBLYaBoXSf8"

# initialize a conversation thread and store its ID in session
def thread_init():
    thread = client.beta.threads.create()
    session['assistant_id'] = assistant_id
    session['thread_id'] = thread.id

# conversation
def ask_assistant(user_input):
    # user input
    message = client.beta.threads.messages.create(
        thread_id = session['thread_id'],
        role = "user",
        content = user_input
    )

    #thread_messages = client.beta.threads.messages.list(thread.id)
    #print(thread_messages.data)

    # run assistant
    run = client.beta.threads.runs.create(
        thread_id = session['thread_id'],
        assistant_id = session['assistant_id']
    )

    # check run status
    while (run.status != "completed"):
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            thread_id = session['thread_id'],
            run_id = run.id
        )

    # get assistant response
    response = client.beta.threads.messages.list(
        thread_id = session['thread_id']
    )

    return response.data[0].content[0].text.value

# TBD: delete thread for cleanup
def thread_delete():
    pass