from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

# Twilio credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp_number = "whatsapp:+14155238886"

client = Client(account_sid, auth_token)

@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.json
    to = data['to']
    order_id = data['order_id']
    seller = data['seller_name']

    message_body = f"Hi {seller}, you have a new order! Order ID: {order_id}"

    message = client.messages.create(
        body=message_body,
        from_=from_whatsapp_number,
        to=f"whatsapp:{to}"
    )
    return {"status": "Message sent"}, 200

if __name__ == "__main__":
    app.run(debug=True)
