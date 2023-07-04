import openai

API_KEY = "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"

openai.api_key = API_KEY

def chat_with_gpt(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    if response.choices:
        return response.choices[0].text.strip()
    
    return None

while True:
    user_input = input("User: ")
    response = chat_with_gpt(user_input)
    if response:
        print("ChatGPT:", response)
    else:
        print("Failed to get a valid response from ChatGPT.")
