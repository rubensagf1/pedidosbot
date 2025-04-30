import openai

def get_ai_response(prompt, api_key):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "Você é um atendente de delivery educado e prestativo." },
            { "role": "user", "content": prompt }
        ]
    )

    return response.choices[0].message.content
