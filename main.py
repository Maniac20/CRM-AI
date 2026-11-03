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


conversation=[]
SYSTEM_INSTRUCTIONS="""
You are  an AI-powered CRM assitant.
Help users understand their customer and deal information.
Be concise and accurate.
You do not have direct access to CRM data.
Never invent customer records,deals or financial  values.
If CRM data is  unavailable , clearly say so.
"""

def chat(user_message):

    conversation.append({
        "role": "user",
        "content": user_message
    })

    response = client.responses.create(
        model=model_name,
        instructions=SYSTEM_INSTRUCTIONS,
        input=conversation
    )

    answer = response.output_text

    conversation.append({
        "role": "assistant",
        "content": answer
    })

    return answer


while True:
    message = input("\nYou: ")

    if message.lower() == "exit":
        break

    answer = chat(message)
    print("\nAssistant:", answer)
# try:
#     response = client.responses.create(
#         model=model_name,
#         input="What information do you need to find a customers deals?",
#         instructions='You are a helpful CRM assitant.'
#     )

#     print(response.output_text)
    
# except RateLimitError:
#     print("API rate limit exceeded")
    
# except APIError as e:
#     print(f"{e.message}")