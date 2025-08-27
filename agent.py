from openai import OpenAI
# Initialize client
client = OpenAI(api_key="************")

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You can also use "gpt-4" or "gpt-4o"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # Agent behavior
            {"role": "user", "content": prompt}  # User input
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = "Write a haiku about coding in Python."
    reply = chat_with_gpt(user_input)
    print("Agent:", reply)
