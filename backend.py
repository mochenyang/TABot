# backend only - for testing purposes

import os
import time
from openai import OpenAI

client = OpenAI()

'''
user_input = input("Enter your prompt: ")
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": user_input}
  ]
)

print(response.choices[0].message.content)
'''

# user input
thread = client.beta.threads.create()
user_input = ''
while (user_input != 'exit'):
    user_input = input("Enter your prompt: ")
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

    print(response.data[0].content[0].text.value)