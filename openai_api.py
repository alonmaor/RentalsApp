import openai
from common.constants import OPENAI_APIKEY_NAME, OPENAI_PROMPT


def generate_text(post, config):
    openai.api_key = config[OPENAI_APIKEY_NAME]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": OPENAI_PROMPT.format(post)}
        ]
    )
    print('------------------OPENAI RESPONSE-------------------')
    print(response)

    return response

