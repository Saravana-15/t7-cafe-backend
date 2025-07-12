from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number
TO_WHATSAPP_NUMBER = "whatsapp:+919655774432"     # Your number

def send_whatsapp_message(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        print('msg', message)
        client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message,
            to=TO_WHATSAPP_NUMBER
        )

        print("✅ WhatsApp message sent!")
    except Exception as e:
        print("❌ Failed to send WhatsApp:", e)
