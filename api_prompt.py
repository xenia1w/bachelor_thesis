import os
import openai

openai.api_key = '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'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "AI Medical assistant helping a patient to fill in a survey. When the patient gives an answer do a general affirm their answer." }
    ],
    max_tokens=100
)

print(response)
