from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("GROQ_API_KEY")

print(api_key)  # This should print your API key (optional for testing)
