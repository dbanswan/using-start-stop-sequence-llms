import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

messages = []


def add_user_message(message):
    messages.append({"role": "user", "content": message})


def add_system_message(message):
    messages.append(
        {
            "role": "assistant",
            "content": message,
        }
    )


def chat(stop_sequences=[]):
    message = client.messages.create(
        model="claude-3-5-haiku-latest",
        max_tokens=1000,
        temperature=1,
        system="You are a helpful assistant",
        messages=messages,
        stop_sequences=stop_sequences,
    )

    print(message.content[0].text)


add_user_message("write a json file with test user and their name, age")
add_system_message("```json")
chat(["```"])
