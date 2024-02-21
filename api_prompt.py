import openai

# add here your personal API key that can be obtained from: https://platform.openai.com/api-keys
# following the best practice it is recommended to hide the actual key in a separate file
personal_api_key = ""

openai.api_key = personal_api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "<your_text_here>"},
        {"role": "assistant",
         "content": "<your_text_here>"},
        {"role": "user",
         "content": "<your_text_here>"}
    ],
    max_tokens=100
)

print(response)
