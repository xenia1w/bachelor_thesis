import openai

openai.api_key = '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'

prompt = 'Say hello'
response = openai.Completion.create(engine="davinci-003", prompt=prompt, max_tokens=40)

print(response)
