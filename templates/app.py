import os
from flask import Flask, request, render_template
from openai import OpenAI
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        bot_name = request.form['bot_name']
        phone_number = request.form['phone_number']
        prompt = request.form['prompt']
        openai_key = request.form['openai_key']
        whatsapp_token = request.form['whatsapp_token']
        whatsapp_phone_id = request.form['whatsapp_phone_id']

        full_number = f"55{phone_number}"

        client = OpenAI(api_key=openai_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "Olá! Gostaria de ver o cardápio."}
            ]
        )

        message_text = response.choices[0].message.content

        url = f"https://graph.facebook.com/v18.0/{whatsapp_phone_id}/messages"
        headers = {
            "Authorization": f"Bearer {whatsapp_token}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": full_number,
            "type": "text",
            "text": {"body": message_text}
        }
        requests.post(url, headers=headers, json=data)

        return render_template('index.html', success=True)

    return render_template('index.html', success=False)
