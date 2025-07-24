import os
import getpass

# Retrieve or insert API key for GROQ
def load_api_keys():
    if "GROQ_API_KEY" not in os.environ:
        os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")
