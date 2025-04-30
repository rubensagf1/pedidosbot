# app.py
from flask import Flask, render_template, request, redirect, url_for
from ai_engine import get_ai_response
from whatsapp_api import send_whatsapp_message
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        bot_name = request.form["bot_name"]
        api_key = request.form["api_key"]
        prompt = request.form["prompt"]
        phone_number = request.form["phone_number"]

        # Get AI response (welcome message)
        response = get_ai_response(prompt, api_key)

        # Send message via WhatsApp
        send_whatsapp_message(phone_number, response)

        return render_template("index.html", success=True, response=response)

    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
