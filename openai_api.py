import openai
from common.constants import OPENAI_APIKEY, OPENAI_PROMPT

openai.api_key = OPENAI_APIKEY

def generate_text(post):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": OPENAI_PROMPT.format(post)}
        ]
    )
    print(response)

    return response

