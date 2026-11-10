import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from schemas import CustomerDeals

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Generate sample CRM data for Rahul Sharma with two deals. Return JSON."
        }

    ],
    # response_format={"type": "json_object"}
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "customer_deals",
            "strict": True,
            "schema": CustomerDeals.model_json_schema()
        }
    }
)

# print(response)
# pass

content = response.choices[0].message.content

data = CustomerDeals.model_validate(json.loads(content))

print(data.model_dump())