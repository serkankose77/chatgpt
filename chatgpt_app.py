from openai import OpenAI
import os
client = OpenAI()

# Function to load the API key from 'secrets.txt'


client.api_key = os.getenv("OPENAI_API_KEY")


def get_chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content # Corrected line

if __name__ == '__main__':
    while True:  # The loop starts here
        user_input = input("Enter your prompt (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'
        reply = get_chatgpt_response(user_input)
        print("ChatGPT:", reply)
