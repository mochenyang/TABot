# TABot: Build customized GPTs to Support Learning

This repo contains the code to leverage [customed GPTs](https://platform.openai.com/docs/assistants/overview) to support student learning by answering their questions based on your course content. It implements a basic Flask frontend and uses MongoDB to store queries and responses. To use it, follow the steps below:

1. Environment Setup (recommend using a virtual env):
```{python}
# edit the environment.yml file to specify your own env name
conda env create -f environment.yml
conda activate YOUR-ENV-NAME
```

2. OpenAI API Setup: generate your own API key. The code assumes you have registered the API key as an environmental variable named ```OPENAI_API_KEY```. Follow [this link](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) for API key best practices.

3. Install MongoDB for storing queries and messages:
    -  Install [MongoDB Community Server](https://www.mongodb.com/try/download/community) and craete the database / collection;
    - Modify ```app.py``` with the info of your database / collection.

4. Replace ```assistant_id``` in ```app.py``` with your own. Run the script to serve the app.


[TO-DO]:
- Implement user authentication
- Flask deployment