import os
from dotenv import load_dotenv
load_dotenv()

# this reads the data from the .env file and returns the value of the key
def get_key(key_name):
    return os.getenv(key_name)

def get_open_ai_key():
    return get_key('OPENAI_API_KEY')

def get_langchain_key():
    return get_key('LANGCHAIN_API_KEY')

def get_project_name():
    return get_key('LANGCHAIN_PROJECT')

def get_langsmith_v2_tracing():
    return get_key('LANGSMITH_TRACING_V2')

def get_huggingface_access_token():
    return get_key('HF_TOKEN')

