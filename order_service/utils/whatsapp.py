from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox number

# ✅ List of recipients (in proper WhatsApp format)
TO_WHATSAPP_NUMBERS = [
    "whatsapp:+919361749744",
    "whatsapp:+917845268331",
    "whatsapp:+919655774432",
    "whatsapp:+917708441990"
]

def send_whatsapp_message(message):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        for number in TO_WHATSAPP_NUMBERS:
            print(f"📨 Sending to: {number}")
            client.messages.create(
                from_=TWILIO_WHATSAPP_NUMBER,
                body=message,
                to=number
            )
        print("✅ WhatsApp messages sent to all numbers!")

    except Exception as e:
        print("❌ Failed to send WhatsApp message:", e)
