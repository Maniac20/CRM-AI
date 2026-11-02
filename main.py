from openai import OpenAI , RateLimitError , APIError
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv('GROQ_API_KEY')
model_name=os.getenv("MODEL_NAME")
if not  api_key:
    raise ValueError("GROQ_API_KEY is missing")


##make the object
client = OpenAI(
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    
    )

try:
    response = client.responses.create(
        model=model_name,
        input="What information do you need to find a customers deals?",
        instructions='You are a helpful CRM assitant.'
    )

    print(response.output_text)
    
except RateLimitError:
    print("API rate limit exceeded")
    
except APIError as e:
    print(f"{e.message}")